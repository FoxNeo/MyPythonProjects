class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print("Hello my name is {} and I am {} years old".format(self.name, self.age))

worker = Person("Alina", 21)
print(worker.age)
print(worker.name)
worker.sayHello()