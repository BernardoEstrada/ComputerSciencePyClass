import random
beats='error'
opponentN=random.randint(1,5)
inputP='error'
opponent='error'
repeat='y'
wins=0
looses=0
ties=0


def rules ():
    print('Welcome to Rock, Paper, scissors, lizard, spock')
    print()
    print('''The rules are simple,

    Scissors - cut -------- Paper
    Paper ---- covers ----- Rock
    Rock ----- crushes ---- Lizard
    Lizard --- poisons ---- Spock
    Spock ---- smashes ---- Scissors
    Scissors - decapitate - lizard
    Lizard --- eats ------- paper
    Paper ---- disproves -- Spock
    Spock ---- vaporizes -- Rock
    Rock ----- crushes ---- Scissors''')    
#------------------ end of rules---------------
def compare(computer,user):
    if computer==user:
       return 'tied','ties'
    
    elif user=='scissors':
        if computer=='paper':
            return 'won','cut'
        elif computer=='rock':
            return 'lost','crushes'
        elif computer=='lizard':
            return 'won','decapitate'
        elif computer=='spock':
            return 'lost','smashes'
        
    elif user=='paper':
        if computer=='rock':
            return 'won','covers'
        elif computer=='lizard':
            return 'lost','eats'
        elif computer=='spock':
            return 'won','disproves'
        elif computer=='scissors':
            return 'lost','cut'
        
    elif user=='rock':
        if computer=='paper':
            return 'lost','covers'
        elif computer=='lizard':
            return 'won','crushes'
        elif computer=='spock':
            return 'lost','vaporizes'
        elif computer=='scissors':
            return 'won','crushes'
        
    elif user=='lizard':
        if computer=='paper':
            return 'won','eats'
        elif computer=='rock':
            return 'lost','crushes'
        elif computer=='spock':
            return 'won','poisons'
        elif computer=='scissors':
            return 'lost','decapitate'
        
    elif user=='spock':
        if computer=='paper':
            return 'lost','disproves'
        elif computer=='rock':
            return 'won','vaporizes'
        elif computer=='lizard':
            return 'lost','poisons'
        elif computer=='scissors':
            return 'won','smashes'
#-----------------end of compare-----------------
def randomize(number):
    if number==1:
        return 'rock'
    elif number==2:
        return 'paper'
    elif number==3:
        return 'scissors'
    elif number==4:
        return 'lizard'
    elif number==5:
        return 'spock'
#-----------------end of randomizer--------------

rules() #<---this code will call the rules
print()
print('If you need to see the rules again type ?, h or help')
print()

while repeat=='y' or repeat=='Y' or repeat=='yes' or repeat=='YES' or repeat=='Yes':
    print('-----------------------------------------------------------------')
    opponent=randomize(opponentN)
    inputP=input('Enter you choice ')
    inputP=inputP.lower()
    print()

    if inputP=='?' or inputP=='h' or inputP=='help':
        rules()
    else:   
        result,beats=compare(opponent,inputP)
        if result=='tied':
            print('You tied!')
            print()
            print('Computer\'s choice:',opponent)
            print('Your choice:',inputP)
            ties=ties+1
        elif result=='won':
            print('You',result,',',inputP,beats,opponent,'!')
            print()
            print('Computer\'s choice:',opponent)
            print('Your choice:',inputP)
            wins=wins+1
        elif result=='lost':
            print('You',result,',',opponent,beats,inputP,'!')
            print()
            print('Computer\'s choice:',opponent)
            print('Your choice:',inputP)
            looses=looses+1
        print()
        repeat=input('Do you want to play again? (y/n)')
print()
print('You won',wins,'times, lost',looses,'times and tied',ties,'times.')
print('Your winrate was',int((wins*100)/(wins+looses+ties)),'%.')
print()
print('Thanks for playing!')






