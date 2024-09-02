import yagmail
import os
import sys
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv('EMAIL_ADDRESS')
# password =  os.getenv('EMAIL_PASSWORD')


def send_email(file_path, recipient_email):
    
    subject = "Processed Images Zip file"
    body = "Please find the processed images attached."
    
    
    # Send the email
    try:
            yag = yagmail.SMTP(sender_email)
            yag.send(
                to=recipient_email,
                subject=subject,
                contents=body,
                attachments=file_path
            )
            print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')

# def zip_folder(folder_path, zip_name):
#     with ZipFile(zip_name, 'w') as zip_file:
#         for foldername, subfolders, filenames in os.walk(folder_path):
#             for filename in filenames:
#                 file_path = os.path.join(foldername, filename)
#                 zip_file.write(file_path, os.path.relpath(file_path, folder_path))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python sendEmail.py <folder_path> <recipient_email>')
        sys.exit(1)

    folder_path = sys.argv[1]
    recipient_email = sys.argv[2]
    
    # zip_name = 'outputFolder3.zip'
    # zip_folder(folder_path, zip_name)
    if os.path.exists(folder_path):
        send_email(folder_path, recipient_email)
    else:
        print(f"Attachement not found: {folder_path}")
    # os.remove(zip_name)  # Clean up the zip file after sending