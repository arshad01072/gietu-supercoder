def fun(str1):
    if str1[-3:]=="ing":
        return (str1+"ly")
    elif len(str1)<3:
        return (str1)
    else:
        return(str1+"ing")
print(fun("arshad"))
print(fun("w3resource"))
    
