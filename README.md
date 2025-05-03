
# 🎓 Student Management System

This is a command-line based Student Management System written in Python that performs CRUD operations (Create, Read, Update, Delete) using a MySQL database.

## 📦 Features

- Add new student
- View all students
- Search for a student by roll number
- Update student details
- Delete a student record
- Menu-driven interface

## 🛠️ Requirements

- Python 3.x
- MySQL Server
- `mysql-connector-python` module

Install the required module using:

```bash
pip install mysql-connector-python
```

## 🗄️ Database Setup

1. Open MySQL and run the following commands to create the database and table:

```sql
CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    roll_number INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    email VARCHAR(100)
);
```

2. Update the database credentials in the Python file if your MySQL setup differs:

```python
host="localhost"
user="root"
password="root"
database="student_db"
```

## ▶️ Running the Program

Run the script using:

```bash
python student.py
```

## 📸 Sample 

```
📚 Student Management System
1. Add New Student
2. View All Students
3. Search Student by Roll Number
4. Update Student Details
5. Delete Student
6. Exit
```

## 👨‍💻 Author

- Developed by: **M.Chandran**
