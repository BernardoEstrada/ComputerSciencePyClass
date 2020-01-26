def add (a,b):
    answer=a+b
    return answer

def subtract (a,b):
    answer=a-b
    return answer

def multiply (a,b):
    answer=a*b
    return answer

def divide (a,b):
    answer=a/b
    return answer


for i in range(4):
    num1=int(input('Enter your first number '))
    num2=int(input('Enter your second number '))
    choice_string=input('What operation would you like to do? (+)(-)(*)(/) ')
    
 #----------------------------------
    if  choice_string=='+':
        product=add(num1,num2)
    elif choice_string=='-':
        product=subtract(num1,num2)
    elif choice_string=='*':
        product=multiply(num1,num2)
    elif choice_string=='/':
        product=divide(num1,num2)
    else:
        print('Error')
  #---------------------------------
    
    print('The result of',num1,choice_string,num2,'is',product)
    print()
