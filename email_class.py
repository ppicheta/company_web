import smtplib, ssl
from email.message import EmailMessage


class Gmail():

    def __init__(self, username, password):
        
        self.username = username
        self.password = password
        self.receiver = self.username
        self.host = 'smtp.gmail.com'
        self.port = 465
    
    def send_email(self, message_subject, message):
        context = ssl.create_default_context()
        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = message_subject
        msg['From'] = self.username
        msg['To'] = self.username

        with smtplib.SMTP_SSL(self.host, self.port, context=context) as server:
            server.login(self.username, self.password)
            server.send_message(msg)
            print('email sent')


# if __name__!='main':
#     message_subject = 'test2'
#     message = """
#     Hi!,
#     how are you"""

#     Gmail('neonrobot9@gmail.com', 'pash ggce smtl hxzi ').send_email(message_subject, message)