my_set={1,2,5,7,5,10,8,2,1}
print(my_set)
print("======")

a={1,2,3,4}
b={3,4,5,6}
print(a|b)
print(a&b)
print(a-b)

print('=====')

nearby_people={'DD','Dev','Shweta'}
user_friends=set()
friend=(input('ennter your friend name to see if he is nearby:'))
user_friends.add(friend)
print(user_friends&(nearby_people))
