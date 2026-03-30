def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for i in s:
        if i in vowels:
            count += 1  

            return f"the number of vowels in the string is {count}"
def is_palindrome(s):
    text = s.replace(" ", "").lower()
    return text == text[::-1]
