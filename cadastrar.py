#métodos de reservar, cadastrar e alugar aqui
import psycopg2
from datetime import datetime
import listas
conn = psycopg2.connect(dbname="dirigindomeucarro", user="postgres", password="5932652225rai")

cur = conn.cursor()

def cadastrar_usuario(nome, email, telefone):
    try:
        cur.execute("INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)", (nome, email, telefone))
        return "usuario " + nome + " cadastrado!"
    except Exception as e:
        print(e)
        return e

def get_usuario_id(email):
    try:
        cur.execute("SELECT cliente_id FROM clientes WHERE email = %s", (email,))  
        linha = cur.fetchone()
        if linha is not None:
            cliente_id = linha[0]  
            return cliente_id
        else:
            return None
    except Exception as e:
        print("Erro ao selecionar os dados:", str(e))
        return e

def get_carro_id(modelo):
    try:
        cur.execute("SELECT carro_Id FROM carros WHERE modelo = %s", (modelo,))
        carro_id = cur.fetchone()
        if carro_id is not None:
            return carro_id[0]
        else:
            return "Nenhum carro encontrado com o modelo especificado."
    except Exception as e:
        print(e)
        return str(e)
    
def cadastrar_reserva(email, modelo, datainicio, datafim):
    try:
        cur.execute("INSERT INTO reservas (cliente_id, carro_id, data_inicio, data_fim) VALUES (%s, %s, %s, %s)",
                     (get_usuario_id(email),
                      get_carro_id(modelo),
                      datainicio,
                      datafim))
        return "Reserva do carro " + modelo + " realizada!"
    except Exception as e:
        return e

def cadastrar_aluguel(email, modelo, datainicio, datafim):
    try:
        carroA = listas.listar_carro_modelo(modelo)
        carro_inicial = float(carroA['preco_inicial'].replace('R$', '').replace(',', '.').replace('.', ''))
        carro_diario= float(carroA['preco_diario'].replace('R$', '').replace(',', '.').replace('.', ''))
        data1 = datetime.strptime(datainicio, '%Y-%m-%d')
        data2 = datetime.strptime(datafim, '%Y-%m-%d')
        diferenca = data2 - data1
        dias = diferenca.days
        funcao = (carro_inicial + float(dias) * carro_diario)
        cur.execute("INSERT INTO alugueis (cliente_id, carro_id, data_aluguel, data_devolucao, valor_total) VALUES (%s, %s, %s, %s, %s)",
                     (get_usuario_id(email),
                      get_carro_id(modelo),
                      datainicio,
                      datafim,
                      float(funcao)))
        return "aluguel do carro " + modelo + " realizada!"
    except Exception as e:
        return e