def clean(sentence):
    result = ""
    for i in sentence:
        if i.isalpha():
            result += i.lower()
    return result


def is_palindrome(text):
    """
    No need to take input. Input
    is already given to you as `text`.
    You just need to complete the
    program using this value.
    """
    # Write code here
    text = clean(text)
    return "YES" if text == text[::-1] else "NO"
