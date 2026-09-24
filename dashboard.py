import sqlite3
import matplotlib.pyplot as plt

connection = sqlite3.connect("attachment_system.db")
cursor = connection.cursor()

print("\n===== STUDENT ATTACHMENT DASHBOARD =====")

cursor.execute("SELECT COUNT(*) FROM students")
total_students = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM attachments WHERE status = 'Ongoing'")
ongoing = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM attachments WHERE status = 'Completed'")
completed = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM attachments WHERE status = 'Not Started'")
not_started = cursor.fetchone()[0]

print("Total Students:", total_students)
print("Ongoing:", ongoing)
print("Completed:", completed)
print("Not Started:", not_started)
plt.bar(
    ["Ongoing", "Completed", "Not Started"],
    [ongoing, completed, not_started]
)

plt.title("Student Attachment Status")
plt.xlabel("Status")
plt.ylabel("Number of Students")

plt.show()

# Progress chart
cursor.execute("""
    SELECT student_id, progress_percentage
    FROM attachments
""")

progress_data = cursor.fetchall()

student_ids = [row[0] for row in progress_data]
progress = [row[1] for row in progress_data]

plt.bar(student_ids, progress)

plt.title("Student Attachment Progress")
plt.xlabel("Student")
plt.ylabel("Progress (%)")
plt.ylim(0, 100)
plt.xticks(rotation=45)

plt.show()

connection.close()