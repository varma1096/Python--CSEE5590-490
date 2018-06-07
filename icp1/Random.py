import random

input_num = int(input("Enter any number between 0 to 9"))
a= random.randint(0,9)

if(input_num == a):
    print("Congratulations! you guessed it  perfectly ")
    print(" Number was ", a)
elif(input_num < a):
    print("Your Guessed number is less than the random/expected  number")
    print( " Number was ",a)
elif(input_num > a):
    print("Your guessed number is greater than the random/expected number")
    print(" Number was ", a)