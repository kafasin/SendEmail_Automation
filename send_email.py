import ssl
import smtplib

def send_email(message):
    port = 465 # SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "your_mail_adress"
    receiver_email = "receivers_mail_adress"
    password = "your_password" # account.gmail.com generate an App Password
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print('email sent!')
        except:
            print("could not login or send the mail.")
