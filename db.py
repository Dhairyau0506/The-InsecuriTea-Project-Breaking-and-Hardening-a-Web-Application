import sqlite3

DB_NAME = "users.db"


def get_db():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        tea_type TEXT,
        sugar TEXT,
        extras TEXT,
        notes TEXT
    )
    """
    )

    conn.commit()
    conn.close()
