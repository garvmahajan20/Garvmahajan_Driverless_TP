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





