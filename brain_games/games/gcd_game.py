import prompt
from random import randint

def gcd(number_1, number_2):
    min_number = 0
    if number_1 <= number_2:
        min_number = number_1
    else:
        min_number = number_2
    i = 1
    nod = 0
    while i <= min_number:
        if number_1 % i == 0 and number_2 % i == 0:
            nod = i
            i += 1
        else:
            i += 1
    return nod

#i = 1
#while i < 35:
 #   x = gcd(randint(1, 20), randint(1, 20))
  #  print(x)
   #i += 1
def gcd_games():
    print('Find the greatest common divisior of given numbers')
    i = 0
    while i < 3:
        number1 = randint(1, 20)
        number2 = randint(1, 20)
        correct_answer = str(gcd(number1, number2))
        print(f'Question: {number1} {number2}')
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
            print('Correct!')
            i += 1
        else:
            print(f'{answer} is wrong answer ;(.Correct answer was {correct_answer}.')
            break
    if i == 3:
        return True
    else:
        return False
