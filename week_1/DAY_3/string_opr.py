import string_op as sp
s = input("enter a string : ")

print(f"the reverse of the string is {sp.reverse_string(s)}")

print(f"{sp.count_vowels(s)}")

if sp.is_palindrome(s):
    print("the string is a palindrome")
else:
    print("the string is not a palindrome")


