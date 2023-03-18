n=int(input())
def fun_palindrome(n):
    i=0
    while(i==0):
         n+=1
         if str(n)==str(n)[::-1]:
            return n
            
print(fun_palindrome(n))        
