import mysql.connector as myconn
from mysql.connector import Error as e

def create_connection(): #Establish a connection to the MySQL database.
    connection = None
    try:
        connection = myconn.connect(host='localhost',user='root',
            database='student_management',
            password='1234')  # Replace with your MySQL credentials
        if connection.is_connected():
            print("Connection to MySQL database was successful.")
            return connection
    except e as Error:
        print(f"Error while connecting to MySQL: {e}")
        return None
    finally:
        if connection and not connection.is_connected():
            print("Failed to connect to MySQL.")

def add_student(connection): #Add a student to the database.
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    mycursor = connection.cursor()
    query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    mycursor.execute(query, (name, age, grade))
    connection.commit()
    print("Student added successfully!")

def display_students(connection): #Display all students in the database.
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM students")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

def update_student(connection): #Update a student's details.
    student_id = int(input("Enter student ID to update: "))
    new_name = input("Enter new name: ")
    new_age = int(input("Enter new age: "))
    new_grade = input("Enter new grade: ")
    mycursor = connection.cursor()
    query = "UPDATE students SET name = %s, age = %s, grade = %s WHERE id = %s"
    mycursor.execute(query, (new_name, new_age, new_grade, student_id))
    connection.commit()
    print("Student updated successfully!")

def delete_student(connection): #Delete a student from the database.
    student_id = int(input("Enter student ID to delete: "))
    mycursor = connection.cursor()
    query = "DELETE FROM students WHERE id = %s"
    mycursor.execute(query, (student_id,))
    connection.commit()
    print("Student deleted successfully!")

def students_by_grade(connection): #Display students filtered by grade.
    grade = input("Enter grade to filter: ")
    mycursor = connection.cursor()
    query = "SELECT * FROM students WHERE grade = %s"
    mycursor.execute(query, (grade,))
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

def average_age(connection): #Calculate and display the average age of students.
    mycursor = connection.cursor()
    query = "SELECT AVG(age) FROM students"
    mycursor.execute(query)
    avg_age = mycursor.fetchone()[0]
    print(f"The average age of students is {avg_age}")

def total_students(connection): #Display the total number of students.
    mycursor = connection.cursor()
    query = "SELECT COUNT(*) FROM students"
    mycursor.execute(query)
    total = mycursor.fetchone()[0]
    print(f"Total number of students: {total}")

def oldest_student(connection): #Display the oldest student.
    mycursor = connection.cursor()
    query = "SELECT * FROM students ORDER BY age DESC LIMIT 1"
    mycursor.execute(query)
    student = mycursor.fetchone()
    print(f"The oldest student is: {student}")

def drop_students_table(connection): #Drop the students table.
    mycursor = connection.cursor()
    mycursor.execute("DROP TABLE IF EXISTS students")
    connection.commit()
    print("Students table dropped.")

def main():
    connection = create_connection()
    if not connection:
        return

    while True:
        print("\nStudent Management System Menu:")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Students by Grade")
        print("6. Average Age of Students")
        print("7. Total Number of Students")
        print("8. Oldest Student")
        print("9. Drop Students Table (CAUTION)")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(connection)
        elif choice == '2':
            display_students(connection)
        elif choice == '3':
            update_student(connection)
        elif choice == '4':
            delete_student(connection)
        elif choice == '5':
            students_by_grade(connection)
        elif choice == '6':
            average_age(connection)
        elif choice == '7':
            total_students(connection)
        elif choice == '8':
            oldest_student(connection)
        elif choice == '9':
            drop_students_table(connection)
        elif choice == '0':
            break
        else:
            print("Invalid choice! Please try again.")

    connection.close()

if __name__ == "__main__":
    main()
