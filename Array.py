from array import *
vals=array('i',[5,9,8,4,2])

vals.reverse()
print(vals)
print(vals.buffer_info())
print(vals[0])
for i in range (5):
    print(vals[i])
print('----------')
for e in vals:
    print(e)
i=0
while i<len(vals):
    print(vals[i])
    i+=1
