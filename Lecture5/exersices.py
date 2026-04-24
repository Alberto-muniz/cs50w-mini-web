def get_number():
    numbers = []

    while True:
        value = input("Enter a number (or 'q' to finish): ")

        if value == "q":
            break

        numbers.append(int(value))

    return numbers


def calculate_total(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return calculate_total(numbers) / len(numbers)


def get_max(numbers):
    if len(numbers) == 0:
        return None
    return max(numbers)


def show_results(total, average, maximum):
    print("total: " , total)
    print("Average: ", average)
    print("Max: ", maximum)

def main():
    numbers = get_number()
    total = calculate_total(numbers)
    average = calculate_average(numbers)
    maximun = get_max(numbers)
    show_results(total, average, maximun)



    
main()






