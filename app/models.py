import os
import mysql.connector

class ItemModel:
    def __init__(self):
        self.config = {
            'host': os.getenv('DB_HOST', 'db'),
            'user': os.getenv('DB_USER', 'db_user'),
            'password': os.getenv('DB_PASS', 'db_password'),
            'database': os.getenv('DB_NAME', 'web_db'),
            'charset': 'utf8mb4'
        }

    def get_connect(self):
        return mysql.connector.connect(**self.config)

    def get_all_items(self):
        try:
            conn = self.get_connect()
            cursor = conn.cursor(dictionary=True)
            cursor.execute('SELECT name FROM items')
            items = cursor.fetchall()
            cursor.close()
            conn.close()
            return items
        except Exception as e:
            print(f"Error: {e}")
            return []
