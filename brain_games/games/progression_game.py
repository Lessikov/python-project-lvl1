import prompt
from random import randint

def progression():
    print('What number is missing in the progression?')
    b = 0
    while b < 3:
        start = randint(1, 9)
        step = randint(1, 9)
        stop = randint(step * 5 + start, step * 13 + start)
        question = []
        for i in range(start, stop, step):
            question.append(i)
        hidden_index = randint(1, len(question)-1)
        hidden_number = question[hidden_index]
        question[hidden_index] = '..'
        print('Question:', *question)
        answer = prompt.string('Your answer: ')
        if answer ==str(hidden_number):
            print('Correct!')
            b += 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {hidden_number}')
            break
    if b == 3:
        return True
    else:
        return False
