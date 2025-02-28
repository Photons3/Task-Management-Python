# Task Management CLI Application

## 📌 Overview

This is a **Task Management Console Application** built with **Python** and **MySQL**, using the `pymysql` library for database interactions.

## 🚀 Features

- Add, list, update, mark complete, and delete tasks.
- Filter tasks by **priority, status, or due date**.
- Command-line user interface (CLI) with **tabulated output**.
- Database interaction with **MySQL**.

---

## 📂 Project Structure

```
project/
│── models/
│   ├── task.py
│── repositories/
│   ├── task_repository.py
│── services/
│   ├── task_service.py
│── cli/
│   ├── cli.py
│── main.py
│── db_config.py
│── README.md
```

---

## 🛠️ Setup Instructions

### 1️⃣ Install Dependencies

Make sure you have **Python 3.x** installed, then run:

```sh
pip install pymysql tabulate
```

### 2️⃣ Configure MySQL Database

Create a MySQL database and table by running:
```sql
CREATE DATABASE tasks_db;

USE tasks_db;

CREATE TABLE tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    priority ENUM('Low', 'Medium', 'High') NOT NULL,
    status ENUM('Pending', 'In Progress', 'Completed') NOT NULL DEFAULT 'Pending',
    creation_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 3️⃣ Update Database Configuration

Modify `db_config.py` to match your **MySQL credentials**:
```python
import pymysql

def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="your_user",
        password="your_password",
        database="tasks_db",
        cursorclass=pymysql.cursors.DictCursor
    )
```

### 4️⃣ Run the Application

```sh
python main.py
```

---

## 🎮 CLI Commands

| Command | Description                               |
| ------- | ----------------------------------------- |
| `1`     | Add a new task                            |
| `2`     | List all tasks                            |
| `3`     | Filter tasks (status, priority, due date) |
| `4`     | Update a task                             |
| `5`     | Mark task as completed                    |
| `6`     | Delete a task                             |
| `7`     | Exit                                      |

---

## ✅ Example Usage

```
📌 Task Management CLI
========================================
1. Add a new task
2. List all tasks
3. Filter tasks (by status, priority, due date)
4. Update a task’s details
5. Mark a task as completed
6. Delete a task
7. Exit
========================================
Enter your choice: 1
Enter task title: Finish Report
Enter task description: Complete the annual report
Enter due date (YYYY-MM-DD): 2025-03-10
Enter priority (Low, Medium, High): High
✅ Task added successfully! Task ID: 1
```

---

## 🛠️ Troubleshooting

\*\*Error: \*\*\`\`\
➡ Solution: Run `pip install pymysql`

\*\*Error: \*\*\`\`\
➡ Solution: Check your MySQL username/password in `db_config.py`

---

## 📜 License

This project is open-source and available under the **MIT License**.

