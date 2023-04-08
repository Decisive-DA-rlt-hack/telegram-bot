import os
import sqlite3

connection = sqlite3.connect(os.path.join("db", "configs.db"))
cursor = connection.cursor()


def add(telegram_id: int, gender: str):
    cursor.execute(f"INSERT INTO data VALUES({telegram_id}, '{gender}')")
    connection.commit()


def get_user(telegram_id: int):
    config = cursor.execute(
        f"SELECT gender FROM data WHERE telegram_id = {telegram_id}"
    ).fetchall()

    if config:
        return config[0][0]
    return False
