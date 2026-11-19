def calculate_average(grades):
    if len(grades) == 0:
        return 0

    total = 0
    for grade in grades:
        total += grade

    average = total / len(grades)
    return average



grades = [80, 90, 70]
avg = calculate_average(grades)
print(avg)