nums=[1,2,3,4]
print(nums)
nums.remove(3)
print(nums)

print('==========')

alist=[123,'xyz','zara','abc']
print('A-List :',alist.pop())
print('A-List :',alist.pop(-1))

print('==========')

alist=[123,'xyz','zara','abc']
blist=[456,'souvik','fayez']
alist.extend(blist)
print('Extended-List :',alist)

print('=========')

var = "Don't panic!"
letters = list(var)
print(letters)
print(letters[0])
print(letters[3])
print(letters[-1])
print(letters[-6])

print('=========')

var = "Don't panic!"
letters = list(var)
print(letters[0:10:3])
print(letters[3:])
print(letters[:10])
print(letters[::2])
