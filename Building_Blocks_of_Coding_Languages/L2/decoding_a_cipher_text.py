def decode_ciphertext(ciphertext, key):
    mapping = {}
    for i in range(26):
        mapping[key[i]] = chr(ord("A") + i)
    resp = ""

    for i in ciphertext:
        if ord("A") <= ord(i) <= ord("Z"):
            resp += mapping[i]
        else:
            resp += i
    print(resp)
