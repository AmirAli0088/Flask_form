from flask import Flask, render_template, request
import sqlite3
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)

DB_PATH = "/tmp/database.db"


def init_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        phone_number INTEGER NOT NULL)
                   ''');
    conn.commit()
    conn.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
        conn.commit()
        conn.close()

        send_email(first_name, last_name, phone_number)

        return "اطلاعات شما ثبت شد و ارسال گردید!"

    return render_template('index.html')


def send_email(first_name, last_name, phone_number):
    sender_email = os.getenv("EMAIL_USER")
    receiver_email = "amirali.abd.0088@gmail.com"
    password = os.getenv("EMAIL_PASS")

    message = MIMEText(f"name: {first_name}\nfamily: {last_name}\nphone number: {phone_number}")
    message['Subject'] = 'اطلاعات جدید کاربر'
    message['From'] = sender_email
    message['To'] = receiver_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
    except Exception as e:
        print("خطا در ارسال ایمیل:", e)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
