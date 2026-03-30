import re

text ="pgunjal925@gmail.com"

print("Original text:", text)
pattern = "gmail.com"
match = re.search(pattern,text)
if match:
    print("Email found at index:", match.start())
else:
    print("Email not found") 

replaced_text = re.sub(pattern,"outlook.com",text)
print("Updated text:", replaced_text)