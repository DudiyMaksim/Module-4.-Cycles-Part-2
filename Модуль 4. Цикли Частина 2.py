# task 1
a,b=map(int, input().split())
x=0
x1=0
y=0
y1=0
z=0
z1=0
for i in range(a,b+1):
    if i%2==0:
        x+=i
        x1+=1
    else:
        y+=i
        y1+=1
    if i%9:
        z+=i
        z1+=1
print(f"{x}, {y}, {z}")
print(f"{x/x1}, {y/y1}, {z/z1}")
# task 2
a=int(input())
b=input()
for i in range(a-1):
    print(b)
# task 3
a=True
while a!=7:
    a=int(input())
    if a>0:
        print("Number is positive")
    if a<0:
        print("Number is negative")
    if a==0:
        print("Number is equal zero")
print("Good bye!")
# task 4
max=int(input())
min=max
a=0
sum=max
while a!=7:
    a=int(input())
    if a==7:
        break
    elif a>=max and a>min:
        max=a
        sum+=a
    elif a<=min and a<max:
        min=a
        sum+=a
    else:
        sum+=a
print(sum, max, min)
print("Good bye")