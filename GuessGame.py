import random

print('\nWelcome to Guess game.')
print('In order to Win you have to guess a secret number between 0 to 10. ')
print('You have 3 lives\n')

secret_number = random.randint(0, 10)
guess_count = 1
guess_limit = 3


while guess_count <= guess_limit:

    while True:
        try:
            guess_input = int(input(f'Guess {guess_count} : '))
            guess_count += 1
            break
        except:
            print('This is not a valid input!\n')

    if guess_input == secret_number:
        print("YOU WON!!")
        break

    elif guess_input in range(0, 10):
        print(f'\nTry Again. {4 - guess_count} Attempt left! \n')


    else:
        print('\nInvalid entry')
        print('Make sure to type a number between 0 to 10')
        break

else:

    print('YOU LOOSE.')
    print(f'The secret number is {secret_number}')





