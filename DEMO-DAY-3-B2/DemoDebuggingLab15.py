import json
import csv
import smtplib
from email.mime.text import MIMEText

def load_config(file_path):
    with open(file_path, 'r') as file:
        print("File read successfully")
        return json.load(file)

def process_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return sum(int(row['value']) for row in reader)

def send_email(config):
    # with open(result_file, 'r') as file:
    #     content = file.read()
    sender = config.get("email_sender")
    recipient = config.get("email_recipient")
    subject = "RPA Task Results"
    msg = MIMEText("demo")
    msg["Subject"] = "RPA Task Results"
    msg["From"] = config["email_sender"]
    msg["To"] = config["email_recipient"]

    with smtplib.SMTP(config.get("smtp_server"), config.get("smtp_port")) as server:
        server.starttls()
        server.login(config.get("email_login"), config.get("email_password"))
        server.sendmail(sender, recipient, msg.as_string())
        print("Email Send Successfully")

def main():
    config = load_config("config.json")
    total = process_data("data.csv")
    print(total)
    with open("result.txt", "w") as file:
        file.write(f"Total: {total}")
    send_email(config)

if __name__ == "__main__":
    main()
