import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import re
from validation import *

# DATABASE CONNECTION
connection = sqlite3.connect("attachment_system.db")
cursor = connection.cursor()

st.set_page_config(page_title="Student Attachment Management System")

st.title("🎓 Student Attachment Management System")

menu = [
    "Dashboard",
    "Add Student",
    "View Students",
    "Search Student",
    "Delete Student"
]

choice = st.sidebar.selectbox("Menu", menu)

# ==========================
# VALIDATION FUNCTIONS
# ==========================

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def validate_student_id(student_id):
    pattern = r'^STU\d{3}$'
    return re.match(pattern, student_id)

# ==========================
# DASHBOARD
# ==========================

if choice == "Dashboard":

    st.header("Dashboard")

    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM attachments WHERE status='Ongoing'"
    )
    ongoing = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM attachments WHERE status='Completed'"
    )
    completed = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM attachments WHERE status='Not Started'"
    )
    not_started = cursor.fetchone()[0]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Students", total_students)
    col2.metric("Ongoing", ongoing)
    col3.metric("Completed", completed)
    col4.metric("Not Started", not_started)

    fig, ax = plt.subplots()

    ax.bar(
        ["Ongoing", "Completed", "Not Started"],
        [ongoing, completed, not_started]
    )

    ax.set_title("Attachment Status")

    st.pyplot(fig)

# ==========================
# ADD STUDENT
# ==========================

elif choice == "Add Student":

    st.header("Add Student")

    student_id = st.text_input("Student ID")
    name = st.text_input("Name")
    email = st.text_input("Email")
    programme = st.text_input("Programme")

    year = st.number_input(
        "Year of Study",
        min_value=1,
        max_value=6
    )

   if st.button("Save Student"):

    if not validate_required(student_id):
        st.error("❌ Student ID is required")

    elif not validate_student_id(student_id):
        st.error("❌ Student ID must follow format STU001")

    elif not validate_required(name):
        st.error("❌ Name cannot be empty")

    elif not validate_email(email):
        st.error("❌ Email must end with @gmail.com")

    else:

        cursor.execute(
            "SELECT student_id FROM students WHERE student_id = ?",
            (student_id,)
        )

        if cursor.fetchone():
            st.error("❌ Student ID already exists")

        else:

            cursor.execute(
                "SELECT email FROM students WHERE email = ?",
                (email,)
            )

            if cursor.fetchone():
                st.error("❌ Email already registered")

            else:

                cursor.execute(
                    """
                    INSERT INTO students
                    (student_id, name, email,
                    programme, year_of_study)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        student_id,
                        name,
                        email,
                        programme,
                        year
                    )
                )

                connection.commit()

                st.success(
                    "✅ Student added successfully"
                ) 

# ==========================
# VIEW STUDENTS
# ==========================

elif choice == "View Students":

    st.header("All Students")

    df = pd.read_sql_query(
        "SELECT * FROM students",
        connection
    )

    st.dataframe(df)

# ==========================
# SEARCH STUDENT
# ==========================

elif choice == "Search Student":

    st.header("Search Student")

    search_id = st.text_input(
        "Enter Student ID"
    )

    if st.button("Search"):

        cursor.execute(
            """
            SELECT * FROM students
            WHERE student_id = ?
            """,
            (search_id,)
        )

        result = cursor.fetchone()

        if result:
            st.write(result)
        else:
            st.warning(
                "Student not found"
            )

# ==========================
# DELETE STUDENT
# ==========================

elif choice == "Delete Student":

    st.header("Delete Student")

    student_id = st.text_input(
        "Student ID"
    )

    if st.button("Delete"):

        cursor.execute(
            """
            DELETE FROM students
            WHERE student_id = ?
            """,
            (student_id,)
        )

        connection.commit()

        st.success(
            "Student deleted successfully"
        )

connection.close()