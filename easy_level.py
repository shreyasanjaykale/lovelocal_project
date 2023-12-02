def length_last_word(s):
    # Splitting the string into words
    words = s.split()
    
    # Check if there are any words or not
    if len(words) == 0:
        return 0
    
    # Return the length of the last word
    return len(words[-1])

# Example
s = "Hello World"
result = length_last_word(s)
print(result)
