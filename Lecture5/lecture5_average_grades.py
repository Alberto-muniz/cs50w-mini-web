def get_grades():
    grades = []

    while True:
        grade = input("Enter a grade (or 'q' to finish): ")

        if grade == "q":
            break

        grades.append(int(grade))

    return grades
    
def calculate_average(grades):
    if len(grades) == 0:
        return 0
    
    total = 0
    for grade in grades:
        total += grade

    average = total / len(grades)
    return average

def show_result(average):
    print("Average grade" , average)


def main():
    grades = get_grades()
    average = calculate_average(grades)
    show_result(average)

main()

