# simple function
def greet():
    print("Hi!")
greet()

# function with param
def greetParam(name):
    print("Hello "+ name)

name = "Anika"
greetParam(name)

# calculate
def sum(num1, num2):
    return num1 + num2

print(sum(5,3))

# Reference
colors = ["red", "green", "blue"]

def inject_colors(colors, color):
    colors.append(color)

newColor = "black"
inject_colors(colors, newColor)

print(colors)