def save_numbers():
    with open("number.txt", "a") as file:
        while True:
            value = input("Enter a expense(or 'q' to finish): ")

            if value == "q":
                break

            file.write(value + "\n")


def read_numbers():
    numbers = []

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                numbers.append(int(line.strip()))
    except FileNotFoundError:
        pass
           
    return numbers
    
def main():
    save_numbers()

    numbers = read_numbers()

    if len(numbers) == 0:
        print("NO numbers saved.")
        return

    
    print("total number:",len(numbers))
    print("Last number entered:", numbers[-1])


main()


