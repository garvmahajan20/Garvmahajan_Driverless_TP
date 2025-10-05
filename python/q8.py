file=open("names.csv","r")
my_list=[]
for line in file:
    line=line.strip()
    parts=line.split(',')
    print("part: ", parts)
    my_list.append([int(parts[0].strip()),parts[1].strip()])
print(my_list)
n=len(my_list)
for i in range(n):
    for j in range(n-i-1):
        if my_list[i][0]>my_list[i+1][0]:
            my_list[i][0],my_list[i+1][0]=my_list[i+1][0],my_list[i][0]
            my_list[i][1],my_list[i+1][1]=my_list[i+1][1],my_list[i][1]
print(my_list)
my_list=my_list[1::2]
print(my_list)
n=len(my_list)
string=""
for i in range(n):
    string+=my_list[i][1]
print(string)
min_diff=300
n1=len(string)
for i in range(n1-1):
    diff=abs(ord(string[i])-ord(string[i+1]))
    if(diff<min_diff):
        min_diff=diff
print(min_diff)