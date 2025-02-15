import smtplib
from email.mime.text import MIMEText

sender_email = "amirali.abd.0088@gmail.com"
receiver_email = "amirali.abd.0088@gmail.com"
password = "hutw xqvc vuwk atkr"

message = MIMEText("این یک تست ایمیل از Flask است.")
message['Subject'] = 'تست ایمیل'
message['From'] = sender_email
message['To'] = receiver_email

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
    print("ایمیل با موفقیت ارسال شد!")
except Exception as e:
    print("خطا در ارسال ایمیل:", e)
