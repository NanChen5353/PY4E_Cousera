fn=input("Enter a file name:")
handle=open(fn)

counts=dict()
for line in handle:
    if line.startswith("From"):
        if not line.startswith("From:"):
            words=line.split()
            time=words[5]
            t=time.split(":")
            hour=t[0]
            counts[hour]=counts.get(hour,0)+1
#not fully understand the counts here,get here
#how to count items, how to write it
#counts only the name of the dictionary when being given an example
#before use it, need to create a dictionary

#how can i put them in the list
#create one to initiate.

#how to change the dictionary into tuples
#use items

tup=sorted(counts.items())
for hour,count in tup:
    print(hour,count)
