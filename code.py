import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(message, email, password,send_to_email, subject):
    """
    :param message: the message we want to send
    :param email: the emails will be sent from this email always,
     so the user wont enter his email
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
    except:
        print "probably not valid email address or not blocked email"

# you can call the function from a loop that run over list of emails
# make sure to sign this for the email you want to send from: https://myaccount.google.com/lesssecureapps
