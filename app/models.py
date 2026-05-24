import time
import os
import mysql.connector

class ItemModel:
    def __init__(self):
        self.config = {
            'host': os.getenv('DB_HOST'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASS'),
            'database': os.getenv('DB_NAME')
        }

    def get_all_items(self):
        for attempt in range(5):
            try:
                conn = mysql.connector.connect(**self.config)
                cursor = conn.cursor(dictionary=True)
                cursor.execute('SELECT name FROM items')
                items = cursor.fetchall()
                cursor.close()
                conn.close()
                return items
            except Exception as e:
                print(f"База данных еще не готова (попытка {attempt+1}/5): {e}")
                time.sleep(2)
        
        return []
