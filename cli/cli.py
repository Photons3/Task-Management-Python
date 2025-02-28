import sys
import os

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

def format_tasks(tasks):
    """Formats task data in a tabular format."""
    if not tasks:
        print("⚠️ No tasks found.\n")
        return

    table_headers = ["ID", "Title", "Priority", "Status", "Due Date", "Created"]
    table_data = [
        [task.task_id, task.title, task.priority, task.status, task.due_date.strftime("%Y-%m-%d"), task.creation_timestamp.strftime("%Y-%m-%d %H:%M:%S")]
        for task in tasks
    ]

    print("\n📝 Task List")
    print(tabulate(table_data, headers=table_headers, tablefmt="fancy_grid"))

def add_task(task_service):
    """Prompts user for task details and adds a new task."""
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (Low, Medium, High): ")

    try:
        task = task_service.create_task(title, description, due_date, priority)
        print(f"\n✅ Task added successfully! Task ID: {task.task_id}\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")

def list_tasks(task_service):
    """Lists all tasks in a table format."""
    tasks = task_service.list_tasks()
    format_tasks(tasks)

def filter_tasks(task_service):
    """Filters tasks based on user input criteria."""
    filter_by = {}
    status = input("Filter by status (Pending, In Progress, Completed) or leave blank: ")
    priority = input("Filter by priority (Low, Medium, High) or leave blank: ")
    due_date = input("Filter by due date (YYYY-MM-DD) or leave blank: ")

    if status:
        filter_by["status"] = status
    if priority:
        filter_by["priority"] = priority
    if due_date:
        filter_by["due_date"] = due_date

    tasks = task_service.list_tasks(filter_by)
    format_tasks(tasks)

def update_task(task_service):
    """Updates an existing task's details."""
    task_id = input("Enter task ID to update: ")
    title = input("Enter new title: ")
    description = input("Enter new description: ")
    due_date = input("Enter new due date (YYYY-MM-DD): ")
    priority = input("Enter new priority (Low, Medium, High): ")

    try:
        task_service.update_task_details(task_id, title, description, due_date, priority)
        print("\n✅ Task updated successfully!\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")

def mark_task_completed(task_service):
    """Marks a task as completed."""
    task_id = input("Enter task ID to mark as completed: ")

    try:
        task_service.mark_task_completed(task_id)
        print("\n✅ Task marked as completed!\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")

def delete_task(task_service):
    """Deletes a task."""
    task_id = input("Enter task ID to delete: ")

    try:
        task_service.delete_task(task_id)
        print("\n🗑️ Task deleted successfully!\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")

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
