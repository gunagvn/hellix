
with open("hi.txt", 'r') as file :
    lines = file.readlines
    for lines in file:
        if "python" in lines:
            print(lines)
