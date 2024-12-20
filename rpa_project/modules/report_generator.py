import csv

def generate_csv_report(analysis_results, report_path):
    """Generate a CSV report from the feedback analysis results."""
    with open(report_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["File Name", "Positive Words", "Negative Words"])
        writer.writerows(analysis_results)
