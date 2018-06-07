import random
gen_num = random.randint(0, 9)

while (1):
    i_num = int(input('Enter a number which is in range of 0 to 9'))
    if(gen_num == i_num):
        print('perfect  , guessed mumber is equal to the generated number')
        break
    elif(gen_num < i_num) :
        print (' your number is greater than generated /expected number')
    elif(gen_num > i_num) :
        print (' your number is less than generated/expected number')
