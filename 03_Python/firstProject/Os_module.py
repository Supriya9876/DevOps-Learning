import os
print("Current Directory",os.getcwd())
try:
    f=open("D:\Shell/cpuDetails.sh")
    # print(f.read())
    # print(f.readline())
    print(f.readlines())
finally:
    f.close()