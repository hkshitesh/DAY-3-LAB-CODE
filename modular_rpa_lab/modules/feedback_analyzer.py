positive_words = ["good", "great", "excellent", "positive", "happy"]
negative_words = ["bad", "poor", "negative", "sad", "angry"]

def analyze_feedback(feedback):
    positive_count = sum(feedback.lower().count(word) for word in positive_words)
    negative_count = sum(feedback.lower().count(word) for word in negative_words)
    return positive_count, negative_count
