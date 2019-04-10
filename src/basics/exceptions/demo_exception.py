try:
    num1 = 5
    num2 = 0
    div = num1 / num2
    print(div)
except ZeroDivisionError:
    print("Error, division entre cero")
except:
    print("Something went wrong!")
else:
    print("La división funciono!")
finally:
    print("Esta prueba de try se ha acabado")