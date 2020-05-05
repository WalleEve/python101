# Chapter 17 - The email / smtplib
"""
Python provides a couple of modules that we can use to craft emails with.
They are emaila and smptlib
"""


# Email Basic - How to Send and Email with smtplib
"""
The smtplib module is very intuitive to use,

"""
# This is basic code for send a mail:
"""
import smtplib

HOST = "smtp.gmail.com"
SUBJECT = "Test email from Python"
TO = "sayed@live.in"
FROM = "x2xcyrus@gmail.com"
text = "Python 3.4 rules them all!"

BODY = "\r\n".join((
"From: %s" %FROM,
"To: %s" %TO,
"Subject: %s" %SUBJECT,
"",
text
))

#print(BODY)

server = smtplib.SMTP(HOST, 587)
server.ehlo()
server.starttls()
server.login("x2xcyrus@gmail.com", "Sayed08sabeeha")
server.sendmail(FROM, TO, BODY)
server.quit()
"""

# Let's put this code into a function:

import smtplib

def send_mail(host, subject, to_addr, from_addr, body_text):
    """
    Send an email
    """

    BODY = "\r\n".join((
    "From: %s" %from_addr,
    "To: %s" %to_addr,
    "Subject: %s" %subject,
    " ",
    body_text
    ))

    server = smtplib.SMTP(host, 587)
    server.ehlo()
    server.starttls()
    server.login(from_addr, "Sayed08sabeeha")
    server.sendmail(from_addr, [to_addr], BODY)
    server.quit()

if __name__ == "__main__":
    host = "smtp.gmail.com"
    subject = "Test mail from Python"
    to_addr = "kamallochan205@gmail.com"
    from_addr = "x2xcyrus@gmail.com"
    body_text = "Hi this is a test message"
    send_mail(host, subject, to_addr, from_addr, body_text)


"""
Now we'll add a config file to hold the server information and the from address.

"""
