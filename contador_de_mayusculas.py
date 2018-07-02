
texto_usuario = input("Introduce una frase: ")

mayusculas = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]

n_mayusculas = 0

for letra in texto_usuario:
    if letra in mayusculas:
        n_mayusculas += 1

print("Hay un total de {} mayusculas en la frase {}".format(n_mayusculas,texto_usuario))

