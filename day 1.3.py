import re
count=0
matcher=re.finditer('ab','abaababa')
for m in matcher:
    count+=1
    print('start:{},end:{},group:{}'.format(m.start(),m.end(),m.group()))

print('the number of occurance:',count)
