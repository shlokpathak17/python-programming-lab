i=0
d=0
c=0
l=[31,28,31,30,31,30,31,31,30,31,30,31]

a=int(input("enter the day"))
b=int(input("enter the month"))

for i in l:
    d=d+i
    c=c+1
    if c==b:
        break
out=365-(d+a)
print("total number of days occured",(d+a))
print("number of days left",out)