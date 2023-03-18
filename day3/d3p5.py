array=list(map(int,input().split(",")))
num1=sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
print(num1)
l=array[array.index(5):array.index(8)+1]
num2=""
for i in l:
         num2+=str(i)
print(int(num2)+num1)         
