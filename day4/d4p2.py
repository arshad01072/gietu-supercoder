def fun(p,m):
    
    P=p.count('P')
    O=p.count('O')
    E=p.count('E')
    if P>E and P>O:
        s=m['P']
    elif E>O:
        s=m['E']
    else:
        s=m['O']
    return s        
p=[301,'P',302,'P',305,'P',401,'E',665,'E']
m={'P':'pedtradics','O':'orthopedics','E':'ENT'}
s=fun(p,m)
print(s)


                   
        
        


