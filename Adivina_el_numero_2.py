
number_to_guess = int(input("Numero a adivinar (Que tu compañero no lo vea): "))

user_number = int(input("Adivina el numero: "))

while number_to_guess != user_number:
    user_number = int(input("Adivina el numero: "))

    if number_to_guess == user_number:
        print("Has acertado, el nuemro es: {}! ".format(number_to_guess))
