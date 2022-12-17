w=int(input("Enter the 1st number:"))
x=int(input("Enter the 2nd number:"))
y=int(input("Enter the 3rd number:"))
if (w>x) and (w>y):
    num=w
elif(x>w) and (x>y):
    num=x
else:
    num=y
print("The biggest number is ",num)

