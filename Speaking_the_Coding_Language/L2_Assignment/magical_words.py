def magical_words(word_list):
    """
    You are not required to take input.
    Input value is given in the `word_list`
    Use it to complete your program.
    """
    # Write code here
    vowels = "aeiouAEIOU"
    max_vowel_count = 0
    words_with_max_vowels = []
    palindromes = []
    word_counts = {}

    for word in word_list:
        lower_word = word.lower()
        vowel_count = sum(char in vowels for char in lower_word)
        if vowel_count > max_vowel_count:
            max_vowel_count = vowel_count
            words_with_max_vowels = [word]
        elif vowel_count == max_vowel_count:
            words_with_max_vowels.append(word)

        if lower_word == lower_word[::-1]:
            palindromes.append(word)

        word_counts[lower_word] = word_counts.get(lower_word, 0) + 1

    duplicate_words = [word for word, count in word_counts.items() if count > 1]

    print("Highest Vowels:", sorted(words_with_max_vowels)[0])
    if palindromes:
        print("Palindrome:", ", ".join(palindromes))
    else:
        print("Palindrome: None")
    if duplicate_words:
        print("Duplicate Words:", ", ".join(duplicate_words))
    else:
        print("Duplicate Words: None")
