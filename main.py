choice=True
def main():
    name=input("enter the name of person: ")
    name=name.split()
    leng=len(name)
    last=name[leng-1]
    last=last.capitalize()
    first=""
    for i in range(0,leng-1):
        temp=""
        temp=name[i]
        temp=temp[0].capitalize()+". "
        first+=temp
    name=first+" "+last
    print(name)
    choice=input("False for exit, Anything else will continue the program\n")
while(choice!=False):
    main()
