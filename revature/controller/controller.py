import sys

sys.path.append('../service')
from services import account_setup
from services import account_login

def welcome():
        while True:
            print("Welcome to the Magic Money Machine!")
            user_check=input("Are you an existing user?")
            if user_check.lower()=="yes":
                    print("Great! Please enter your username and password.")
                    account_login()
                    break
            elif user_check.lower()=="no":
                    print("Well, what are you waiting for? Let's get you an account to help us steal your money. Um....I mean help you save.")
                    account_setup()
                    welcome()
                    break
            else :print('Please enter "YES" or "NO"')



