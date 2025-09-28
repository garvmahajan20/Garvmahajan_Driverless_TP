from q3class import question3,question31
num=int(input("enter a integer"))
s_list=[]
for i in range(num):
    s=input("enter strings")
    s_list.append(s)
sorting=question3(s_list)
print("original list is",s_list)
sorted_list=sorting.sort()
print("sorted list is",sorted_list)
word=input("enter the string to be searched")
searching=question31(sorted_list)
existence=searching.binary(word)
if existence==True:
    print("the string exists")
else:
    print("the string does not exist")
