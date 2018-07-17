
lista_original = ["hola",1,4,"helado"]

lista_numeros = []

lista_strings = []

for dato in lista_original:
    if type(dato) == type(str()):
        lista_strings.append(dato)
    elif type(dato) == type(int()):
        lista_numeros.append(dato)

print("Estos son los numeros: {}".format(lista_numeros))
print("Estos son las strings: {}".format(lista_strings))
