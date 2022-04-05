#!/usr/bin/env python3
import prompt
from random import randint


def main():
    print('Welcome to the brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no"')
    i = 0
    question = 0
    while i < 3:
        question = randint(1, 100)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer.lower() != 'no' and answer.lower() != 'yes':
            print(f"'yes' is wrong answer ;(.\
                    Correct answer was 'no'. Let's try again, {name}!")
            break
        elif question % 2 == 0 and answer.lower() == 'yes':
            print('Correct!')
            i += 1
        elif question % 2 != 0 and answer.lower() == 'no':
            print('Correct!')
            i += 1
        elif question % 2 != 0 and answer.lower() == 'yes':
            print(f"'yes' is wrong answer ;(.\
                    Correct answer was 'no'. Let's try again, {name}!")
            break
        elif question % 2 == 0 and answer.lower() == 'no':
            print(f"'no' is wrong answer ;(.\
                    Correct answer was 'yes'. Let's try again, {name}!")
            break
    if i == 3:
        print(f'Congrulations, {name}!')


if __name__ == '__main__':
    main()
