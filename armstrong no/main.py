a = int(input("enter a no of your choice"))
temp = a
sum = 0

while temp > 0:
    print(temp)
    rev = temp % 10
    print(rev)
    sum = sum + rev ** 3
    print(sum)
    temp = int(temp/10)

    print(temp)

if sum == a:
    print("armstrong no")

else:
    print(sum)
    print("not armstrong")
