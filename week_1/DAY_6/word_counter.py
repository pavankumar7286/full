def word_counter(file_name):
    # Open and read file
    with open(file_name, "r") as file:
        content = file.read()

    # Convert all text to lowercase
    content = content.lower()

    # Split into words
    words = content.split()

    # Ask user for the word to count
    w = input("Enter a word to count: ").lower()

    # Count occurrences
    count = words.count(w)

    # Return result
    return f"The word '{w}' appears {count} times in the file."

# Example usage
file_name = "file.txt"
print(word_counter(file_name))
