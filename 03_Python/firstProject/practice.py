import pandas as pd

data={'name':['supriya','vilas','Saheb'],'subject':['Shell','Linux','Python'],'marks':['54','87','13']}
date_list = ['2025-02-01', '2025-02-02', '2025-02-03', '2025-02-04']

df = pd.DataFrame(data)
print("data")
print(df)


for index, row in df.iterrows():
    print(f'{index} ')
    print(f"{row['name']}") #this is iterate only give name

datef=pd.to_datetime(date_list)
print(datef)