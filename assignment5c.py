import random
number=random.randint(1,100)
user=int(input('Enter a number '))
tries=1

#--------------------------------------------------------------
while user!=number:
    if user>number:
        print('The number is lower')
    elif user<number:
        print('The number is higher')
    user=int(input('Enter a number '))
    tries=tries+1
#---------------------------------------------------------------

print('You are right! The mumber is',number,'!')
print('It took you',tries,'tries to guess the number!')
