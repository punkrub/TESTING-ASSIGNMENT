def funnyString(s):
    r = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
            return "Not Funny"
    return "Funny"

def alternatingCharacters(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            deletions += 1
    return deletions

def caesarCipher(s, k):
    k = k % 26
    result = []
    for char in s:
        if char.islower():
            result.append(chr((ord(char) - 97 + k) % 26 + 97))
        elif char.isupper():
            result.append(chr((ord(char) - 65 + k) % 26 + 65))
        else:
            result.append(char)
    return "".join(result)