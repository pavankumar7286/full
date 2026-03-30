# with open("file.txt","w") as f:
#     f.write("Hello World")
with open("file.txt","r") as f:
    content = f.readlines()

print(content)