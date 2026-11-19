import sqlite3

def create_table():
    conn = sqlite3.connect("grades.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grade INTEGER
        )
    """)
    pass

def insert_grade():
     grade = input("Enter your Grade: ")
     conn = sqlite3.connect("grades.db")
     cursor = conn.cursor()
     
     
     cursor.execute(
        "INSERT INTO grades (grade) VALUES (?)",
        (grade,)
    )
     
     conn.commit()
     conn.close()

def read_grades():
    conn = sqlite3.connect("grades.db")
    cursor = conn.cursor()

    cursor.execute("SELECT grade FROM grades")

    rows = cursor.fetchall()

    conn.close()

    if len(rows) == 0:
        print("no Grades saved")
        return
    
    for row in rows:
        print(row[0])



def show_average():
    conn = sqlite3.connect("grades.db")
    cursor = conn.cursor()

    cursor.execute("SELECT AVG (grade) FROM grades")
    row = cursor.fetchone()


    if row[0] is None:
        print("No grades to calculate average.")
        return
    
    print("average grade:", row[0])
    



    pass


def clear_grades():
    conn = sqlite3.connect("grades.db")
    cursor = conn.cursor()


    cursor.execute("DELETE FROM grades")

    conn.commit()
    conn.close()

    print("All grades deleted.")
    pass


def main():

    create_table()

    while True:
        print("1 - add grade")
        print("2 - show grades")
        print("3 - show average")
        print("4 - Clear grades")
        print("5 - Exit")

        option = input("Choose and option: ")

        if option == "1":
            insert_grade()

        elif option == "2":
            read_grades()

        elif option == "3":
            show_average()

        elif option == "4":
            clear_grades()

        elif option == "5":
            print("goodbye!")
            break
        
        else:
            print("Invalid Option")

main()




