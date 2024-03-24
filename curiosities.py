# Cuando creamos una variable, no debemos poner tildes ni caracteres raros como los que se usan en el español
my_text = "Hello"
# my-text2 = "World" Èsto nos darà un error ya que el guiòn medio no se puede colocar en el nombre de la variable
# Lo que si es correcto:
my_text2 = "World"


# Concatenar texto
unit_text = my_text + my_text2
print(unit_text)

# PARA USAR COMILLAS DOBLES EN UN STRING INICIALIZADO CON COMILLAS DOBLES, HACEMOS LO SIGUIENTE:
my_text3 = "On \"Python\""
print(my_text3)

my_text4 = 'On "Python" '
print(my_text4)