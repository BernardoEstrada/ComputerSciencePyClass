while True:
    phrase=input('Enter the phrase: ')
    list(phrase)
    shift=int(input('Enter the shift amount: '))
    print('Message: ')
    print('-',end='')
    for i in range(len(phrase)):
        if ord(phrase[i])!=32:
            number=(ord(phrase[i]))+shift
            if number>=123:
                number=number-26
            if number<=96:
                number=number+26
        else:
            number=32
        letter=chr(number)
        print(letter,end='')
    print()
    print('Shift used:', shift)
    print()

#tfdglkvi jtzvetv zj ef dfiv rsflk tfdglkvij kyre rjkifefdp zj rsflk kvcvjtfgvj
#9
