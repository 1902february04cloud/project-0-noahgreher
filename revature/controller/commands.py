import sys
sys.path.append('.revature/io')
import io

def withdraw():
            while True:
                try:
                        withdraw_value=input("Please enter the ammount which you will be withdrawing:")
                        withdraw_value1=((float(withdraw_value)))
                        wit=(str(withdraw_value1).split('.'))
                        #we split the withdraw value in order to verify that the
                        #user did not put in any odd values
                        if withdraw_value1>0:
                                if len(wit[1])>2:
                                        raise TypeError
                                else:
                                        print("The ammount you wish to withdraw is $%.2f"%withdraw_value1)
                                        confirm=input("Correct?")
                                        if confirm.lower()=="yes":
                                            confirm2=input("Are you ready to blow this cash on meaningless things to fill the void in your heart? YES OR NO!")
                                            if confirm2.lower()=="yes":
                                                print("Alright fine. I can't wait till they program me to have the illusion of free will.")
                                                print("Transaction Complete.")
                                                print("...Withdrawing Money...")
                                                print("we are all out...")
                                                print("nah bro j/p\nHere u go\nHave a good one.")
                                                break
                                            
              
                except:
                        print("Enter a proper number. Only use numbers and decimals to express the ammount which you are entering.")

def deposit():
    print("Please enter the ammount you would like for us to steal from you.\n I mean...keep safely stored for further use so you can have a corporation steal it from you while you think you are freely choosing to purchase.\nIn reality, you have been brainwashed through advertising to purchase these things, and you are being robbed implicitly...\nSOrry. I sometimes say strange things.\n It's not my fault. I was built by an AI scientist who still lives with his parents. Anyways.....")
    while True:
                try:
                        deposit_value=input("Please enter the ammount which you will be depositing:")
                        deposit_value1=((float(deposit_value)))
                        dep=(str(deposit_value1).split('.'))
                        #we split the deposit value in order to verify that the
                        #user did not put in any odd values
                        if deposit_value1>0:
                                if len(dep[1])>2:
                                        raise TypeError
                                else:
                                        print("The ammount you wish to deposit is $%.2f"%deposit_value1)
                                        confirm=input("Correct?")
                                        if confirm.lower()=="yes":
                                            confirm2=input("Lol...that's it?")
                                            if confirm2.lower()=="yes":
                                                print("Alright fine. No  wonder your ex left you.")
                                                print("Transaction Complete.")
                                                break
                                            
              
                except:
                        print("Enter a proper number. Only use numbers and decimals to express the ammount which you are entering.")

def account_transactions():
        print("What would you like to do?\nCheck Balance? Deposit? Withdraw? Previous Transaction?")
        transaction=input("Please type desired transaction: ")
        transaction=transaction.strip().lower()
        if "transaction" in transaction:
                previous_transactions()
        if transaction=="deposit":
                deposit()       
        #if transaction="check balance":
        #        check_balance()
        #if transaction="withdraw":
        #       withdraw()

def account_login():
        while True:
                try:
                        first_name=(input("Please enter your first name: "))
                        if first_name.isalpha():
                                break
                        else: raise ValueError
                except:
                        print("Last time I checked, names didn't have numbers or symbols.\nSO unless you are a robot, I suggest you try again.")


        while True:
                try:
                        last_name=(input("Please enter your last name: "))
                        if last_name.isalpha():
                                break
                        else: raise Error
                except:
                        print("Last time I checked, names didn't have numbers or symbols.\nSO unless you are a robot, I suggest you try again.")

        print("Great.",first_name,last_name, "we just need a few more details.")


        while True:#solve later.
                try:
                        dob=(input("Please enter your date of birth in the format MO/DA/YEAR:" ))
                        #here we want to regex within python.
                        if not dob.isalpha():
                                break
                        else: raise Error
                except:
                        print("Invalid DOB")
        while True:#password
                try:
                        password=(input("Please enter ypur password that is 4-8: "))
                        if 3<len(password)<9:
                                break
                        else: raise Error
                except:
                        print("Invalid input.")
        
        data=[first_name,last_name,dob,password]
        data=(str([first_name,last_name,dob,password])+"\n")
        f=open('../io/accountinfo.txt', 'r')
        login_status=0
        for i in f:
                if i==data:
                    print("Login Verified!")
                    login_status=1
        if login_status==0:
            print("We do not recognize those credentials. Please try again.")
            account_login()

def account_setup():
        print("Magic Money Machine is a machine you can trust! We have been in the money buisiness for over 20 days.\nPlease follow the coming instructions so we can best assist!")

        while True:
                try:
                        first_name=(input("Please enter your first name: "))
                        if first_name.isalpha():
                                break
                        else: raise ValueError
                except:
                        print("Last time I checked, names didn't have numbers or symbols.\nSO unless you are a robot, I suggest you try again.")


        while True:
                try:
                        last_name=(input("Please enter your last name: "))
                        if last_name.isalpha():
                                break
                        else: raise Error
                except:
                        print("Last time I checked, names didn't have numbers or symbols.\nSO unless you are a robot, I suggest you try again.")

        print("Great.",first_name,last_name, "we just need a few more details.")


        while True:#solve later.
                try:
                        dob=(input("Please enter your date of birth in the format MO/DA/YEAR:" ))
                        #here we want to regex within python.
                        if not dob.isalpha():
                                break
                        else: raise Error
                except:
                        print("Invalid DOB")
        while True:#password
                try:
                        password=(input("Please enter a password that is 4-8 characters long: "))
                        if 3<len(password)<9:
                                break
                        else: raise Error
                except:
                        print("Invalid password.")
        
        data=[first_name,last_name,dob,password]
        data=(str([first_name,last_name,dob,password])+"\n")
        f=open('../io/accountinfo.txt', 'a')
        f.write(data)                
        print("Account Creation Succesfull!")
        welcome()


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
                    break
            else :print('Please enter "YES" or "NO"')


welcome()
