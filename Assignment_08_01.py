fname=input("Enter file name:")
fh=open(fname)
stuff=list()
for line in fh:
    line=line.rstrip()
    words=line.split()
    for word in words:
        if word not in stuff:
            stuff.append(word)
stuff.sort()
print(stuff)
