from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)

# لیست موقت برای ذخیره کاربران (به جای دیتابیس)
users = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['last_name']
        email_address = request.form['last_name']

        # ذخیره در لیست به جای دیتابیس
        users.append({"first_name": first_name, "last_name": last_name, "email_address": email_address,
                      "phone_number": phone_number})

        # ارسال ایمیل
        send_email(first_name, last_name, email_address, phone_number)

        return "اطلاعات شما ثبت شد و ارسال گردید!"

    return render_template('index.html', users=users)


def send_email(first_name, last_name, email_address, phone_number):
    sender_email = os.getenv("amirali.abd.0088@gmail.com")
    receiver_email = "amirali.abd.0088@gmail.com"
    password = os.getenv("hutw xqvc vuwk atk")

    message = MIMEText(f"name: {first_name}\nfamily: {last_name}\nemail: {email_address}\nphone: {phone_number}")
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
    app.run(debug=True)
