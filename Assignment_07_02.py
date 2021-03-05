fname=input("Enter the file name:")
fh=open (fname)
count=0
total=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence"):
        colon=line.find(":")
        locate=line[colon+1:]
        number=locate.strip()
        change=float(number)
        count=count+1
        total=total+change
Average=total/count
print("Average spam confidence:", Average)
