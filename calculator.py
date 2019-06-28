print("press 1 to add two no")
print("press 2 to sub two no")
print("press 3 to multiply two no")
print("press 4 to divide two no")
print("press 5 to find the  modulus")
print("press 6 for exp")
print("enter 0 to exit")
inp=int(input(""))
while(inp!=0):
    if(inp<7):
        a=int(input("enter value of a "))
        b=int(input("enter value of b"))
    else:
        print("incorrect input")

    if(inp==1):
        sum=lambda a,b:a+b;
        print("answer is :",sum(a,b))
    
    elif(inp==2):
        sub=lambda a,b:a-b
        print("answer is :",sub(a,b))

    elif(inp==3):
        mul=lambda a,b:a*b
        print("answer is :",mul(a,b))

    elif(inp==4):
        div=lambda a,b:a/b
        print("answer is :",mul(a/b))

    elif(inp==5):
        div=lambda a,b:a%b
        print("remainder is :",mul(a%b))

    elif(inp==6):
        exp=lambda a,b:a**b
        print("exponential of " ,a ,"is :",exp(a,b))
    
    inp=int(input(""))
    







