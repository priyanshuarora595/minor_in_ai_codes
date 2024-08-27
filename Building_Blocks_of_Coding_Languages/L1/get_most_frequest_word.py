import re
from collections import Counter


def get_most_frequent_word(lines):
    if not lines:
        return "No valid words found in the list."

    # Join all lines into a single string
    text = " ".join(lines)

    # Convert to lowercase and remove punctuation
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation

    # Split the text into words
    words = text.split()

    if not words:
        return "No valid words found in the list."

    # Count word frequencies
    word_counts = Counter(words)

    # Find the most frequent word
    most_common_word, most_common_count = word_counts.most_common(1)[0]
    return most_common_word
