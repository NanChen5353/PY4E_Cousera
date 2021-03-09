fn=input("Enter a file name:")
handle=open(fn)
counts=dict()
for line in handle:
    if line.startswith("From"):
        if not line.startswith("From:"):
            words=line.split()
            name=words[1]
            counts[name]=counts.get(name,0)+1

bigcount=None
bigname=None
for name, count in counts.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigname=name
print (bigname,bigcount)
