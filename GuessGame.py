import random
import time

while True:
    print('\nWelcome to Guess game.')

    print('In order to Win you have to guess a secret number between 0 to 10. ')

    print('You have 3 lives.')

    print('press return after your input\n')

    secret_number = random.randint(0, 10)
    guess_count = 1
    guess_limit = 3

    while guess_count <= guess_limit:

        while True:
            try:
                guess_input = int(input(f'Guess {guess_count} : '))
                break

            except:
                print('This is not a valid input!\n')

        if guess_input == secret_number:
            print("YOU WON!!")
            print(f'{secret_number} is the secret number.')
            break

        elif guess_input in range(0, 10):
            guess_count += 1
            print(f'\nTry Again. {4 - guess_count} Attempt left! \n')

        elif guess_input is not range(0, 10):
            print('\nInvalid entry')
            print('Make sure to type a number between 0 to 10\n')
            continue

    else:
        print('YOU LOOSE.')
        print(f'The secret number is {secret_number}')

    restart_option = input('Want to play again? (y/n): ')

    if restart_option == 'y':
        continue

    elif restart_option == 'n':
        print('Goodbye')
        break

    else:
        print('Not a valid entery!!')
        print('terminating ...')
        time.sleep(2.5)
        break
