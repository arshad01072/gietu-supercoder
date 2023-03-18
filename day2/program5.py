def fun(n):
    n=str(n)
    d=str(n*2)
    c=0
    for i in n:
        if i in d:
            c+=1
    if c==len(n):
        return True
    else:
        return False
print(fun(125874))    


def fun1(n):
    n=(n)
    d=(n*2)
    l1=[n]
    l2=[d]
    l1=l1.sort()
    l2=l2.sort()
    if l1==l2:
        return True
    else:
        return False
print(fun1(125874))    
        
            
          
            
            
