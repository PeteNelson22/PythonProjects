import random

n=random.randrange(1,10)
guess=int(input('Enter a number: '))
while n!=guess:
    if guess<n:
        print('Too low')
        guess=int(input('Enter again: '))
    elif guess>n:
        print('Too hign')
        guess = int(input('Enter again: '))
    else:
        break
print('Congrats...You are correct')
