import sqlite3


# ---------- CREAR TABLA ----------
def create_table():
    conn = sqlite3.connect("numbers.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS numbers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value INTEGER
        )
    """)

    conn.commit()
    conn.close()


# ---------- INSERTAR NÚMERO ----------
def insert_number():
    value = input("Enter a number: ")

    conn = sqlite3.connect("numbers.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO numbers (value) VALUES (?)",
        (value,)
    )

    conn.commit()
    conn.close()


# ---------- LEER NÚMEROS ----------
def read_numbers():
    conn = sqlite3.connect("numbers.db")
    cursor = conn.cursor()

    cursor.execute("SELECT value FROM numbers")
    rows = cursor.fetchall()

    conn.close()

    if len(rows) == 0:
        print("No numbers saved.")
        return

    for row in rows:
        # row es una tupla, ejemplo: (10,)
        print(row[0])


# ---------- BORRAR TODOS LOS NÚMEROS ----------
def clear_numbers():
    conn = sqlite3.connect("numbers.db")
    cursor = conn.cursor()

    # SQL que borra TODAS las filas de la tabla
    cursor.execute("DELETE FROM numbers")

    conn.commit()
    conn.close()

    print("All numbers deleted.")


# ---------- FUNCIÓN PRINCIPAL ----------
def main():
    create_table()

    while True:
        print("\n1 - Add number")
        print("2 - Show numbers")
        print("3 - Exit")
        print("4 - Clear numbers")  # 👈 NUEVA OPCIÓN

        option = input("Choose an option: ")

        if option == "1":
            insert_number()

        elif option == "2":
            read_numbers()

        elif option == "3":
            print("Goodbye!")
            break

        elif option == "4":
            clear_numbers()  # 👈 LLAMAMOS A LA FUNCIÓN NUEVA

        else:
            print("Invalid option")


# EJECUTA EL PROGRAMA
main()