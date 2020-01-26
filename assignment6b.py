def math(a,b):
    result=a*b
    return result
#---------------functions are usually at the top of the program
c=int(input('Type in the number of atoms of Carbon '))
h=int(input('Type in the number of atoms of Hydrogen '))
n=int(input('Type in the number of atoms of Nitrogen '))
o=int(input('Type in the number of atoms of Oxygen '))
s=int(input('Type in the number of atoms of Sulfur '))



weight=math(12.011,c)+math(1.00794,h)+math(14.00674,n)+math(15.9994,o)+math(32.066,s)

print('The molecular weight of that amino acid is',weight)
