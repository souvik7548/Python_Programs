def twosum(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if target-num[i]==num[j]:
                return [i,j]
num=[2,7,9,11,15]
target=9
print(twosum(num,target))
