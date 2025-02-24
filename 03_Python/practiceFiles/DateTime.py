# import datetime
# print(dir(datetime))

from datetime import datetime
now=datetime.now()
day=now.day
year=now.year
hr=now.hour
mn=now.minute
sc=now.second
print(day," ",year," ",hr," ",mn," ",sc)