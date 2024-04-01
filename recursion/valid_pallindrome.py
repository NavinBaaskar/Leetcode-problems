def isPallindrome_helper( i, s, n):
    if i >= n / 2:
        return True
    if s[i] != s[n - i - 1]:
        return False
    return isPallindrome_helper(i + 1, s, n)


def isPalindrome( s: str) -> bool:
    i = 0

    s = s.lower()
    l2 = []
    for char in s:
        if char.isalpha() or char.isnumeric():
            l2.append(char)
    s = ''.join(l2)

    n = len(s)
    return isPallindrome_helper(i, s, n)


print(isPalindrome("nivin"))