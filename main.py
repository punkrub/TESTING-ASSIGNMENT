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

def alternate(s):
    max_len = 0
    unique_chars = list(set(s))
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1, char2 = unique_chars[i], unique_chars[j]
            filtered_s = [c for c in s if c == char1 or c == char2]
            is_valid = True
            for k in range(1, len(filtered_s)):
                if filtered_s[k] == filtered_s[k-1]:
                    is_valid = False
                    break
            if is_valid:
                max_len = max(max_len, len(filtered_s))
    return max_len