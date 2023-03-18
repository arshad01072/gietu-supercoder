s1=(" I like python")
s2=("Java is a popular langauge")
def fun(s1,s2):
    flag=0
    s1=s1.replace(' ','')
    for i in s1:
        if i in s2:
            print(i,end="")
            flag=1
    if flag==0:
        print("-1")
fun(s1,s2)        
        
       
       
           
        
        
