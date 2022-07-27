'''
def array(arr,n,d):
    temp=[ ]
    i=0
    while(i<d):
            temp.append(arr[i])
            i+=1
    #i=0
    while(d<n):
         arr[i]=arr[d]
         i+=1
         d+=1
         arr[:]=arr[:]+temp
         return arr
arr=[2,1,3,4,5]
print("Array Is :",end=" ")
print(array(arr,len(arr),3))

def Array(arr1,arr2,n,d):
    temp=[ ]
    i=0
    while i<0:
        temp.append(arr[i])
        i+=1
    while(d<n):
   '''
def SecondLarge(arr,n,k):
    #arr.sort()
    return 


