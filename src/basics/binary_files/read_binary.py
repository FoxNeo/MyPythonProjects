import pickle

fichero = open("fichero_cars.pckl", "rb") # read binary

readed_list = pickle.load(fichero)

print(readed_list)