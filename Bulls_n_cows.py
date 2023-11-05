import random


def int_to_list(n):
    return [int(i) for i in str(n)]


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
    val = int_to_list(random.randint(1000, 9999))
    local_flag = True
    while local_flag:
        guess = int_to_list(int(input('Your number: ')))
        res = counter(val, guess)
        print(f'Answer: {res[0]} bulls, {res[1]} cows')
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
