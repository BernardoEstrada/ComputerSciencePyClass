sum=0
numbers=0
add=1

print('Enter as many numbers as you want. Enter "0" when you are done')
while add > 0:
    add=int(input('Enter a number: '))
    sum=sum+add
    numbers=numbers+1
print('The sum of the',numbers-1,'numbers typed is', sum)
