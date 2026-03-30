def count_words_and_lines(filename):
    try:
        with open(filename,"r")as f:
            lines = f.readlines()
            word_count = sum(len(line.split()) for line in lines)
            line_count = len(lines)

            return f"Word Count: {word_count}, Line Count: {line_count}"
    except FileNotFoundError:
        return "File not found. Please check the filename and try again."

filename = "file.txt"
result = count_words_and_lines(filename)
print(result)