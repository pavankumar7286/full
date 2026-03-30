with open("file.txt","w") as f:
    f.writelines(["grape\n","banana\n","apple\n","orange"])

with open("file.txt","r")as f:
    content = f.read()
    print(content)