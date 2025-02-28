from db_config import get_db_connection
from repositories.task_manager import TaskManager
from services.task_service import TaskService
from cli.cli import main_menu

def main():
    connection = get_db_connection()
    task_repository = TaskManager(connection)
    task_service = TaskService(task_repository)
    main_menu(task_service)

if __name__ == "__main__":
    main()
