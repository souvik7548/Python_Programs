from array import *
arr=array('i',[])
n=int(input('enter the len of array'))
for i in range(n):
    s=int(input('enter the value of array'))
    arr.append(s)
print(arr)

val=int(input('enter the value for search'))
k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1
print(arr.index(val))
