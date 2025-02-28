import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from abc import ABC, abstractmethod

class ITaskService(ABC):
    """
    Interface for task service, defining methods for managing tasks.
    """
    
    @abstractmethod
    def create_task(self, title: str, description: str, due_date: str, priority: str):
        """
        Creates a new task and saves it to the repository.
        :param title: The title of the task.
        :param description: The description of the task.
        :param due_date: The due date of the task in YYYY-MM-DD format.
        :param priority: The priority level of the task (Low, Medium, High).
        """
        pass

    @abstractmethod
    def get_task(self, task_id: str):
        """
        Retrieves a task by its ID.
        :param task_id: Unique identifier of the task.
        :return: Task object if found, otherwise None.
        """
        pass

    @abstractmethod
    def list_tasks(self, filter_by: dict = None):
        """
        Lists all tasks with optional filtering by status, priority, or due date.
        :param filter_by: Dictionary containing filter conditions.
        :return: List of Task objects.
        """
        pass

    @abstractmethod
    def update_task_details(self, task_id: str, title: str, description: str, due_date: str, priority: str):
        """
        Updates the details of an existing task.
        :param task_id: Unique identifier of the task.
        :param title: New title of the task.
        :param description: New description of the task.
        :param due_date: New due date of the task.
        :param priority: New priority level of the task.
        """
        pass

    @abstractmethod
    def mark_task_completed(self, task_id: str):
        """
        Marks a task as completed.
        :param task_id: Unique identifier of the task.
        """
        pass

    @abstractmethod
    def delete_task(self, task_id: str):
        """
        Deletes a task from the repository.
        :param task_id: Unique identifier of the task to be deleted.
        """
        pass