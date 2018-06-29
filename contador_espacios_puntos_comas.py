
texto_usuario = input("Introduce una frase: ")

puntos = "."
comas = ","
espacios = " "

n_puntos = 0
n_comas = 0
n_espacios = 0

for letra in texto_usuario:
    if letra in puntos:
        n_puntos += 1
    elif letra in comas:
        n_comas += 1
    elif letra in espacios:
        n_espacios += 1


print("La cantidad de puntos en la frase es de: {}".format(n_puntos))
print("La cantidad de comas en la frase es de: {}".format(n_comas))
print("La cantidad de espacios en la frase es de: {}".format(n_espacios))
