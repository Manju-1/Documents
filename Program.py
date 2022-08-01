from csv import reader
s="Googlebot/2.1;"
with open(r"I:\CSV files\Alpha5-master\files\access-log.txt") as f:
    count1=0
    for line in f:
        if line==" ":
            count1+=1
        print(line)
        if line.strip():
            l=line.split()
            for word in l:
                if word==s:
                    count1+=l.count(word)
    print(count1)

