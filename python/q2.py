from q2class import question2
num=int(input("enter a integer"))
s_list=[]
for i in range(num):
    s=input("enter strings")
    s_list.append(s)
sorting=question2(s_list)
print("original list is",s_list)
sorted_list=sorting.sort()
print("sorted list is",sorted_list)