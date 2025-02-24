lang = "Python"
lst = list(lang)
print(type(lst))
print(lst)

lst1 = [i for i in lang]
print(type(lst1))

lst2=[i for i in range(20)]
print(lst2)

lst3=[i*i for i in range(20)]
print(lst3)

lst4=[(i,i*i) for i in range(20)]
print(lst4)
print(type(lst4))

lst5=[i for i in range(20) if i%2!=0]
print(lst5)

# list of list getting converted into list
lst6=[[1,2,3],[4,5,6],[20,43]]
flat_list=[number for row in lst6 for number in row]
print(flat_list)