import sqlite3

connection = sqlite3.connect("attachment_system.db")
cursor = connection.cursor()


# CREATE
# CREATE
def create():
    student_id = input("Student ID: ")
    name = input("Name: ")
    email = input("Email: ")
    programme = input("Programme: ")
    year = int(input("Year of study: "))

    attachment_id = input("Attachment ID: ")
    organization_id = input("Organization ID (e.g. ORG001): ")
    start_date = input("Start date (YYYY-MM-DD): ")
    end_date = input("End date (YYYY-MM-DD): ")
    status = input("Status (Ongoing/Completed/Not Started): ")
    progress = int(input("Progress percentage: "))

    # Add student
    cursor.execute("""
        INSERT INTO students
        (student_id, name, email, programme, year_of_study)
        VALUES (?, ?, ?, ?, ?)
    """, (student_id, name, email, programme, year))

    # Add attachment
    cursor.execute("""
        INSERT INTO attachments
        (attachment_id, student_id, organization_id,
         start_date, end_date, status, progress_percentage)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (attachment_id, student_id, organization_id,
          start_date, end_date, status, progress))

    connection.commit()
    print("Student and attachment added!")


# READ
def read():
    student_id = input("Student ID: ")

    cursor.execute("""
        SELECT students.name, students.email, students.programme,
               students.year_of_study,
               organizations.organization_name, organizations.county,
               attachments.start_date, attachments.end_date,
               attachments.status, attachments.progress_percentage
        FROM students
        LEFT JOIN attachments
        ON students.student_id = attachments.student_id
        LEFT JOIN organizations
        ON attachments.organization_id = organizations.organization_id
        WHERE students.student_id = ?
    """, (student_id,))

    student = cursor.fetchone()

    if student:
        print("\n--- STUDENT DETAILS ---")
        print("Name:", student[0])
        print("Email:", student[1])
        print("Programme:", student[2])
        print("Year:", student[3])

        print("\n--- ATTACHMENT DETAILS ---")
        print("Organization:", student[4])
        print("County:", student[5])
        print("Start Date:", student[6])
        print("End Date:", student[7])
        print("Status:", student[8])
        print("Progress:", student[9], "%")
    else:
        print("Student not found.")


# UPDATE
def update():
    student_id = input("Student ID: ")

    name = input("New name: ")
    email = input("New email: ")
    programme = input("New programme: ")
    year = int(input("New year of study: "))

    attachment_id = input("New attachment ID: ")
    organization_id = input("New organization ID: ")
    start_date = input("New start date (YYYY-MM-DD): ")
    end_date = input("New end date (YYYY-MM-DD): ")
    status = input("New status (Ongoing/Completed/Not Started): ")
    progress = int(input("New progress percentage: "))

    cursor.execute("""
        UPDATE students
        SET name = ?, email = ?, programme = ?, year_of_study = ?
        WHERE student_id = ?
    """, (name, email, programme, year, student_id))

    cursor.execute("""
        UPDATE attachments
        SET attachment_id = ?, organization_id = ?,
            start_date = ?, end_date = ?,
            status = ?, progress_percentage = ?
        WHERE student_id = ?
    """, (attachment_id, organization_id, start_date, end_date,
          status, progress, student_id))

    connection.commit()

    print("Student and attachment updated!")


# DELETE
def delete():
    student_id = input("Student ID: ")

    cursor.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )

    connection.commit()
    print("Student deleted!")


print("\nSTUDENT ATTACHMENT MANAGEMENT SYSTEM")
print("1. Create Student")
print("2. View Student & Attachment")
print("3. Update Student")
print("4. Delete Student")
print("5. Exit")

choice = input("Choose an option: ")

if choice == "1":
    create()
elif choice == "2":
    read()
elif choice == "3":
    update()
elif choice == "4":
    delete()
elif choice == "5":
    print("Goodbye!")
else:
    print("Invalid option")

connection.close()