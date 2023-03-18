sen=["a new world record was set","in the holy city of ayodha ","on the eve of diwali on tuesday"," with over three kakh diya or earthen lamps","lit up simultaneously o nhe bank of the river of the sarayu river"]
st=['for','a','of','the','and','to','in','on','with','was']
res=[]
for i in sen:
    row_data=[]
    for j in i.split():
        if j not in st:
            row_data.append(j)
    res.append(row_data)
print(res)    
        
    
print([[j for j in i.split() if j not in st]for i in sen])
