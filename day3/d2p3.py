mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
res=[]
for i in list_b:
    res.append((i,mylist.index(i)))
    
print(res)


print([(i,mylist.index(i))for i in list_b])
dict1={}
for i in list_b:
    dict1[i]=mylist.index(i)
print(dict1)
print({i:mylist.index(i)for i in list_b})

