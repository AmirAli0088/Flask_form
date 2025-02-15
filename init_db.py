import sqlite3

conn = sqlite3.connect("your_database.db")  # نام دیتابیس خود را بگذارید
cursor = conn.cursor()

# ساخت جدول users
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL
    )
""")

conn.commit()
conn.close()

print("Database initialized successfully!")
