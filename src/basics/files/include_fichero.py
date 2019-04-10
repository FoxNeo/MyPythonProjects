fichero = open("fichero_generado.txt", "at") # a = append
cadena_para_incluir = "\nEsta es la siguiente linea de fichero"
fichero.write(cadena_para_incluir)
fichero.close()