import re

def find_email(fp):
    with open(fp,'r') as file:
        content=file.read()
    email=re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',content)
    return email

fp=input("Enter the path of the emailcontains file: ")
l=find_email(fp)
for li in l:
    print(li)