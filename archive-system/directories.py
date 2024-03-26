import os

# CREAR CARPETA:
if not os.path.isdir("./my_folder"):
# Asì creamos un directorio, tal cual como se hace en MacOS y Linux (tambièn ya se puede en Powershell de Windows)
    os.mkdir("./my_folder")
else: 
    print("El directorio ya existe")
    
"""
# ELIMINAR CARPETA:
if os.path.isdir('./my_folder/'):
    os.rmdir('./my_folder/')
    print("Se eliminò el directorio")
else:
    print("Ya se ha eliminado el directorio")



# Tambièn se puede copiar una carpeta CON TODO Y CONTENIDOS:
import shutil

original_rute = "./my_folder/"
new_rute = "./my_folder_2/"

shutil.copytree(original_rute, new_rute)



import shutil

# ELIMINAR CARPETAS NO VACÌAS:
shutil.rmtree('./my_folder_2/')
"""

# LISTANDO EL CONTENIDO DE MI CARPETA:
print("Contenido de mi carpeta: ")
content = os.listdir('./my_folder/')
# print(content)

# PODEMOS RECORRER EL CONTENIDO DE LA CARPETA:
for folder in content:
    print("El fichero: " + folder)