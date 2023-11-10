import random


def int_to_list(n):
    return [int(i) for i in str(n)]


def random_number():
    res = set()
    n = 0
    while len(res) != 4:
        res.add(str(random.randint(0, 9)))
    while n < 999:
        n = int(''.join(list(res)))
    return int_to_list(n)


def counter(value, user_number):
    bulls, cows = 0, 0
    for i in range(len(value)):
        if value[i] == user_number[i]:
            bulls += 1
        elif user_number[i] in value:
            cows += 1
    return bulls, cows


main_flag = False

while True:
    ans = input('Start game? Y/N:\n')
    if ans == 'Y':
        main_flag = True
    elif ans == 'N':
        main_flag = False
    else:
        print('Wrong answer')
        continue
    break

while main_flag:
    val = random_number()
    print(val)
    local_flag = True
    while local_flag:
        guess = int_to_list(int(input('Your number: ')))
        res = counter(val, guess)
        print(f'Answer: {res[0]} bulls, {res[1]} cows')
        if res == (4, 0):
            print('You Win!\nRestart game to play again')
            while True:
                next_game = input('start new game? Y/N\n')
                if next_game == 'Y':
                    local_flag = False
                    break
                elif next_game == 'N':
                    print('See you later')
                    local_flag = False
                    main_flag = False
                else:
                    print('Wrong answer')
                    continue
                break
        else:
            while True:
                next_iter = input('Make a new guess? Y/N\n')
                if next_iter == 'Y':
                    local_flag = True
                elif next_iter == 'N':
                    print('See you later')
                    main_flag, local_flag = False, False
                else:
                    print('Wrong answer')
                    continue
                break
