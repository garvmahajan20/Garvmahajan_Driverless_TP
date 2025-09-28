num = int(input("enter a integer"))
s_list=[]
for i in range(num):
    s=input("enter the strings")
    s_list.append(s)
dict={}
for i in range(num):
    for char in s_list[i].lower():
        if char.isalpha():
            if char in dict:
                dict[char]+=1
            else:
                dict[char]=1
print(dict)



        

