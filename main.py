import csv
import smtplib
import time
from email.message import EmailMessage
import os
from dotenv import load_dotenv

# CONFIGURATION
load_dotenv()
CSV_FILE = "responses.csv" 
GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
EMAIL_COLUMN = "EMAIL"
NAME_COLUMN = "NAME"
STATUS_COLUMN = "Status"  
MESSAGE_TEMPLATE="Default"
SUBJECT_TEMPLATE="Default"

with open("message.txt",mode="r") as file:
    SUBJECT_TEMPLATE = file.readline().strip()  
    MESSAGE_TEMPLATE = file.read()
    
with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    fieldnames = list(reader.fieldnames)   
    # Automatically add a "Status" column to track sent emails if not already there
    if STATUS_COLUMN not in fieldnames:
        fieldnames.append(STATUS_COLUMN)    
    rows = list(reader)

def send_email(smtp_server, recipient_email, recipient_name):
    msg = EmailMessage()
    msg["Subject"] = SUBJECT_TEMPLATE.format(recipient_name=recipient_name)
    msg["From"] = f"JUGS<{GMAIL_USER}>"
    msg["To"] = recipient_email

    msg.set_content(
        MESSAGE_TEMPLATE.format(recipient_name=recipient_name)
    )
    smtp_server.send_message(msg)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD)
    for row in rows:
        recipient_email = str(row.get(EMAIL_COLUMN, "")).strip()
        recipient_name = str(row.get(NAME_COLUMN, "there")).strip()
        status = str(row.get(STATUS_COLUMN, "")).strip()

        # Skip if empty email or already marked as "Sent"
        if not recipient_email or status.lower() == "sent":
            continue

        try:
            print(f"Sending email to {recipient_email}...")
            send_email(smtp, recipient_email, recipient_name)
            # Mark as Sent in memory
            row[STATUS_COLUMN] = "Sent"
            print("Sent successfully!")
            
            with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            time.sleep(1.5)
            
        except Exception as e:
            print(f"Failed to send to {recipient_email}: {e}")

print("All done! Your local CSV file has been updated.")