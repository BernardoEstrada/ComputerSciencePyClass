r=0
sum=0
continue_string='y'
import random

print('The random numbers are:')
while sum <= 21 and continue_string=='y':
    r=random.randint(0,11)#Generate random number from 0 to 11
    print(r)
    sum=sum+r
    continue_string=input('Do you want to continue? (y/n) ')
print('The sum is', sum)
