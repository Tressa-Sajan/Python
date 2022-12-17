
print(input("Enter the name of student:"))
q=int(input("Mark of ENGLISH out of 100 ="))
w=int(input("Mark of COMPUTER out of 100 ="))
e=int(input("Mark of MATHEMATICS out of 100 ="))
r=int(input("Mark of SCIENCE out of 100 ="))
t=int(input("Mark of MALAYALAM out of 100 ="))
totalSum = q+w+e+r+t
perOfStudent = (totalSum/500)*100
print("Total sum of the student:",totalSum)
print("Total percentage of the student:",perOfStudent)
