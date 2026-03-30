with open("file.txt", "r") as file:
    content = file.read()
    print(content)
with open("file_2.txt", "w") as file:
    file.write(content)