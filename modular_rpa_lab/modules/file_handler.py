import os

def read_text_files(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    feedbacks = {}
    for file in files:
        with open(os.path.join(directory, file), 'r') as f:
            feedbacks[file] = f.read()
    return feedbacks
