import random
import time
from colorama import Fore

def main():
    for i in range(1):
        print('Hello!')
        time.sleep(1.5)

    for i in range(1):
        print('Working on getting your new randomized password . . .')
        time.sleep(1.5)
    


    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()?'

    password = ('')
    for i in range(1):
        print('Your new password : ', end='')
        time.sleep(1.5)

    for x in range(16):
        password += random.choice(characters)
    for i in range(1):    
        print(Fore.GREEN + password)
        time.sleep(1)

    print(Fore.WHITE)
    print('Are you satisfied with your new password?')

    repeat = input('Do you want to run again : ').lower()
    if repeat == "yes":
            print()    
            main()
    else:
            print('Thank you for using this software!')
            exit()
main()