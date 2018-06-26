
mi_lista = []
input_usuario = input("Que necesitas comprar? (escribe FIN para salir): ")

while input_usuario != "Fin":
    mi_lista.append(input_usuario)
    input_usuario = input("Que necesitas comprar? (escribe FIN para salir): ")

largo_lista = len(mi_lista)
indice_actual = 0

for item in mi_lista:
    print("Tengo que comprar {}".format(item))

print("Esta es la lista de la compra")
