# Write a code to grade the student based on their score
phy=int(input("Enter the score of the physics: "))
math=int(input("Enter the score of the math: "))
chem=int(input("Enter the score of the chem: "))
total=(phy+math+chem)
avg=total//3
print("Average score is:",avg)
if(avg>=80):
    print("Excellent Result")
elif(avg<80 and avg>=60):
    print("Good Result")
elif(avg<60 and avg>=35):
    print("Need to do better")
else:
    print("Fail")