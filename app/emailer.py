import threading
import smtplib
from email.mime.text import MIMEText
from .config import SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, EMAIL_FROM, EMAIL_TO
from .logger import logger

def send_email(patient):
    body = f"New patient record created:\n\nID: {patient.id}\nName: {patient.name}\nAge: {patient.age}\nDisease: {patient.disease}"
    msg = MIMEText(body)
    msg['Subject'] = f"New Patient Created: {patient.name}"
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())

            logger.info("Email sent successfully", extra={"patient_id": patient.id, "to": EMAIL_TO})
    
    except Exception as e:
        logger.error("Failed to send email", extra={"error": str(e), "patient_id": patient.id})

def send_email_background(patient):
    thread = threading.Thread(target=send_email, args=(patient,))
    thread.start()
