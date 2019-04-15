
for num in range(0,11):
    print(num)

print("numeros pares")

def pares(maximo):
    for num in range(maximo):
        if(num % 2 == 0):
            yield num
maximo = 11
for numero in pares(maximo):
    print(numero)