import random
random.seed(42)

INDENT = ' ' * 4


# ------------------------------- select level ------------------------------- #
# define levels
levels = (
    {
        'name': 'EASY',
        'range':(1,10),
        'moves': 7
    },
    {
        'name': 'MEDIUM',
        'range':(1,10),
        'moves': 5
    },
    {
        'name': 'HARD',
        'range':(1,100),
        'moves': 10
    }
)

# print level menu:
print(f'Welcome to Guess the Number!\n')
print(f'{" Levels ":*^50}')
for idx, level in enumerate(levels):
    line = f"{idx+1}. {level['name']}, range: {level['range']}, max moves: {level['moves']}"
    print(f'* {line:46} *')
print('*' * 50)

# let user choose a level:
while True:
    choice = int(input(f'\n>>> Select level: '))
    # check for correct input:
    if 1<=choice<=len(levels):
        break
    else:
        print(f'{INDENT}( Enter a number between 1 and {len(levels)} )')

# setup level parameters:
level = levels[choice-1]

START = level['range'][0]
STOP = level['range'][1]
MAX_MOVES = level['moves']

# print(f'START: {START}, STOP: {STOP}, MAX_MOVES: {MAX_MOVES}')

# -------------------------------- Game start -------------------------------- #
print(f"\n*** Let's play {level['name']}. Good Luck! ***")
# Generate a random number between START and STOP
number_to_guess = random.randint(START, STOP)
moves_left = MAX_MOVES

# print(f'# number_to_guess: {number_to_guess}') # for testing and debugging

while True:
    # game end if moves_left is 0:
    if moves_left==0:
        print(f'\n*** GAME OVER! My number was {number_to_guess} ***')
        break

    # User inputs their guess
    guess = int(input(f"\n>>> Guess the number (between {START} and {STOP}): "))

    # Check if the guess is valid
    if not START<=guess<=STOP:
        print(f"{INDENT}( {guess} is out of bounds. Enter a number between {START} and {STOP} )")
        continue

    # decrement moves:
    moves_left -= 1

    # Compare guess to the number
    if guess < number_to_guess:
        print(f"Too low! Moves left: {moves_left}")
    elif guess > number_to_guess:
        print(f"Too high! Moves left: {moves_left}")
    else:
        moves = MAX_MOVES-moves_left
        print(f"\n*** Congratulations! You guessed it right in {moves} move{'s' if moves>1 else ''}!. ***")
        break
