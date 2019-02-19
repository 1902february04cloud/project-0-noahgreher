#!/usr/bin/env python3

def welcome():
        print("Welcome to the Magic Money Machine!")
        user_check=input("Are you an in existing user?")
        if user_check.lower()=="yes":
                print("Great! Please enter your username and password.")
                #here we execute a script for login
        if user_check.lower()=="no":
                print("Well, what are you waiting for? Let's get you an account to help us steal your money. Um....I mean help you save.")
                                                   
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
        f=open('bankinginfo.txt', 'a+')
        f.write(data)
#account_setup()

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
                        password=(input("Please enter a password that is 4-8 characters long: "))
                        if 3<len(password)<9:
                                break
                        else: raise Error
                except:
                        print("Invalid password.")
        
        data=[first_name,last_name,dob,password]
        data=(str([first_name,last_name,dob,password])+"\n")
        f=open('bankinginfo.txt', 'r')
        for i in f:
                if i==data:print("Login Verified!")        

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

def previous_transactions():
        f=open("transactions.txt","r+")
        for line in f:
                print(line)
#we need to develop this to discriminate based off of current user logged in, so it only prints the details relevant to that specific
#user--the username may be a key in a dictionary potentially. and we will read from the value entries, parsing through and only returning
#needed values in human readable for such as print("On", import some time stamp, +transaction,)


#i can potentially make one function that can be called by the deposit and the withdrawing methods.
def deposit_verify():
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
                                        return deposit_value1
                                        break
                except:
                        print("Enter a proper number. Only use numbers and decimals to express the ammount which you are entering.")


def deposit():
        f=open("transactions.txt", "a+")
        f.write(.
        print(deposit_verify())
        
account_transactions()
