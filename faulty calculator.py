p=int(input("Enter your first number "))
p2=int(input("Enter your second number"))
c=('+,-,/,*')

c=input("Enter your choice : +  -  *  /  ** ")
if p==56 and p2==9 and c=='+':
    print("The result is 66")
elif p==20 and p2==10 and c=='/':
    print("The result is 1.9")
elif p==2 and p2==3 and c=='**':
    print("The result is 92")
elif c=='+':
    print("The result is ",p+p2)
elif c=='-':
    print("The result is ",p-p2)
elif c=='*':
    print("The result is ",p*p2)
elif c=='/':
    print("The result is ",round(p/p2))
elif c=='**':
    print("The result is ",round(p**p2))
