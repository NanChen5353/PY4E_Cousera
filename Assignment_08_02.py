fn=input("Enter the file name:")
fh=open(fn)
count=0
for line in fh:
    line=line.rstrip()
    if line.startswith("From"):
        if not line.startswith("From:"):
            continue
        count=count+1
        email=line.split()
        print(email[1])
print ("There were", count, "lines in the file with From as the first word")
