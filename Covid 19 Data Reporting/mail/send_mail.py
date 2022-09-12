from fileinput import filename
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
    

sender_email_address = 'queryweird@gmail.com'
sender_email_password = 'qu3ryw3!rd123'

def send_mail(receiver_email_address, subject_line, mail_text, attachment=''):
    
    '''Sending Emails to the recipients'''
    
    from_address = sender_email_address
    to_address = receiver_email_address
    
    msg= MIMEMultipart()
    
    # storing the senders email address
    msg['From'] = from_address
    
    # storing the receiver email address
    msg['To'] = to_address
    
    # storing the subject
    msg['Subject'] = subject_line
    
    # string to store body of the mail
    body = mail_text
    
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    
    # open the file to be sent
    if attachment == '':
        pass
    else:
        filename = attachment
        attachment = open(filename, 'rb')
        
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # to change the payload into encoded form
    p.set_payload((attachment).read())
    
    # encode into base 64
    encoders.encode_base64(p)
    
    p.add_header('Content-Disposition', 'attachment; filename = %s' % filename)
    
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
    
    # Create SMTP session
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
    except expression as identifier:
        pass
    
    # start TLS for security
def send_mail():
    print('Step 8: Sending email')