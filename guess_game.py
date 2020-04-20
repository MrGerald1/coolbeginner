#PSEUDO CODE: building a guessing game
from random import randrange
print('Welcome to the Ultimate guessing game.\nProve yourself worthy to be the ultimate guessing champion to win the grand prize.')
user_input=input('Choose your difficulty (Easy, Medium, Hard)?: ').capitalize()

while user_input not in 'Easy Medium Hard'.split():
    user_input = input('You must enter a difficulty (Easy, Medium, Hard): ').capitalize()
print(f'You have chosen {user_input}. ')

if user_input=='Easy':
    generated_num= randrange(1,10)
    #On easy, user has to guess number between 1-10 with 6 guesses
    print('In this difficulty, you have only 6 guesses to choose the correct random number between 1-10')
    print('Guess the correct random number between 1-10')
    n=6
    while n>=1:
        num=int(input('What number is it? '))
        while num not in range(0,11):
            num=int(input('Guess a number between 0 and 10: '))
        if num == generated_num:
            print("You got it right with", n,'attempts left. Congratulations champion!!!')
            print('10 Gbosa for you')
            gbosa=0
            while gbosa<9:
                print('GBOSA!')
                gbosa+=1
            print('GBOSA!!!!!!!!!!!!!!')
            break
        elif num!= generated_num:
            print("That was wrong, Try again")
            n-=1
            print('You have', n,'attempts left, try again.')
    if n == 0:
        print('Game over, you have no more attempts again.\nThe random number is', generated_num)

elif user_input=='Medium':
    #On medium, user has to guess number between 1-20 with 4 guesses
    generated_num= randrange(1,20)
    print('In this difficulty, you have only 4 guesses to choose the correct random number between 1-20')
    print('Guess the correct random number between 1-20')
    n=4
    while n>=1:
        num=int(input('What number is it? '))
        while num not in range(0,21):
            num=int(input('Guess a number between 0 and 20: '))
        if num == generated_num:
            print("You got it right with", n,'attempts left. Congratulations champion!!!')
            print('10 Gbosa for you')
            gbosa=0
            while gbosa<9:
                print('GBOSA!')
                gbosa+=1
            print('GBOSA!!!!!!!!!!!!!!')
            break
        elif num!= generated_num:
            print("That was wrong, Try again")
            n-=1
            print('You have', n,'attempts left, try again.')
    if n == 0:
        print('Game over, you have no more attempts again.\nThe random number is', generated_num)
            
elif user_input=='Hard':
    #On hard, user has to guess number between 1-50 with 4 guesses
    generated_num= randrange(1,50)
    print('In this difficulty, you have only 3 guesses to choose the correct random number between 1-50')
    print('Guess the correct random number between 1-50')
    n=3
    while n>=1:
        num=int(input('What number is it? '))
        while num not in range(0,51):
            num=int(input('Guess a number between 0 and 50: '))
        while False:
            if num not in range(0,11):
                print('Enter a number between 0 and 10')
                num=int(input('What number is it? '))
        if num == generated_num:
            print("You got it right with", n,'attempts left. Congratulations champion!!!')
            print('10 Gbosa for you')
            gbosa=0
            while gbosa<9:
                print('GBOSA!')
                gbosa+=1
            print('GBOSA!!!!!!!!!!!!!!')
            break  
        elif num!= generated_num:
            print("That was wrong, Try again")
            n-=1
            print('You have', n,'attempts left, try again.')
    if n == 0:
        print('Game over, you have no more attempts again.\nThe random number is', generated_num)


if num not in range(0,11):
    print('Enter a number between 0 and 10')
    num=int(input('What number is it? '))
