# Justin Gerard - 04/10/24
# A perfect number is a positive integer that is equal to the sum of its proper divisors.
# This code allow to check if a number is magic or not. FUN guaranteed !

import numpy as np

while True:
    num = input("Enter an integer ('exit' to quit game) : ")

    if num == "exit":
        break

    num = int(num)
    p = (1+np.sqrt(1+8*num))/2 # Some magic number

    # p is a power of 2
    p_is_power_of_2 = False
    for i in range(250):
        if p == 2**i:
            p_is_power_of_2 = True

    # p-1 is a prime number
    p_minus_1_is_prime = True
    for i in range(2, int(p-1)):
        if (p-1)%i == 0:
            num_is_prime = False

    # General check
    if p != int(p): # p can be a real number.
        print(str(num)+" is not a perfect number. Sorry !\n")
    elif p_is_power_of_2 and p_minus_1_is_prime: # has to verify both
        print(str(num)+" is a perfect number :)\n")
    else:
        print(str(num)+" is not a perfect number. Sorry !\n")
