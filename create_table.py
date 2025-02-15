import sqlite3

# اتصال به دیتابیس
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# ایجاد جدول users در صورت عدم وجود
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);
""")

# ذخیره تغییرات
conn.commit()
conn.close()

print("✅ جدول users با موفقیت ایجاد شد!")