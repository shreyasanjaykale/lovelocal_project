def shortest_palindrome(s):
    rev_s = s[::-1]
    for i in range(len(s) + 1):
        if s.startswith(rev_s[i:]):
            return rev_s[:i] + s
# Examples
s1 = "aacecaaa"
result1 = shortest_palindrome(s1)
print(result1)
s2 = "abcd"
result2 = shortest_palindrome(s2)
print(result2)
