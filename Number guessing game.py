import random
def guess_num():
    num_s=random.randint(1,10)
    num_g=int(input("Guess a number between 1 to 10=> "))
    if num_g==num_s:
        print('Voila! You have guessed the correct number.')
    else:
        if num_g>num_s:
            print('The Number is too high.')
        else:
            print('The number is too low.')
guess_num()