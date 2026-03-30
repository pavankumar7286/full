import re

text = "AADAACAADAABAADAA"
pattern = "ADAA"

match = re.search(pattern,text)
if match:
    print("Pattern found at index:", match.start())
else:
    print("Pattern not found")

matches = re.findall(pattern,text)
print("All matches:", matches)

upadted_text = re.sub(pattern,"XXX",text)
print("Updated text:", upadted_text)