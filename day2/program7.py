def translate(d,l):
    l1=[]
    for i in l:
        l1.append(d[i])
    return l1    
        
d={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
l=["merry","happy"]
print(translate(d,l))
