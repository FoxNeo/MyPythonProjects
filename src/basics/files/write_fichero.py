# create a txt file

content = "Hola, esta es la linea que vamos a grabar en el fichero"

fichero = open("fichero_generado.txt", "wt")

fichero.write(content)

fichero.close()