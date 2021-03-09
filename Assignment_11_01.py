fn=input("Enter a file name:")
handle=open(fn)
sum=0
import re
for line in handle:
    line=line.strip()
    stuff=re.findall("[0-9]+",line)
    for item in stuff:
        num=int(item)
        sum=sum+num
print(sum)




    # look for integers using the re.findall(),
     #looking for a regular expression of '[0-9]+' and
     #then converting the extracted strings to integers
     # and summing up the integers.
