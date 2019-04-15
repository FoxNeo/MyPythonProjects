#pydoc - generate automat documentation

class Saludos:
    """
    Esta es la documentación de la clase silla
    Tendra dos funciones buenos_dias y adios
    y ambas será necesario pasarle un parametro con el nombre de la persona
    """
    def buenos_dias(self, nombre):
        """ Sirve para dar los buenos días a un nombre pasado como parametro"""
        print("Buenos días {}".format(nombre))

    def adios(self, nombre):
        """ Sirve para decir adios a un nombre pasado como parametro"""
        print("Adios {}".format(nombre))