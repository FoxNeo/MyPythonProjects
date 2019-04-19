def multiplicar(numero):
    return numero * 2

numeros = [2, 4, 6]
mapeo = map(multiplicar, numeros)
resultado = list(mapeo)
print(resultado)

# One line map
lista_resultado = list(map(multiplicar, numeros))
print(lista_resultado)

# map With Lambda
lista_resultado2 = list(map(lambda numero: numero * 2, numeros))
print(lista_resultado2)