import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from abc import ABC, abstractmethod
from models.task import Task

class ITaskRepository(ABC):
    """
    Interface for task repository, defining methods for CRUD operations.
    """
    @abstractmethod
    def add_task(self, task: Task):
        """
        Adds a new task to the repository.
        :param task: Task object to be added.
        """
        pass

    @abstractmethod
    def get_task(self, task_id: int):
        """
        Retrieves a task by its ID.
        :param task_id: Unique identifier of the task.
        :return: Task object if found, otherwise None.
        """
        pass

    @abstractmethod
    def list_tasks(self, filter_by: dict = None):
        """
        Lists tasks with optional filtering.
        :param filter_by: Dictionary with filter conditions (status, priority, due date).
        :return: List of Task objects.
        """
        pass

    @abstractmethod
    def update_task_details(self, task_id: int, title: str, description: str, due_date: str, priority: str):
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
    def update_task_status(self, task_id: int, new_status: str):
        """
        Updates the status of a task.
        :param task_id: Unique identifier of the task.
        :param new_status: New status (Pending, In Progress, Completed).
        """
        pass

    @abstractmethod
    def delete_task(self, task_id: int):
        """
        Deletes a task from the repository.
        :param task_id: Unique identifier of the task to be deleted.
        """
        pass