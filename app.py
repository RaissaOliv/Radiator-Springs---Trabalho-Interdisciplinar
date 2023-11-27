from flask import Flask, render_template, request
import listas, comparar, cadastrar
import psycopg2

conn = psycopg2.connect(dbname="dirigindomeucarro", user="postgres", password="5932652225rai")

cur = conn.cursor()

app = Flask(__name__)

# Mock data
carros = [
    {"id": 1, "modelo": "Carro A", "preco_diaria": 100, "preco_base": 500},
    {"id": 2, "modelo": "Carro B", "preco_diaria": 80, "preco_base": 400}
    # Adicione mais carros conforme necessário
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare_cars')
def compare_cars():
    return render_template('compare_cars.html', carros=listas.listar_carros())

@app.route('/compare_cars_resultado', methods=['GET', 'POST'])
def compare_cars_resultado():
    carro_a = request.form.get("carro_a")
    carro_b = request.form.get("carro_b")
    dias = request.form.get('dias')
    carro_a = listas.listar_carro_modelo(carro_a)
    carro_b = listas.listar_carro_modelo(carro_b)
    resultado = comparar.calcularMelhorCarro(carro_a, carro_b, dias)
    return render_template('compare_cars_resultado.html', carros=listas.listar_carros(), resultado = resultado)

@app.route('/car_list')
def car_list():
    return render_template('car_list.html', carros=listas.listar_carros())

@app.route('/car_list_disponiveis')
def car_list_disponiveis():
    return render_template('car_list_disponiveis.html', carros_disponiveis=listas.listar_carros_disponiveis())

@app.route('/car_list_populares')
def car_list_populares():
    return render_template('car_list_populares.html', carros_popular=listas.listar_carros_popular())

@app.route('/car_list_luxo')
def car_list_luxo():
    return render_template('car_list_luxo.html', carros_luxo=listas.listar_carros_luxo())

@app.route('/adm')
def adm():
    reservas_list = listas.listar_reservas()
    alugueis_list = listas.listar_alugueis()
    return render_template('adm.html', reservas=reservas_list, alugueis=alugueis_list)

@app.route('/alugar')
def alugar():
    return render_template('alugar.html', carros_disponiveis=listas.listar_carros_disponiveis(), carros=listas.listar_carros())

@app.route('/alugar_result_cadastro', methods=['POST', 'GET'])
def alugar_result_cadastro():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    cadastro = cadastrar.cadastrar_usuario(nome, email, telefone)
    return render_template('alugar_result_cadastro.html',
                            carros_disponiveis=listas.listar_carros_disponiveis(),
                            carros=listas.listar_carros(),
                            cadastrou=cadastro)

@app.route('/alugar_result', methods=['POST', 'GET'])
def alugar_result():
    email = request.form.get('emailreserva')
    modelo = request.form.get('carro_a')
    datareserva = request.form['datareserva']
    datadevolucao = request.form['datadevolucao']
    resultado = cadastrar.cadastrar_aluguel(email, modelo, datareserva, datadevolucao)
    return render_template('alugar_result.html', 
                           resultado = resultado,
                           carros_disponiveis = listas.listar_carros_disponiveis(),
                           carros=listas.listar_carros())

@app.route('/reservar')
def reservar():
    return render_template('reservar.html', carros_disponiveis=listas.listar_carros_disponiveis(), carros=listas.listar_carros())

@app.route('/reservar_result_cadastro', methods=['POST', 'GET'])
def reservar_result_cadastro():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    cadastro = cadastrar.cadastrar_usuario(nome, email, telefone)
    return render_template('reservar_result_cadastro.html',
                            carros_disponiveis=listas.listar_carros_disponiveis(),
                            carros=listas.listar_carros(),
                            cadastrou=cadastro)

@app.route('/reservar_result', methods=['POST', 'GET'])
def reservar_result():
    email = request.form.get('emailreserva')
    modelo = request.form.get('carro_a')
    datareserva = request.form['datareserva']
    datadevolucao = request.form['datadevolucao']
    resultado = cadastrar.cadastrar_reserva(email, modelo, datareserva, datadevolucao)
    return render_template('reservar_result.html', 
                           reservou = resultado,
                           carros_disponiveis = listas.listar_carros_disponiveis(),
                           carros=listas.listar_carros())

@app.route('/car_details/<int:car_id>')
def car_details(car_id):
    carro = next((c for c in carros if c['id'] == car_id), None)
    if carro:
        return render_template('car_details.html', carro=carro)
    else:
        return "Carro não encontrado", 404
    
@app.route('/search', methods=['GET', 'POST'])
def search():
    busca = ""
    resultados = []

    if 'modelo' in request.form:
        busca = request.form['modelo']
        resultados = listas.listar_carro_pesquisa(busca)

    return render_template('search.html', resultados=resultados, busca=busca)

@app.route('/search_result', methods=['GET','POST'])
def search_result():
    modelo = request.form.get('inputPesquisa')
    resultados = listas.listar_carro_pesquisa(modelo)
    return render_template('search_result.html', resultados = resultados, busca=modelo, carros=resultados)
# Adicione mais rotas conforme necessário

if __name__ == '__main__':
    app.run(debug=True)
