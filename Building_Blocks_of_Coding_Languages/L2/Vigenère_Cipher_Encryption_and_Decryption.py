def vigenere_encrypt(plaintext, key):
    def char_to_index(char: str) -> int:
        return ord(char.upper()) - ord("A")

    def index_to_char(index: int) -> str:
        return chr(index + ord("A"))

    # Normalize inputs
    plaintext = plaintext.upper().strip()
    key = key.upper()

    # prepare the key
    key_repeated = list(key)
    ciphertext = []

    for pt_char in plaintext:
        if pt_char.isalpha():  # Encrypt only alphabetic characters
            pt_index = char_to_index(pt_char)
            key_index = char_to_index(key_repeated[0])
            key_repeated.append(key_repeated.pop(0))
            encrypted_index = (pt_index + key_index) % 26
            ciphertext.append(index_to_char(encrypted_index))
        else:
            # Non-alphabetic characters are appended unchanged
            ciphertext.append(pt_char)

    return "".join(ciphertext)
