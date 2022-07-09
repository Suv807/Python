a=int(input("enter a no"))
b=int(input("enter b no"))
c=int(input("enter c no"))
max=0
if (a>b) and (a>c):
    max=a
if (b>a) and (b>c):
    max=b
if(c>a) and (c>b):
    max=c
print(max,"larger no among 3")