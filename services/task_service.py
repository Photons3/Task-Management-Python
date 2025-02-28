import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.task import Task
from repositories.task_manager import TaskManager

class TaskService:
    """
    Service class for managing tasks.
    Handles business logic and interacts with the task repository.
    """
    
    def __init__(self, task_repository: TaskManager):
        """
        Initializes TaskService with a TaskRepository instance.
        :param task_repository: An instance of TaskRepository for database operations.
        """
        self.__task_repository = task_repository

    def create_task(self, title: str, description: str, due_date: str, priority: str):
        """
        Creates a new task and adds it to the repository.
        :param title: Title of the task.
        :param description: Description of the task.
        :param due_date: Due date of the task in YYYY-MM-DD format.
        :param priority: Priority level of the task (Low, Medium, High).
        :return: The created Task object.
        """
        task = Task(title, description, due_date, priority)
        self.__task_repository.add_task(task)
        return task

    def get_task(self, task_id: int):
        """
        Retrieves a task by its ID.
        :param task_id: Unique identifier of the task.
        :return: Task object if found, otherwise None.
        """
        return self.__task_repository.get_task(task_id)

    def list_tasks(self, filter_by: dict = None):
        """
        Lists all tasks with optional filtering by status, priority, or due date.
        :param filter_by: Dictionary containing filter conditions.
        :return: List of Task objects.
        """
        return self.__task_repository.list_tasks(filter_by)

    def update_task_details(self, task_id: int, title: str, description: str, due_date: str, priority: str):
        """
        Updates the details of an existing task.
        :param task_id: Unique identifier of the task.
        :param title: New title of the task.
        :param description: New description of the task.
        :param due_date: New due date of the task.
        :param priority: New priority level of the task.
        """
        self.__task_repository.update_task_details(task_id, title, description, due_date, priority)

    def mark_task_completed(self, task_id: int):
        """
        Marks a task as completed by updating its status.
        :param task_id: Unique identifier of the task.
        """
        self.__task_repository.update_task_status(task_id, "Completed")

    def delete_task(self, task_id: int):
        """
        Deletes a task from the repository.
        :param task_id: Unique identifier of the task to be deleted.
        """
        self.__task_repository.delete_task(task_id)
