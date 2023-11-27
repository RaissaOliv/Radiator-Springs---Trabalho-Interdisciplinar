import psycopg2

conn = psycopg2.connect(dbname="dirigindomeucarro", user="postgres", password="5932652225rai")

cur = conn.cursor()

def listar_carro_modelo(input: str):
  try:
    cur.execute('SELECT MODELO, PRECO_INICIAL, PRECO_DIARIO FROM carros WHERE modelo = %s', (input,))   
    linha = cur.fetchone()
    if linha is not None:
      modelo, preco_inicial, preco_diario = linha
      carro = {
          'modelo': modelo,
          'preco_inicial': preco_inicial,
          'preco_diario': preco_diario,
          }
      return carro
    else:
      return None
  except Exception as e:
    print("Erro ao selecionar os dados:", str(e))
    return None


def listar_carros():
    try:
      cur.execute("SELECT * FROM carros")
      resultados = cur.fetchall()
      carros = []
      for linha in resultados:
        id, marca, modelo, ano, placa, preco_inicial, preco_diario, disponivel, popular, luxo = linha
        carro = {
          'id': id,
          'marca': marca,
          'modelo': modelo,
          'ano': ano,
          'placa': placa,
          'preco_inicial': preco_inicial,
          'preco_diario': preco_diario,
          'disponivel': disponivel,
          'popular': popular,
          'luxo': luxo
          }
        carros.append(carro)
      return carros
    except Exception as e:
        print("Erro ao selecionar os dados:", str(e))
        return []

def listar_carro_pesquisa(input: str):
    try:
      cur.execute('SELECT * FROM carros WHERE modelo = %s', (input,))   
      resultados = cur.fetchall()
      carros = []
      for linha in resultados:
        id, marca, modelo, ano, placa, preco_inicial, preco_diario, disponivel, popular, luxo = linha
        carro = {
          'id': id,
          'marca': marca,
          'modelo': modelo,
          'ano': ano,
          'placa': placa,
          'preco_inicial': preco_inicial,
          'preco_diario': preco_diario,
          'disponivel': disponivel,
          'popular': popular,
          'luxo': luxo
          }
        carros.append(carro)
      return carros
    except Exception as e:
        print("Erro ao selecionar os dados:", str(e))
        return []



def listar_carros_disponiveis():
    try:
      cur.execute("SELECT * FROM carro_disponivel")
      resultados = cur.fetchall()
      carro_disponivel = []
      for linha in resultados:
        id, marca, modelo, ano, placa, preco_inicial, preco_diario, disponivel = linha
        carro = {
          'id': id,
          'marca': marca,
          'modelo': modelo,
          'ano': ano,
          'placa': placa,
          'preco_inicial': preco_inicial,
          'preco_diario': preco_diario,
          'disponivel': disponivel
          }
        carro_disponivel.append(carro)
      return carro_disponivel
    except Exception as e:
        print("Erro ao selecionar os dados:", str(e))
        return []


def listar_carros_popular():
    try:
      cur.execute("SELECT * FROM carro_popular")
      resultados = cur.fetchall()
      carro_popular = []
      for linha in resultados:
        id, marca, modelo, ano, placa, preco_inicial, preco_diario, disponivel, popular = linha
        carro = {
          'id': id,
          'marca': marca,
          'modelo': modelo,
          'ano': ano,
          'placa': placa,
          'preco_inicial': preco_inicial,
          'preco_diario': preco_diario,
          'disponivel': disponivel,
          'popular': popular
          }
        carro_popular.append(carro)
      return carro_popular
    except Exception as e:
        print("Erro ao selecionar os dados:", str(e))
        return []
      
def listar_carros_luxo():
    try:
      cur.execute("SELECT * FROM carro_luxo")
      resultados = cur.fetchall()
      carro_luxo = []
      for linha in resultados:
        id, marca, modelo, ano, placa, preco_inicial, preco_diario, disponivel, luxo = linha
        carro = {
          'id': id,
          'marca': marca,
          'modelo': modelo,
          'ano': ano,
          'placa': placa,
          'preco_inicial': preco_inicial,
          'preco_diario': preco_diario,
          'disponivel': disponivel,
          'luxo': luxo
          }
        carro_luxo.append(carro)
      return carro_luxo
    except Exception as e:
        print("Erro ao selecionar os dados:", str(e))
        return []
      
        
def listar_reservas():
  try:
    cur.execute(" SELECT * FROM listar_reservas")
    resultados = cur.fetchall()
    reservas = []
    
    for linha in resultados:
      id_reserva, nome_cliente, modelo_carro, marca_carro, data_inicio, data_fim = linha
      reserva = {
        'id_reserva': id_reserva,
        'nome_cliente': nome_cliente,
        'modelo_carro': modelo_carro,
        'marca_carro': marca_carro,
        'data_inicio': data_inicio,
        'data_fim': data_fim
        }
      reservas.append(reserva)
    return reservas
      
  except:  
    print("Erro ao selecionar os dados")
        
def listar_alugueis():
    try:
      cur.execute("SELECT * FROM listar_alugueis")
      resultados = cur.fetchall()
      alugueis = []

      for linha in resultados:
        id_aluguel, nome_cliente, email_cliente, modelo_carro, marca_carro, data_aluguel, data_devolucao, valor_total = linha
        aluguel = {
          'id_aluguel': id_aluguel,
          'nome_cliente': nome_cliente,
          'email_cliente': email_cliente,
          'modelo_carro': modelo_carro,
          'marca_carro': marca_carro,
          'data_aluguel': data_aluguel,
          'data_devolucao': data_devolucao,
          'valor_total': valor_total
          }
        alugueis.append(aluguel)

      return alugueis

    except Exception as e:
        print("Erro ao selecionar os dados:", str(e))