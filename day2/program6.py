n=(12,18,25,25,2,5,18,20,20,21)
def more_than_avg(n):
    l=[]
    avg=sum(n)/len(n)
    for i in n:
        if i>avg:
            l.append(i)
    per=(len(l)/len(n))*100
    return per
    
print(more_than_avg(n))



def count_marks(n):
    l=[]
    for i in range(25):
        l.append(n.count(i))
    return l
print(count_marks(n))



def sort_marks(n):
    l=list(n)
    l.sort()
    return l
print(sort_marks(n))
        
            
