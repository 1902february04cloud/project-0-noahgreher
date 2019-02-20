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



withdraw()
