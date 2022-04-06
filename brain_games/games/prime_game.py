import prompt
from random import randint
from math import sqrt

def prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        number =randint(12, 67)
        number_prime = True
        a = 2
        while a < number:
            if number % a == 0:
                number_prime = False
                break
            a += 1
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number_prime == True and answer.lower() == 'yes':
            print('Correct!')
        elif number_prime == False and answer.lower() == 'no':
            print('Correct!')
        elif number_prime and answer.lower() == 'no':
            print(f'{answer} wrong asnwer ;(. Correct answer was yes')
            break
        else:
            print(f'{answer} wrong answer ;(. Correct answer was no')
            break
        i += 1
    if i == 3:
        return True
    else:
        return False
