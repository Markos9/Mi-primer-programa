
apetece_helado_input = input("Te apetece un helado? (SI/NO): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Te he dicho que me digas si o no, no se que has dicho pero cuento como que no")
    apetece_helado = False
tienes_dinero_input = input("Tienes dinero para un helado? (SI/NO): ").upper()
esta_el_senor_de_los_helados_input = input("Esta el senor de los helados? (SI/NO): ").upper()
esta_tu_tia_input = input("Estas con tu tia? (SI/NO): ").upper()



apetece_helado = apetece_helado_input == "SI"
tienes_dinero = tienes_dinero_input == "SI"
esta_tu_tia = esta_tu_tia_input == "SI"
puede_permitirselo = tienes_dinero or esta_tu_tia
esta_el_senor_de_los_helados = esta_el_senor_de_los_helados_input == "SI"

if apetece_helado and puede_permitirselo and esta_el_senor_de_los_helados:
    print("Toma tu helado")
else:
    print("Pues nada")
