def converterValores(preco):
    total = 0
    value = preco.replace('R$', '')

    if '.' in value:
        thousands, decimals = value.split(',')
        thousands = float(thousands.replace('.', ''))
        decimals = float(decimals.replace(',','.'))
        decimals = float(decimals) / 100
    else:
        thousands = float(value.replace('.', '').replace(',','.'))
        decimals = 0
    total += thousands + decimals
    return total


def calcularMelhorCarro(carroA, carroB, dias):
    carro_a_inicial = converterValores(carroA['preco_inicial'])
    carro_b_inicial= converterValores(carroB['preco_inicial'])
    carro_a_diario= converterValores(carroA['preco_diario'])
    carro_b_diario= converterValores(carroB['preco_diario'])
    f1 = (carro_a_inicial + float(dias) * carro_a_diario)
    f2 = (carro_b_inicial + float(dias) * carro_b_diario)
    formula = f1 - f2
    if formula > 0:
       return carroA['modelo'] + " (preço: "+ str(f1) + ") é melhor que " + carroB['modelo'] + " preço: "+ str(f2) +" em uma viagem de " + dias + " dias."
    
    elif formula < 0:
        return carroB['modelo'] + " (preço: "+ str(f2) + ") é melhor que " + carroA['modelo'] + " (preço: "+ str(f1) +") em uma viagem de " + dias + " dias."
    
    else:
        return carroA['modelo'] + " (preço: "+ str(f1) + ") tem a mesma performance que " + carroB['modelo'] + " (preço: "+ str(f2) + ") em uma viagem de " + dias + " dias."
