n=int(input("enter the number of students"))
c=int(input("enter the number of candies"))
a=[]
i=1
sum=0
print("enter the array of candy")
while(i<n+1):
    a.append(int(input()))
    i=i+1
print(a)
for i in a:
    sum=sum+i
if(sum==c):
    print("all students are setisfied")
else:
    print("students not setisfied")