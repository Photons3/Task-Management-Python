import pymysql

def setup_database():
    """
    Creates the tasks_db database and the tasks table if they do not exist.
    """
    try:
        connection = pymysql.connect(
            host="localhost",
            user="your_user",
            password="your_password",
            cursorclass=pymysql.cursors.DictCursor
        )
        
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS tasks_db;")
            cursor.execute("USE tasks_db;")
            
            create_table_query = """
            CREATE TABLE IF NOT EXISTS tasks (
                task_id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description TEXT,
                due_date DATE NOT NULL,
                priority ENUM('Low', 'Medium', 'High') NOT NULL,
                status ENUM('Pending', 'In Progress', 'Completed') NOT NULL DEFAULT 'Pending',
                creation_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor.execute(create_table_query)
            
        connection.commit()
        print("✅ Database and table setup complete!")
    except pymysql.MySQLError as e:
        print(f"❌ Error setting up database: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    setup_database()