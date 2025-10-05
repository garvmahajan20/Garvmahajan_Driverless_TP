def sort(my_coord,x0,y0):
    n=len(my_coord)
    for i in range(n):
            for j in range(i+1,n):
                x_dist_i=x0-my_coord[i][0]
                y_dist_i=y0-my_coord[i][1]
                dist_i=(((x_dist_i**2)+(y_dist_i**2))**0.5)

                x_dist_j=x0-my_coord[j][0]
                y_dist_j=y0-my_coord[j][1]
                dist_j=(((x_dist_j**2)+(y_dist_j**2))**0.5) 
                if dist_i>dist_j:
                     my_coord[i],my_coord[j]=my_coord[j],my_coord[i]
                                 
    
    return my_coord

n=int(input("enter the number of coordinates you want to enter"))
my_coord=[]
for _ in range(1,n+1):
    x=int(input("x coordinates"))
    y=int(input("y coordinates"))
    my_coord.append([x,y])
print(my_coord)
print("enter reference coordinates")
x0=int(input("enter the reference x coordinate"))
y0=int(input("enter the reference y coordinate"))
sorting=sort(my_coord,x0,y0)
print("the sorted distances are")
print(sorting)


