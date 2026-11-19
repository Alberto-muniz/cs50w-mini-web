def save_expenses():
    with open("expenses.txt", "a") as file:
        while True:
            value = input("Enter a expense(or 'q' to finish): ")

            if value == "q":
                break

            file.write(value + "\n")


def read_expenses():
    expenses = []

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                expenses.append(int(line.strip()))
    except FileNotFoundError:
        pass
           
    return expenses
    

def calculate_total(expenses):
    total = 0 
    for expense in expenses:
        total += expense
    return total
    

def calculate_average(expenses):
    if len(expenses) == 0:
        return 0 
    return calculate_total(expenses) / len(expenses)


def main():
    save_expenses()

    expenses = read_expenses()
    total = calculate_total(expenses)
    average = calculate_average(expenses)

    print("total expenses:",total)
    print("average expense:", average)

main()



