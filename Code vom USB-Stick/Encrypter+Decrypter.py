def encrypt(word, shifting_number):
    
    """Shifts the letters in a word by a given shifting number in the alphabet forwards:
    >>> encrypt("abc", 2)
    'cde'
    >>> encrypt("xyz", 2)
    'zab'
    >>> encrypt("a", 5)
    'f'
    >>> encrypt(1, 5)
    False
    """



    shifting_number = int(shifting_number)
    word = list(word)
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    word_length = len(word)
    i = 0
    u = 0
    o = 0
    for i in range(word_length):
        for u in range(26):
            if word[i] == alphabet[u]:
                word[i] = (u + shifting_number) % 26
    for o in range(word_length):
        for a in range(26):
            if word[o] == alphabet.index(alphabet[a]):
                word[o] = alphabet[a]
    
    return word






def decrypt(word, new_shifting_number):
    
    """Shifts the letters in a word by a given shifting number in the alphabet backwards:
    >>> decrypt("cde", 2)
    abc
    >>> decrypt("zab", 2)
    xyz
    >>> encrypt("f", 5)
    a
    >>> encrypt(1, 5)
    False
    """



    new_shifting_number = int(new_shifting_number)
    word = list(word)
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    word_length = len(word)
    i = 0
    u = 0
    o = 0
    for i in range(word_length):
        for u in range(26):
            if word[i] == alphabet[u]:
                word[i] = (u - new_shifting_number) % 26
    for o in range(word_length):
        for a in range(26):
            if word[o] == alphabet.index(alphabet[a]):
                word[o] = alphabet[a]
    
    return word



                



word = input("Bitte geben Sie ein Wort ein: ")
word = word.lower()
shifting_number = input("Um wie viel sollen die Buchstaben verschoben werden? ")
shifting_number = int(shifting_number)
word = list(word)
word = encrypt(word, shifting_number)
print("".join(word))

decrypted = False
while not decrypted:
    new_shifting_number = input("Bitte geben Sie zum Entschlüsseln die Entschlüsselungszahl ein! ")
    decrypted_word = decrypt(word, new_shifting_number)
    print("".join(decrypted_word))
    new_shifting_number = int(new_shifting_number)
    if shifting_number == new_shifting_number:
        decrypted = True
        
