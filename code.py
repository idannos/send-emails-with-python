import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(message, email, password,send_to_email, subject):
    """
    :param message: the message we want to send
    :param email: the email will send from this email address always
    :param password: the password for the email
    :param send_to_email: the email address we want to send to.
    :param subject: subject of the email message
    :exit: sent or an error message
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587) # may need to change the port
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()
        print "sent email"
    except Exception as e:
        print e

message = "the message itself"
email = "my_email@gmail.com"
password = "my_email_password"
send_to_email = ["ar12@gmail.com", "ts@gmail.com"]  # add emails you want to send to to this list.
subject = "mail's subject"

for i in send_to_email:
    send_email(message, email, password, i, subject)
    #  keep in mind that running this function takes about 2 seconds,
    #  if you want to send to hundreds mails you need try with threads maybe or another methods
