import os

def read_text_files(data_directory):
    """Reads all text files in the specified directory."""
    feedback_files = {}
    for filename in os.listdir(data_directory):
        if filename.endswith(".txt"):
            with open(os.path.join(data_directory, filename), 'r') as file:
                feedback_files[filename] = file.read()
    return feedback_files
