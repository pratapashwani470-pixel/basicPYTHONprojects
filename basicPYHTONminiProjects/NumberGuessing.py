import random
target = random.randint(1,100)


while True:
    GUESS_number = int(input('GUESS ANY NUMBER, BETWEEN (1 TO 100) '))
    if (GUESS_number == target  ):
         print ('SUCCESS : CORRECT GUESS!!')
         break
    elif (GUESS_number > target):
        print('NUMBER IS TOO BIG , try again  ')
    elif( GUESS_number < target):
        print('NUMBER IS TOO SMALL , try again  ')