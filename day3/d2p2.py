mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

res=[]
for i in mat:
    row=[]
    for j in i:
        if j%2!=0:
             row.append(j**2)
        else:
             row.append(j**3)
    res.append(row)        
print(res)


print([j**2 if j%2!=0 else j**3 for i in mat for j in i ])
print([[j**2 if j%2!=0 else j**3 for j in i] for i in mat ])
    
