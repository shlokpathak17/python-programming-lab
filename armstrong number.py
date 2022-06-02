a=input("enter the number")
s=0
for i in a:
    s=s+int(i)**3
if(s==int(a)):
    print("the number is armstrong")
else:
    print("number is not armstrong")
