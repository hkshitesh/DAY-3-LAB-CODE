import logging
from logging.handlers import RotatingFileHandler
import json
import smtplib
from email.mime.text import MIMEText

# Configure logging
def configure_logging(log_file="rpa_lab_logs.log"):
    """Set up logging system with file rotation."""
    logger = logging.getLogger("RPA Logger")
    logger.setLevel(logging.DEBUG)

    # File handler with rotation
    file_handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=5)
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("%(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    return logger

# Initialize logger
logger = configure_logging()

def load_config(file_path):
    """Load configuration file with error handling and logging."""
    try:
        logger.info(f"Attempting to load config file: {file_path}")
        with open(file_path, 'r') as file:
            config = json.load(file)
        logger.info("Config file loaded successfully.")
        return config
    except FileNotFoundError:
        logger.error("Config file not found. Ensure the file is in the correct location.", exc_info=True)
    except json.JSONDecodeError:
        logger.error("Error decoding JSON config file. Check the file format.", exc_info=True)
    except Exception as e:
        logger.critical(f"Unexpected error loading config file: {e}", exc_info=True)

def process_data(file_path):
    """Process data from a file with error handling and logging."""
    try:
        logger.info(f"Reading data from file: {file_path}")
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file.readlines()]
        total = sum(numbers)
        logger.info(f"Successfully processed data. Total sum: {total}")
        return total
    except FileNotFoundError:
        logger.error(f"Data file not found: {file_path}")
    except ValueError:
        logger.error("Data file contains invalid entries. Ensure all lines are numeric.", exc_info=True)
    except Exception as e:
        logger.critical(f"Unexpected error processing data file: {e}", exc_info=True)

def send_email(config, total):
    """Send an email summarizing the task results."""
    try:
        logger.info("Preparing to send email notification.")
        sender = config.get("email_sender")
        recipient = config.get("email_recipient")
        subject = "RPA Task Results"
        body = f"The RPA process completed successfully. Total sum of data: {total}"

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = recipient

        with smtplib.SMTP(config.get("smtp_server"), config.get("smtp_port")) as server:
            server.starttls()
            server.login(config.get("email_login"), config.get("email_password"))
            server.sendmail(sender, recipient, msg.as_string())
        logger.info(f"Email successfully sent to {recipient}")
    except smtplib.SMTPAuthenticationError:
        logger.error("Failed to authenticate email server. Check login credentials.")
    except Exception as e:
        logger.critical(f"Unexpected error sending email: {e}")



def main():
    # Task 1: Load config
    config = load_config("config.json")
    # if not config:
    #     return

    print("Hello, this is next line")

    # Task 2: Process data
    total = process_data("data.txt")
    if total is None:
        return

    # Task 3: Send email
    send_email(config, total)

if __name__ == "__main__":
    main()
