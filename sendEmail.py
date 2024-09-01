import smtplib
import sys
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from zipfile import ZipFile
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv('EMAIL_ADDRESS')
password =  os.getenv('EMAIL_PASSWORD')


def send_email(file_path, recipient_email):
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'Folder Attachment'
    
    body = 'Please find the attached folder.'
    msg.attach(MIMEText(body, 'plain'))
    
    attachment = open(file_path, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename = {file_path}')
    msg.attach(part)
    attachment.close()
    
    
    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')

def zip_folder(folder_path, zip_name):
    with ZipFile(zip_name, 'w') as zip_file:
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zip_file.write(file_path, os.path.relpath(file_path, folder_path))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python sendToEmail.py <folder_path> <recipient_email>')
        sys.exit(1)

    folder_path = sys.argv[1]
    recipient_email = sys.argv[2]
    
    zip_name = 'outputFolder.zip'
    zip_folder(folder_path, zip_name)
    send_email(zip_name, recipient_email)
    os.remove(zip_name)  # Clean up the zip file after sending