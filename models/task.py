import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import datetime

class Task:
    def __init__(self, title: str, description: str, due_date: str, priority: str,
                 status: str = "Pending", task_id: int = None, creation_timestamp: datetime = None):
        self._task_id = task_id
        self._title = title
        self._description = description
        self._due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self._priority = priority
        self._status = status
        self._creation_timestamp = creation_timestamp if creation_timestamp else datetime.now()

    @property
    def task_id(self):
        return self._task_id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def due_date(self):
        return self._due_date

    @property
    def priority(self):
        return self._priority

    @property
    def status(self):
        return self._status

    @property
    def creation_timestamp(self):
        return self._creation_timestamp