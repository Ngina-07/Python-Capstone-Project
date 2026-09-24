import sqlite3

connection = sqlite3.connect("attachment_system.db")
cursor = connection.cursor()

# STUDENTS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    programme TEXT NOT NULL,
    year_of_study INTEGER
)
""")

# ORGANIZATIONS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS organizations (
    organization_id TEXT PRIMARY KEY,
    organization_name TEXT NOT NULL,
    industry TEXT NOT NULL,
    county TEXT NOT NULL,
    contact_person TEXT NOT NULL
)
""")

# ATTACHMENTS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS attachments (
    attachment_id TEXT PRIMARY KEY,
    student_id TEXT NOT NULL,
    organization_id TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    status TEXT NOT NULL,
    progress_percentage INTEGER NOT NULL
)
""")

# 10 DUMMY STUDENTS
students = [
    ("STU001", "Amina Wanjiku", "amina.wanjiku@example.com", "BSc Computer Science", 3),
    ("STU002", "Brian Otieno", "brian.otieno@example.com", "BSc Business Information Technology", 3),
    ("STU003", "Grace Akinyi", "grace.akinyi@example.com", "BSc Computer Science", 4),
    ("STU004", "Kevin Mwangi", "kevin.mwangi@example.com", "BSc Information Technology", 4),
    ("STU005", "Sheila Njeri", "sheila.njeri@example.com", "BSc Information Technology", 3),
    ("STU006", "David Kamau", "david.kamau@example.com", "BSc Computer Science", 3),
    ("STU007", "Faith Wambui", "faith.wambui@example.com", "BSc Information Technology", 4),
    ("STU008", "Eric Kiptoo", "eric.kiptoo@example.com", "BSc Business Information Technology", 3),
    ("STU009", "Lucy Atieno", "lucy.atieno@example.com", "BSc Computer Science", 4),
    ("STU010", "Samuel Mutua", "samuel.mutua@example.com", "BSc Information Technology", 3)
]

cursor.executemany("""
INSERT OR IGNORE INTO students
(student_id, name, email, programme, year_of_study)
VALUES (?, ?, ?, ?, ?)
""", students)

# 3 DUMMY ORGANIZATIONS
organizations = [
    ("ORG001", "Tech Solutions Ltd", "ICT", "Nairobi", "John Kamau"),
    ("ORG002", "Digital Hub Kenya", "Technology", "Kiambu", "Peter Otieno"),
    ("ORG003", "Smart Systems Ltd", "ICT", "Machakos", "Ann Wambui")
]

cursor.executemany("""
INSERT OR IGNORE INTO organizations
(organization_id, organization_name, industry, county, contact_person)
VALUES (?, ?, ?, ?, ?)
""", organizations)

attachments = [
    ("ATT001", "STU001", "ORG001", "2026-09-01", "2026-11-20", "Ongoing", 35),
    ("ATT002", "STU002", "ORG002", "2026-06-01", "2026-08-21", "Completed", 100),
    ("ATT003", "STU003", "ORG003", "2026-09-08", "2026-11-27", "Ongoing", 20),
    ("ATT004", "STU004", "ORG001", "2026-10-05", "2026-12-25", "Not Started", 0),
    ("ATT005", "STU005", "ORG002", "2026-08-03", "2026-10-23", "Ongoing", 50),
    ("ATT006", "STU006", "ORG003", "2026-07-06", "2026-09-25", "Ongoing", 85),
    ("ATT007", "STU007", "ORG001", "2026-04-06", "2026-06-26", "Completed", 100),
    ("ATT008", "STU008", "ORG002", "2026-10-12", "2027-01-02", "Not Started", 0),
    ("ATT009", "STU009", "ORG003", "2026-08-17", "2026-11-06", "Ongoing", 45),
    ("ATT010", "STU010", "ORG001", "2026-05-04", "2026-07-24", "Completed", 100)
]

cursor.executemany("""
INSERT OR IGNORE INTO attachments
(attachment_id, student_id, organization_id, start_date, end_date, status, progress_percentage)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", attachments)

connection.commit()

print("Database setup successful!")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables:", cursor.fetchall())

cursor.execute("SELECT * FROM students")
print("Students:", cursor.fetchall())

connection.close()