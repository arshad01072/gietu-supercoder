n1=int(input())
n2=int(input())
c=0
array=[i for i in range(n1,n2+1)]
print(array)
res=[]
for i in range(len(array)):
    for j in range(i,len(array)):
        res.append(array[i:j+1])
print(res)
for i in res:
    if sum(i)%2!=0:
        c+=1
print(c)        

        
    
       
