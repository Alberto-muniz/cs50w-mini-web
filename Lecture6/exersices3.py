def save_numbers():

    with open("numbers.txt", "a") as file:
        while True:
            value = input("Enter a number(or 'q' to finish)")

            if value == "q":
                break

            file.write(value + "\n")


def read_number():
    numbers = []

    try:
        with open("numbers.txt") as file:
            for line in file:
                numbers.append(int(line.strip()))
    except FileNotFoundError:
        pass

    return numbers



def show_numbers(numbers):
    if len(numbers) == 0:
        print("No numbers saved. ")
        return
    
    for n in numbers:
        print(n)


def main():
    while True:
        print("\n1 -add numbers")
        print("2 - show numbers")
        print("3 - Exit")

        Option = input("Choose an option: ")

        if Option == "1":
            save_numbers()
        elif Option == "2":
            numbers = read_number()
            show_numbers(numbers)
        elif Option == "3":
            print("Goodbye!")
            break
        else:
            print("invalid option")

main()









