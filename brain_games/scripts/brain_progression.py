import prompt
from brain_games.games.progression_game import progression

def main():
    print('Welcome to the brain Games!')
    name = prompt.string('May I have your name? ')
    won_or_not = progression()
    if won_or_not:
        print(f'Congratulation, {name}!')
    else:
        print(f"Let's try again, {name}")

if __name__ == '__main__':
    main()
