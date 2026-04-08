while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Saludar")
    print("2. Verificar si un número es positivo o negativo")
    print("3. Contar del 1 al 5")
    print("0. Salir")

    option = input("Elige una opción: ")

    if option == "1":
        name = input("¿Cómo te llamas? ")
        print("Hola", name)

    elif option == "2":
        number = int(input("Escribe un número: "))
        if number > 0:
            print("El número es positivo")
        elif number < 0:
            print("El número es negativo")
        else:
            print("El número es cero")

    elif option == "3":
        for i in range(1, 6):
            print(i)

    elif option == "0":
        print("Programa terminado")
        break

    else:
        print("Opción no válida, intenta de nuevo")