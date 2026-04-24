def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Saludar")
    print("2. Verificar número")
    print("3. Contar del 1 al 5")
    print("0. Salir")

    
def option_saludar():
    nombre = input("What is your name? ")
    print("hello", nombre)


def option_numero():
    numero = int(input("Write number:"))

    if numero > 0:
        print("The number is positive")
    elif numero < 0:
        print("the number is negative")
    else:
        print("the number is zero")


def option_contar():
    for i in range(1, 6):
        print(i)


def main():
    while True:
        mostrar_menu()
        opcion = input("Choose an option: ")

        if opcion == "1":
            option_saludar()
        elif opcion == "2":
            option_numero()
        elif opcion == "3":
            option_contar()
        elif opcion == "0":
            print("Finished")
            break
        else:
            print("invalid option")


main()



