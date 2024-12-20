def analyze_feedback(feedback, positive_words, negative_words):
    """Analyze feedback for positive and negative words."""
    positive_count = sum(feedback.lower().count(word) for word in positive_words)
    negative_count = sum(feedback.lower().count(word) for word in negative_words)
    return positive_count, negative_count
