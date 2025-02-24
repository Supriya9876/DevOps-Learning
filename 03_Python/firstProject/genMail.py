import smtplib
from email.mime.text import MIMEText

sender_email='supriyabatabyal346@gmail.com'
reciver_email='supriyabatabyal346@gmail.com'
password="ydjv kljg snjp idgf"



def send_email(process_name,pid,cpu_usage):
    subject=f"High CPU Usage Alert: {process_name}"
    body = f"Process {process_name} (PID: {pid}) is consuming {cpu_usage}% CPU."
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = reciver_email
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, reciver_email, msg.as_string())
        print(f"Email alert sent for {process_name} (PID: {pid})")
    except Exception as e:
        print(f"Error sending email: {e}")