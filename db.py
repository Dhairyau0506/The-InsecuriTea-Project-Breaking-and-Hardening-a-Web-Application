import sqlite3

DB_NAME = "users.db"


def get_db():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_db()
    cursor = conn.cursor()

    # Create table
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

    # ✅ Check if admin exists
    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    admin = cursor.fetchone()

    # ✅ If not, create admin
    if not admin:
        cursor.execute(
            """
            INSERT INTO users (username, password, tea_type, sugar, extras, notes)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            ("admin", "admin123", "Masala Chai", "Normal Sugar", "", "System Admin"),
        )
        print("✅ Admin user created: admin / admin123")

    conn.commit()
    conn.close()