import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pymysql
from models.task import Task
from interfaces.Itask_repository import ITaskRepository

class TaskManager(ITaskRepository):
    def __init__(self, connection):
        self.__connection = connection

    def add_task(self, task: Task):
        try:
            with self.__connection.cursor() as cursor:
                sql = """INSERT INTO tasks (title, description, due_date, priority, status, creation_timestamp)
                         VALUES (%s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql, (task.title, task.description, task.due_date.strftime("%Y-%m-%d"), task.priority, task.status, task.creation_timestamp))
                self.__connection.commit()
                task._Task__task_id = cursor.lastrowid
        except pymysql.MySQLError as e:
            print(f"Database error: {e}")
            self.__connection.rollback()
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_task(self, task_id: int):
        try:
            with self.__connection.cursor() as cursor:
                sql = "SELECT * FROM tasks WHERE task_id = %s"
                cursor.execute(sql, (task_id,))
                row = cursor.fetchone()
                if row:
                    return Task(row["title"], row["description"], row["due_date"].strftime("%Y-%m-%d"), row["priority"], row["status"], row["task_id"], row["creation_timestamp"])
        except pymysql.MySQLError as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        return None

    def list_tasks(self, filter_by: dict = None):
        try:
            with self.__connection.cursor() as cursor:
                sql = "SELECT * FROM tasks"
                conditions = []
                values = []
                
                if filter_by:
                    if "status" in filter_by:
                        conditions.append("status = %s")
                        values.append(filter_by["status"])
                    if "priority" in filter_by:
                        conditions.append("priority = %s")
                        values.append(filter_by["priority"])
                    if "due_date" in filter_by:
                        conditions.append("due_date = %s")
                        values.append(filter_by["due_date"])
                
                if conditions:
                    sql += " WHERE " + " AND ".join(conditions)
                
                cursor.execute(sql, tuple(values))
                rows = cursor.fetchall()
                return [Task(row["title"], row["description"], row["due_date"].strftime("%Y-%m-%d"), row["priority"], row["status"], row["task_id"], row["creation_timestamp"]) for row in rows]
        except pymysql.MySQLError as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        return []

    def update_task_status(self, task_id: int, new_status: str):
        try:
            with self.__connection.cursor() as cursor:
                sql = "UPDATE tasks SET status = %s WHERE task_id = %s"
                cursor.execute(sql, (new_status, task_id))
                self.__connection.commit()
        except pymysql.MySQLError as e:
            print(f"Database error: {e}")
            self.__connection.rollback()
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    def update_task_details(self, task_id: int, title: str, description: str, due_date: str, priority: str):
        """
        Updates the details of an existing task.
        :param task_id: Unique identifier of the task.
        :param title: New title of the task.
        :param description: New description of the task.
        :param due_date: New due date of the task in YYYY-MM-DD format.
        :param priority: New priority level of the task.
        """
        try:
            with self.__connection.cursor() as cursor:
                sql = """UPDATE tasks SET title = %s, description = %s, due_date = %s, priority = %s
                         WHERE task_id = %s"""
                cursor.execute(sql, (title, description, due_date, priority, task_id))
                self.__connection.commit()
        except pymysql.MySQLError as e:
            print(f"Database error: {e}")
            self.__connection.rollback()
        except Exception as e:
            print(f"Unexpected error: {e}")
               
    def delete_task(self, task_id: int):
        try:
            with self.__connection.cursor() as cursor:
                sql = "DELETE FROM tasks WHERE task_id = %s"
                cursor.execute(sql, (task_id,))
                self.__connection.commit()
        except pymysql.MySQLError as e:
            print(f"Database error: {e}")
            self.__connection.rollback()
        except Exception as e:
            print(f"Unexpected error: {e}")