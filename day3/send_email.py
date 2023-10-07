import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username = 'your email'
password = 'pass word'


def send_mail(text = "Email Body", subject = " Email Subject", from_email = "JPC mail", 
              to_emails = ['jpc.coder@gmail.com'], html = None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart("alternative")
    msg['From'] = from_email
    msg['To'] = ",".join(to_emails)
    msg["Subject"] = subject
    msg["Reply-To"] = 'no-reply'
    txt_part = MIMEText(text, "plain")
    msg.attach(txt_part)

    if html != None:
        html_part = MIMEText(html, "html")
        msg.attach(html_part)

    msg_str = msg.as_string()


    # Login to stmp server
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    # server.starttls()
    server.login(username, password)


    
    # send mail
    try:
        server.sendmail(from_email, to_emails, msg= msg_str)
        message = "email sent"
    except:
        message = "email Not sent"
    
    return message

    # to stop server
    server.quit()