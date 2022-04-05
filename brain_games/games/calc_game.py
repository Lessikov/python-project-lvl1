import prompt
from random import randint, choice


def calc_games():
    print('What is the result of the expression?')
    i = 0
    argument_1 = 0
    argument_2 = 0
    operator = ' '
    result_sum = 0
    result_mult = 0
    while i < 3:
        operator = choice('+*')
        argument_1 = randint(1, 20)
        argument_2 = randint(1, 20)
        result_sum = argument_1 + argument_2
        result_mult = argument_1 * argument_2
        print(f'Question: {argument_1} {operator} {argument_2}')
        answer = prompt.string('Your answer: ')
        if operator == '+' and str(result_sum) == answer:
            print('Correct!')
            i += 1
        elif operator == '*' and str(result_mult) == answer:
            print('Correct!')
            i += 1
        else:
            if operator == '+':
                print(f'{answer} is wrong answer ;(.\
                        Correct answer was {result_sum}.')
                break
            if operator == '*':
                print(f'{answer} is wrong answer ;(.\
                        Correct answer was {result_mult}.')
                break
    if i == 3:
        return True
    else:
        return False
