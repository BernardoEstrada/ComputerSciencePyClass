for i in range(5):
    num_grade=int(input('Enter your grade: '))
    letter_grade='Error'

    if num_grade>=90 and num_grade<=100:
        letter_grade='A'

    elif num_grade>=80 and num_grade<=89:  #use elif instead of all if
        letter_grade='B'

    if num_grade>=70 and num_grade<=79:
        letter_grade='C'

    if num_grade>=60 and num_grade<=69:
        letter_grade='D'
    
    if num_grade>=0 and num_grade<=59:
        letter_grade='F'

    if letter_grade=='A' or letter_grade=='F':
        print('Your grade was',num_grade,', you got an',letter_grade)
    else:
        print('Your grade was',num_grade,', you got a',letter_grade)
