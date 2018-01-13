name=input("enter the name of person")
name=name.split()
leng=len(name)
lastName=name[leng-1]
first=""
for i in range(0,leng-1,-1):
    temp=name[i]
    print(temp)
print
