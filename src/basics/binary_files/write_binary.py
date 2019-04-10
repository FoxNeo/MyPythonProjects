import pickle

list_cars = ["Audi", "Ford", "Toyota", "BMW"]

fichero = open("fichero_cars.pckl", "wb") # write binary file .pckl

pickle.dump(list_cars, fichero)

fichero.close()