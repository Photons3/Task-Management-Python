import sys
import os
import re
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tabulate import tabulate
from services.task_service import TaskService

def print_menu():
    """Displays the command-line menu options."""
    print("\n📌 Task Management CLI")
    print("=" * 40)
    print("1. Add a new task")
    print("2. List all tasks")
    print("3. Filter tasks (by status, priority, due date)")
    print("4. Update a task’s details")
    print("5. Mark a task as completed")
    print("6. Delete a task")
    print("7. Exit")
    print("=" * 40)

def validate_date(date_str):
    """Validates the date format (YYYY-MM-DD) and ensures it's not in the past."""
    try:
        input_date = datetime.strptime(date_str, "%Y-%m-%d")
        if input_date < datetime.now():
            print("❌ Due date cannot be in the past. Please enter a future date.")
            return False
        
        """Validates the date format (YYYY-MM-DD)."""
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_priority(priority):
    """Validates priority input."""
    return priority in ["Low", "Medium", "High"]

def validate_status(status):
    """Validates status input."""
    return status in ["Pending", "In Progress", "Completed"]

def validate_task_id(task_id):
    """Validates task ID as an integer."""
    return task_id.isdigit()

def add_task(task_service):
    """Prompts user for task details and adds a new task."""
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    
    while True:
        due_date = input("Enter due date (YYYY-MM-DD): ")
        if validate_date(due_date):
            break
        print("❌ Invalid date format. Please enter in YYYY-MM-DD format.")
    
    while True:
        priority = input("Enter priority (Low, Medium, High): ")
        if validate_priority(priority):
            break
        print("❌ Invalid priority. Choose from Low, Medium, or High.")
    
    try:
        task = task_service.create_task(title, description, due_date, priority)
        print(f"\n✅ Task added successfully! Task ID: {task.task_id}\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")

def update_task(task_service):
    """Updates an existing task's details."""
    while True:
        task_id = input("Enter task ID to update: ")
        if validate_task_id(task_id):
            break
        print("❌ Invalid task ID. Please enter a valid number.")
    
    title = input("Enter new title: ")
    description = input("Enter new description: ")
    
    while True:
        due_date = input("Enter new due date (YYYY-MM-DD): ")
        if validate_date(due_date):
            break
        print("❌ Invalid date format. Please enter in YYYY-MM-DD format.")
    
    while True:
        priority = input("Enter new priority (Low, Medium, High): ")
        if validate_priority(priority):
            break
        print("❌ Invalid priority. Choose from Low, Medium, or High.")
    
    try:
        task_service.update_task_details(task_id, title, description, due_date, priority)
        print("\n✅ Task updated successfully!\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")

def mark_task_completed(task_service):
    """Marks a task as completed."""
    while True:
        task_id = input("Enter task ID to mark as completed: ")
        if validate_task_id(task_id):
            break
        print("❌ Invalid task ID. Please enter a valid number.")
    
    try:
        task_service.mark_task_completed(task_id)
        print("\n✅ Task marked as completed!\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")

def delete_task(task_service):
    """Deletes a task."""
    while True:
        task_id = input("Enter task ID to delete: ")
        if validate_task_id(task_id):
            break
        print("❌ Invalid task ID. Please enter a valid number.")
    
    try:
        task_service.delete_task(task_id)
        print("\n🗑️ Task deleted successfully!\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")

def list_tasks(task_service):
    """Lists all tasks in a tabular format."""
    tasks = task_service.list_tasks()
    if not tasks:
        print("⚠️ No tasks found")
        return
    
    table_headers = ["ID", "Title", "Description", "Priority", "Status", "Due Date", "Created"]
    table_data = [
        [task.task_id, task.title, task.description, task.priority, task.status, task.due_date.strftime("%Y-%m-%d"), task.creation_timestamp.strftime("%Y-%m-%d %H:%M:%S")]
        for task in tasks
    ]
    
    print("📝 Task List")
    print(tabulate(table_data, headers=table_headers, tablefmt="fancy_grid"))

def filter_tasks(task_service):
    """Filters tasks based on user input criteria."""
    filter_by = {}
    status = input("Filter by status (Pending, In Progress, Completed) or leave blank: ")
    priority = input("Filter by priority (Low, Medium, High) or leave blank: ")
    due_date = input("Filter by due date (YYYY-MM-DD) or leave blank: ")
    
    if status and validate_status(status):
        filter_by["status"] = status
    if priority and validate_priority(priority):
        filter_by["priority"] = priority
    if due_date and validate_date(due_date):
        filter_by["due_date"] = due_date
    
    tasks = task_service.list_tasks(filter_by)
    list_tasks(task_service)

def main_menu(task_service: TaskService):
    """Main CLI loop."""
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(task_service)
        elif choice == "2":
            list_tasks(task_service)
        elif choice == "3":
            filter_tasks(task_service)
        elif choice == "4":
            update_task(task_service)
        elif choice == "5":
            mark_task_completed(task_service)
        elif choice == "6":
            delete_task(task_service)
        elif choice == "7":
            print("\n👋 Exiting Task Management CLI. Goodbye!\n")
            sys.exit()
        else:
            print("\n⚠️ Invalid choice. Please try again.\n")
