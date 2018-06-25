
tipo_operacion = input("Que operacion quieres realizar? (Multiplicar / Dividir / Sumar / Restar): ")

primer_numero = int(input("Primer numero:"))
segundo_numero = int(input("Segundo numero:"))

if tipo_operacion == "Multiplicar":
    resultado_multiplicar = primer_numero * segundo_numero
    print("El resultado es {}".format(resultado_multiplicar))

elif tipo_operacion == "Dividr":
    resultado_dividir = primer_numero / segundo_numero
    print("El resultado es {}".format(resultado_dividir))

elif tipo_operacion == "Sumar":
    resultado_sumar = primer_numero + segundo_numero
    print("El resultado es {}".format(resultado_sumar))

elif tipo_operacion == "Restar":
    resultado_restar = primer_numero - segundo_numero
    print("El resultado es {}".format(resultado_restar))
