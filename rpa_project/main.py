import os
from modules.file_handler import read_text_files
from modules.feedback_analyzer import analyze_feedback
from modules.report_generator import generate_csv_report
from modules.email_sender import send_email
from read_config import load_config

def main():
    # Load the configuration parameters
    config = load_config()

    # Read the directories from config
    data_directory = config['directories']['data_directory']
    report_directory = config['directories']['report_directory']
    os.makedirs(report_directory, exist_ok=True)

    # Read the keywords from config
    positive_words = config['keywords']['positive_words']
    negative_words = config['keywords']['negative_words']

    # Read the email credentials from config
    email_config = config['email']
    sender_email = email_config['sender_email']
    recipient_email = email_config['recipient_email']
    smtp_server = email_config['smtp_server']
    smtp_port = email_config['smtp_port']
    smtp_username = email_config['smtp_username']
    smtp_password = email_config['smtp_password']

    # Step 1: Read feedback files
    feedbacks = read_text_files(data_directory)

    # Step 2: Analyze feedback
    analysis_results = []
    for file_name, content in feedbacks.items():
        positive, negative = analyze_feedback(content, positive_words, negative_words)
        analysis_results.append((file_name, positive, negative))

    # Step 3: Generate report
    report_path = os.path.join(report_directory, 'feedback_report.csv')
    generate_csv_report(analysis_results, report_path)

    # Step 4: Send email with the report
    send_email(
        sender=sender_email,
        recipient=recipient_email,
        subject="Feedback Analysis Report",
        body="Please find the attached feedback analysis report.",
        attachment_path=report_path,
        smtp_server=smtp_server,
        smtp_port=smtp_port,
        smtp_username=smtp_username,
        smtp_password=smtp_password
    )
    print("Report sent successfully.")

if __name__ == "__main__":
    main()
