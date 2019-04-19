def positivo(numero):
    if (numero > 0):
        return True
    else:
        return False

numeros = [4,-2, 8, -3, -5, -7, 1, 9]
filtro = filter(positivo, numeros) # [4, 8, 1, 9]

result = list(filtro)
print(result)