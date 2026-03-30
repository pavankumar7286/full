import re

def clean_text(text):
    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

text = "Hello, World! This is a test.   "
cleaned_text = clean_text(text)
print("Original text:", text)
print("Cleaned text:", cleaned_text)