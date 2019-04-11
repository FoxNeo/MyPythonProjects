import json

values = { "nombre": "silla", "color": "blanco", "precio":100}
# Python to JSON
data = json.dumps(values)
print(data)

# convert JSON to Python dictionary
product = json.loads(data)
print(product)
print(product["nombre"])