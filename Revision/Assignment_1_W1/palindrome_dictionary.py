import string


def is_palindrome(word):
    # Remove punctuation and convert to lowercase
    cleaned_word = word.translate(str.maketrans("", "", string.punctuation)).lower()
    # Check if the cleaned word is a palindrome
    return cleaned_word == cleaned_word[::-1] and cleaned_word != ""


def palindrome_dictionary(sentences):
    result = {}

    for sentence in sentences:
        # Split the sentence into words
        words = sentence.split()
        # Count palindrome words
        palindrome_words = [word for word in words if is_palindrome(word)]
        result[sentence] = len(palindrome_words)

    return result
