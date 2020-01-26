num1=int(input('Enter your first number '))
num2=int(input('Enter your second number '))
choice_string=input('What operation would you like to do? (sum/product) ')

if  choice_string=='sum':
    product=num1+num2
elif choice_string=='product':
    product=num1*num2
else:
    print('Error')

print('The', choice_string,'of',num1,'and',num2,'is',product)
