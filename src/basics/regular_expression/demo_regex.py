# regex in python
text = "Hola, mi nombre es Larry"
import re

# search
result = re.search("nombre", text) # returns match object
if (result):
    print("Match found")
else:
    print("Not found")

# findall
body = """
El coche de Luis es rojo,
El coche de Antony es blanco
y el coche de Maria es rojo
"""
print(re.findall("coche.*rojo", body))

# split
header = "La silla es blanca y vale 80"
print(re.split("\s", header))

# sub
print(re.sub("blanca", "roja", header))