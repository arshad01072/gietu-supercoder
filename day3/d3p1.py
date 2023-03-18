 #lis compresion

#for loop version
res=[]
for i in range(11):
    res.append(i)
print(res)

 #list compresion version

print([i for i in range(11)])
#for loop version odd element

res=[]
for i in range(11):
    if i%2!=0:
        res.append(i)
    else:
        res.append(i*2)
print(res)
print([i if i%2!=0 else i**2 for i in range(11)])
        
