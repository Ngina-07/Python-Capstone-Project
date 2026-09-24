# Student Attachment Management System

## Project Description
The Student Attachment Management system is a python-based application designed to help manage and monitor student attachment records.
The system stores student information, organisation details, attachment dates, attachment status and progress.
It also provides a dashboard with charts to make the attachment ingormation easier to understand and monitor.

## Objectives
- Manage student attachment records.
- Store organization and placement details.
- Track attachment dates, status, and progress.
- Perform CRUD operations on student records.
- Provide a dashboard for easy monitoring.

## 🛠️ Technologies Used

- **Python** – Used to develop the application logic and implement the CRUD operations for managing student records.

- **SQLite** – Used as the database to store student, organization, and attachment information.

- **SQL** – Used to create tables, insert records, retrieve information, update records, and delete records from the SQLite database.

- **Matplotlib** – Used to create the dashboard charts for visualizing attachment status and student progress.

- **VS Code** – Used as the development environment for writing, testing, and running the Python code.

  ##  System Features

### 1. Create
Allows users to add new student and attachment records.

### 2. Read
Allows users to view student, organization, and attachment information.

### 3. Update
Allows users to update student and attachment information.

### 4. Delete
Allows users to remove student records.

### 5. Dashboard
Provides a summary of attachment information using charts, including attachment status and student progress.

## 🗄️ Database

The system uses an SQLite database to store and manage the project data.

The main tables are:

- **Students** – Stores student identification, contact, programme, and year of study.
- **Organizations** – Stores organization names, industries, counties, and contact persons.
- **Attachments** – Stores attachment placement details, dates, status, and progress percentage.

The tables are connected using student and organization identifiers to allow related information to be retrieved together.

## 📊 Dashboard & Data Visualization

The system includes a dashboard that provides a summary of student attachment information.

The dashboard displays:

- Total number of students
- Number of ongoing attachments
- Number of completed attachments
- Number of not started attachments
- Student attachment progress

**Matplotlib** is used to create visual charts that make the attachment data easier to understand and monitor.

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Ngina-07/Python-Capstone-Project.git
### 2. Open the project folder

```bash
cd Python-Capstone-Project
```
### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```
### 4. Run the application

```bash
python app.py
```
### 5. Run the dashboard

```bash
python dashboard.py
```
## 📁 Project Structure

```text
Python-Capstone-Project/
│
├── app.py
├── database.py
├── dashboard.py
├── attachment_system.db
├── requirements.txt
├── project_template.md
├── README.md
└── .gitignore
```
## 💡 Project Benefits

- Organizes student attachment information in one system.
- Makes it easier to monitor attachment status and progress.
- Reduces the difficulty of managing records manually.
- Makes student and organization information easier to access.
- Provides visual summaries through the dashboard.


