num=int(input("please enter a number"))
if num>10:
    print("num is greater than 10")
elif num<5:
    print("num is smaller than 5")
else:
    print("num is out of the range")

# Write the students to grade them based on score

# i=1
# while i<10:
#     print(num*i)
#     i+=1
# else:
#     print("this is the table")


# Check the number is prime is not

def isP(num):
    for i in range(2,num//2):
        if num%i==0:
            print("Not prime")
            return 
    return "prime"

isP(10)

# Return the first repeating number in list
def fRN(nums):
    nrn= set()
    for i in nums:
        if(i in nrn):
            return i
        nrn.add(i)
    return -1

nums=[2,3,1,5,7,8,3]
print(fRN(nums))