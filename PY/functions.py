def menu():
    while True:
        print("\n1. Saludar")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            print("Hola")
        elif opcion == "0":
            print("Adiós")
            break
        else:
            print("Opción inválida")

menu()