with open("text_file_0.txt") as fo :
    data = fo.read()
    for line in data:
        line.rstrip()

print data

fo.close()
