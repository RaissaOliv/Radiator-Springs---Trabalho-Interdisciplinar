def calcularMelhorCarro(carroA, carroB, dias):
    carro_a_inicial = float(carroA['preco_inicial'].replace('R$', '').replace(',', '.').replace('.', ''))
    carro_b_inicial= float(carroB['preco_inicial'].replace('R$', '').replace(',', '.').replace('.', ''))
    carro_a_diario= float(carroA['preco_diario'].replace('R$', '').replace(',', '.').replace('.', ''))
    carro_b_diario= float(carroB['preco_diario'].replace('R$', '').replace(',', '.').replace('.', ''))

    formula = (carro_a_inicial + float(dias) * carro_a_diario) - (carro_b_inicial + float(dias) * carro_b_diario)
    if formula > 0:
       return carroA['modelo'] + " é melhor que " + carroB['modelo'] + " em uma viagem de " + dias + " dias."
    
    elif formula < 0:
        return carroB['modelo'] + " é melhor que " + carroA['modelo'] + " em uma viagem de " + dias + " dias."
    
    else:
        return carroA['modelo'] + " tem a mesma performance que " + carroB['modelo'] + " em uma viagem de " + dias + " dias."
