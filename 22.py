q = int(input("Enter the number:"))
Rev = 0
while (q>0):
    R = q % 10
    Rev = (Rev*10)+R
    q = q//10
print("Reverse of the number:",Rev)
