# email_manager
with this code you can automate email to as as many people you want
This Python code automates the sending of emails with a specified subject and content to a list of recipients. 
The script uses the smtplib library to establish a Simple Mail Transfer Protocol (SMTP) server connection, 
and then the MIME library to construct and attach the email's body and any desired attachments.

The send_email() function takes a single argument receiver_mail, which is a string containing the email address of the recipient. 
The function then proceeds to create a message object, add a subject, body text, and attachment (if specified), 
before using the SMTP server to send the email to the recipient's address.

In the main block, a list of recipient emails is defined, and the send_email() function is called for each email address in the list.
