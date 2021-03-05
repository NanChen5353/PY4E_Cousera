fh=open("words.txt")
for line in fh:
    ly=line.rstrip()
    ly=line.upper()
    print(ly)
