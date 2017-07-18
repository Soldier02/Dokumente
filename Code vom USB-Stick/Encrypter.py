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
    alphabet = list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
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











#if __name__ == "__main__":
   # import doctest
   # doctest.testmod()
