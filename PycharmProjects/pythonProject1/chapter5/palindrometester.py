import string

def is_palindrome(s):
    s = s.lower()
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.replace(" ", "")
    stack = []
    for c in s:
        stack.append(c)
    for c in s:
        if c != stack.pop():
            return False
    return True
