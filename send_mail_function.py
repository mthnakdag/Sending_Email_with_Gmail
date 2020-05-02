import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
username = "akdag.metehan231345@gmail.com"
password = "asdzxd12d"


def send_mail(text="Email Body", subject="Hello",
              from_email="Metehan Akdag <akdag.metehan231345@gmail.com>",
              to_emails=None, html=None, img_path=None):
    to_emails = "akdag.metehan231345@gmail.com"
    img_path = "python.jpg"
    assert isinstance(from_email, str)
    assert isinstance(to_emails, str)
    msg = MIMEMultipart("alternative")
    msg["From"] = from_email
    msg["To"] = to_emails
    msg["Subject"] = subject
    txt_part = MIMEText(text, "plain")
    msg.attach(txt_part)
    if img_path is not None:
        image = MIMEImage(open(img_path, "rb").read(), name= os.path.basename(img_path))
        msg.attach(image)
    if html is not None:
        html_part = MIMEText(html, "html")
        msg.attach(html_part)
        
    msg_str = msg.as_string()
    #server = smtplib.SMTP()
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(from_email, to_emails, msg_str)
    #server.quit()

