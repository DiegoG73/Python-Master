"""
Para trabajar con los ficheros en Python, es necesario utilizar un mòdulo en concreto
es el mòdulo open en el paquete io
"""
from io import open
import pathlib
import shutil

# Abrir archivo (De la mejor manera):
rute = str(pathlib.Path().absolute()) + "/text_file.txt"
archive = open(rute, "a+")

# Escribiendo dentro de un archivo
archive.write("********Soy un texto metido desde Python********\n")

# Cerrando un archivo (ES IMPORTANTE CERRAR EL ARCHIVO DESPUÈS DE UTILIZARLO)
archive.close()

# Abrir archivo para leer de èl
rute = str(pathlib.Path().absolute()) + "/text_file.txt"
# Aquì, cambiamos la "a+", por una "r" de "read"/"lectura"
read_archive = open(rute, "r")

# Leer contenido:
# content = read_archive.read()

# Hacer que Python me muestre el contenido por pantalla
# print(content)


"""
# Hacer que Python lea el contenido linea a linea
list = read_archive.readlines()
read_archive.close()

# Mostrar lista y recorrerla
for phrase in list:
    if not  phrase.isnumeric():
        print("- " + phrase.upper())
        
for phrase in list:
    phrase_list = phrase.split()
    print(phrase_list)
    #print("- ")
    
for phrase in list:
    print("- " + phrase.capitalize())
    
"""

"""
# Copiar un archivo, nombrarlo y eliminarlo
original_rute = str(pathlib.Path().absolute()) + "/text_file.txt"
#              ruta absoluta:            |
new_rute = str(pathlib.Path().absolute()) + "/copied_file.txt"
alternative_rute = str(pathlib.Path().absolute()) + "/../packages/copied_file2.txt"
shutil.copyfile(original_rute, alternative_rute)


# renombrar archivo:
original_rute = str(pathlib.Path().absolute()) + "/copied_file.txt"
new_rute = str(pathlib.Path().absolute()) + "/NEW_copied_file.txt"

shutil.move(original_rute, new_rute)
"""

# Eliminar:
import os

new_rute = str(pathlib.Path().absolute()) + "/NEW_copied_file.txt"
# os.remove(new_rute)

# Comprobar si existe un archivo o no:
import os.path
#print(os.path.abspath("../"))

#Ruta absoluta
proove_rute = os.path.abspath("./") + "/text_file.txt"
# Ruta relativa
proove_rute = "./file.py"

if os.path.isfile(proove_rute):
    print("El archivo existe")
else: 
    print("El archivo no existe")