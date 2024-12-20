import os
import smtplib
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup

def read_file(file_path):
    """Read and process data from a file with error handling."""
    try:
        with open(file_path, 'r') as file:
            data = file.readlines()
            numbers = [int(line.strip()) for line in data]
            print(f"Sum of numbers: {sum(numbers)}")
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the file path.")
    except ValueError:
        print("Error: File contains non-numeric data. Please correct the file content.")
    except Exception as e:
        print(f"Unexpected error while reading the file: {e}")


def send_email(sender, recipient, subject, body, smtp_server, smtp_port, login, password):
    """Send an email with error handling."""
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = recipient

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(login, password)
            server.sendmail(sender, recipient, msg.as_string())
        print("Email sent successfully.")
    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Check your email credentials.")
    except smtplib.SMTPConnectError:
        print("Error: Unable to connect to the email server.")
    except Exception as e:
        print(f"Unexpected error while sending email: {e}")

def scrape_website(url):
    """Scrape data from a website with error handling."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        soup = BeautifulSoup(response.content, "html.parser")
        # Assuming we're extracting product prices as an example
        prices = soup.find_all("span")
        if not prices:
            raise ValueError("Error: Unable to find the price elements on the webpage.")
        for price in prices:
            print(price.get_text())
    except requests.exceptions.RequestException as e:
        print(f"Error: Network issue or invalid URL - {e}")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Unexpected error during web scraping: {e}")




def main():
    # Task 1: File reading
    file_path = "data.txt"
    read_file(file_path)
    # Task 2: Sending an email
    sender_email = "hkshitesh@gmail.com"
    recipient_email = "hiteshupes@gmail.com"
    subject = "Test Email: By Hitesh"
    body = "This is a test email from the RPA script."
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_login = "hkshitesh@gmail.com"
    email_password = "sljj ysjc ooee tpzx"
    send_email(sender_email, recipient_email, subject, body, smtp_server, smtp_port, email_login, email_password)
    print("Next Line code")

    # Task 3: Web scraping
    url = "https://example.com"
    scrape_website(url)


if __name__ == "__main__":
    main()
