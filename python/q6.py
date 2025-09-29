nums=int(input("enter a integer"))
my_list=[]
for i in range(nums):
    n=int(input("enter the integers"))
    my_list.append(n)
hash_table=[[] for _ in range(10)]
for num in my_list:
    rem = num % 10
    if num not in hash_table[rem]:
        hash_table[rem].append(num)
print("hash table is")
for i in range(10):
    print("Bucket index",[i] ,":",hash_table[i])
for i in range(10):
    count=len(hash_table[i])
    for j in range(count-1):
        for k in range(count-1-j):
            if hash_table[i][k]>hash_table[i][k+1]:
                hash_table[i][k],hash_table[i][k+1]=hash_table[i][k+1],hash_table[i][k]
print("the sorted hash table is")
for i in range(10):
    print("Bucket index",[i] ,":",hash_table[i])
add=int(input("enter the number to be added"))
rem=add%10
count1=len(hash_table[rem])
low=0
high=count1-1
while low<=high:
    mid=(low+high)//2
    if add<hash_table[rem][mid]:
        high=mid-1
    else:
        low=mid+1
pos=low
hash_table[rem].insert(pos,add)
count1=count1+1
print("the hash table after addition of the number is:")
for i in range(10):
    print("Bucket index",[i] ,":",hash_table[i])