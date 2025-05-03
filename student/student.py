import mysql.connector
from mysql.connector import Error

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="student_db"
    )

def get_valid_roll_number(prompt):
    while True:
        roll_input = input(prompt)
        if roll_input.isdigit():
            return int(roll_input)
        print("❗ Invalid input. Please enter a valid number.")

def add_student():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        roll = get_valid_roll_number("Enter Roll Number: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        email = input("Enter Email: ")

        query = "INSERT INTO students (roll_number, name, department, email) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (roll, name, dept, email))
        conn.commit()
        print("✅ Student added successfully.")
    except Error as e:
        print(f"❌ Error: {e}")
    finally:
        cursor.close()
        conn.close()

def view_students():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(f"Roll: {row[0]}, Name: {row[1]}, Dept: {row[2]}, Email: {row[3]}")
        else:
            print("⚠️ No records found.")
    except Error as e:
        print(f"❌ Error: {e}")
    finally:
        cursor.close()
        conn.close()

def search_student():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        roll = get_valid_roll_number("Enter Roll Number to Search: ")
        cursor.execute("SELECT * FROM students WHERE roll_number = %s", (roll,))
        row = cursor.fetchone()
        if row:
            print(f"Roll: {row[0]}, Name: {row[1]}, Dept: {row[2]}, Email: {row[3]}")
        else:
            print("⚠️ Student not found.")
    except Error as e:
        print(f"❌ Error: {e}")
    finally:
        cursor.close()
        conn.close()

def update_student():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        roll = get_valid_roll_number("Enter Roll Number to Update: ")
        name = input("Enter New Name: ")
        dept = input("Enter New Department: ")
        email = input("Enter New Email: ")

        cursor.execute("UPDATE students SET name=%s, department=%s, email=%s WHERE roll_number=%s",
                       (name, dept, email, roll))
        conn.commit()
        if cursor.rowcount:
            print("✅ Student updated successfully.")
        else:
            print("⚠️ Roll number not found.")
    except Error as e:
        print(f"❌ Error: {e}")
    finally:
        cursor.close()
        conn.close()

def delete_student():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        roll = get_valid_roll_number("Enter Roll Number to Delete: ")
        cursor.execute("DELETE FROM students WHERE roll_number = %s", (roll,))
        conn.commit()
        if cursor.rowcount:
            print("✅ Student deleted successfully.")
        else:
            print("⚠️ Roll number not found.")
    except Error as e:
        print(f"❌ Error: {e}")
    finally:
        cursor.close()
        conn.close()

def menu():
    while True:
        print("\n📚 Student Management System")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.")

menu()
