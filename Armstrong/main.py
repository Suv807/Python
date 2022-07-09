num=int(input("enter a number"))
temp=num
sum=0
while(num>0):
    rev=num%10
    sum=sum+rev**3
    num=num//10
if(temp==sum):
    print("armstrong")
else:
    print("not armstong")