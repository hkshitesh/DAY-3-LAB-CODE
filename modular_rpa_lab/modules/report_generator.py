import pandas as pd
def generate_csv_report(data, output_path):
    df = pd.DataFrame(data, columns=["File Name", "Positive Words", "Negative Words"])
    df.to_csv(output_path, index=False)
