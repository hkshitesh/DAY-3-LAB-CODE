import os
from modules.file_handler import read_text_files
from modules.feedback_analyzer import analyze_feedback
from modules.report_generator import generate_csv_report
from modules.email_sender import send_email

def main():
    data_directory = './data'
    report_directory = './reports'
    os.makedirs(report_directory, exist_ok=True)

    # Step 1: Read feedback files
    feedbacks = read_text_files(data_directory)

    # Step 2: Analyze feedback
    analysis_results = []
    for file_name, content in feedbacks.items():
        positive, negative = analyze_feedback(content)
        analysis_results.append((file_name, positive, negative))

    # Step 3: Generate report
    report_path = os.path.join(report_directory, 'feedback_report.csv')
    generate_csv_report(analysis_results, report_path)

    # Step 4: Send email
    send_email(
        sender="hkshitesh@gmail.com",
        recipient="hiteshupes@gmail.com",
        subject="Feedback Analysis Report",
        body="Please find the attached feedback analysis report.",
        attachment_path=report_path
    )
    print("Report sent successfully.")

if __name__ == "__main__":
    main()
