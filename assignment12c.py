alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for h in range(3):
    shift=h
    if h==2:
        shift=-1
    for i in range(len(alphabet)):
        number=(ord(alphabet[i]))+shift
        if number>=123:
            number=number-26
        if number<=96:
            number=number+26
        letter=chr(number)
        print(letter,end='')
    print()
