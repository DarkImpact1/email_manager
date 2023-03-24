'''
here is the sample of automation of email which I can further modify in order to gain lots of click and traffic in your site
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(receiver_mail):
    # Sender and receiver information
    sender_email = "email provided by you, ( or my email if needed)"
    sender_password = "pass word of the mail"
    receiver_mail

    # Create a message object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_mail
    message["Subject"] = "A subject which will make user to open the mail......."

    # Add body text to the email
    body = '''
    here will be your site's content and links'''
    message.attach(MIMEText(body, "plain"))

    # Attach the file to the email
    filename = document
    with open(filename, "rb") as f:
        attachment = MIMEApplication(f.read(), _subtype="txt")
        attachment.add_header("Content-Disposition", "attachment", filename=filename)
        message.attach(attachment)

    try:
        # Create the SMTP server and login
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email and close the connection
        text = message.as_string()
        server.sendmail(sender_email, receiver_mail, text)

    except Exception as e:
        print(e)

    finally:
        server.quit()

if __name__ == "__main__":
    # here I can automate the email which can be sent within a click 
    user =["client1","client2","..............clientn"]
    for client in user:
        send_email(client)