import prompt
from brain_games.games.prime_game import prime

def main():
    print('Welcome to the brain Games!')
    name = prompt.string('May I have your name? ')
    win_or_not = prime()
    if win_or_not:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}")

if __name__ == '__main__':
    main()


