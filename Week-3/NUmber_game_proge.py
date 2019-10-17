import random
print ('Hello, what is your name stranger?')
myName = input ()
print ('Well, nice to meet you ' + myName)
print ('Do you want to play a game? (yes/no)')
answer = input ()

#Some simple interaactions with the player

if answer == 'yes':
    print ('Cool! I am thinking of a number between 1 and 10. Try to guess it.')
elif answer == 'no':
    print ('Well, though luck sunshine. Your still gonna have to play it! I am thinking of a number between 1 and 10. Try to guess it!')
else:
    print ('That answer does not comfort me! Just say yes or no. (btw, im stupid and also case sensitive)')
    answer1 = input ()
    if answer1 == 'yes':
        print ('Cool! I am thinking of a number between 1 and 10. Try to guess it.')
    elif answer1 == 'no':
        print ('Well, though luck sunshine. Your still gonna have to play it! I am thinking of a number between 1 and 10. Try to guess it!')
    else:
        print ('I see that You dont want to follow the rules... Fuck it, just play the game! I am thinking of a number between 1 and 10. Try to guess it!')

# the actual game starts here

randomNumber = random.randint(1, 10)
guess = int(input())
if guess == randomNumber:
    print ('You are a lucky c***, ' + myName +'!' )
else: 
    print ('It breaks my hear to tell you, that you failed... miserably.')
print ('The end!')