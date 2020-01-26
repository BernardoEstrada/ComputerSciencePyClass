words=['apple','banana','grape','pineapple','strawberry','watermelon']
tries=0

print('Try to guess all the fruits by typing them.')
print('You have to guess all the',len(words),'words. You have 4 tries')
print('-------------------------------------------------')
print()
while len(words)>0 and tries<4:
    user=input('Enter your choice: ').lower()
    if user in words:
        words.pop(words.index(user))
        print('The word is right, you are missing', len(words),'words')
    else: 
        print('The word is wrong, you are missing', len(words),'words') 
        print('You have',3-tries,'tries left')
        tries+=1
    print()
print()
if len(words)<=0:
    print('You won, you were wrong only',tries,'times')
else:
    print('You lost, you were missing the following',len(words),'words:')
    for i in sorted(words):
        print('-',i.capitalize())
