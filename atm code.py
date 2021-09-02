print("WELCOME TO JAMMU AND KASHMIR ATM")
restart=("y")
chance=3
balance=9999.89
while chance>=0:
    pin=int(input("please enter your 4 digit pin:"))
    if pin==(1234):
        print("your entered pin is correctly")
        print("please press 1 for your balance")
        print("plese press 2 to make a withdrawal")
        print("please press 3 to pay in ")
        print("please press4 to return card\n")
        while restart not in ("n","NO","no","N"):
            print("please press 1 for your balance")
            print("please press 2 to make am withdrawal")
            print("please  press 3 to pay in ")
            print("please press 4 to return card")
            option=int(input("what do you like to choose?:"))
            if option==1:
                print("your balance is $",balance)
                restart=input("would you like to go back ?")
                if restart in ("n","NO","no","N"):
                    print("thank you")
                    break
            elif option==2:
                option2=("y")
                withdrawal=float(input("how much would you like to withdrawal? 10,20,40,60,80,100 for other enter 1:"))
                if withdrawal in[10,20,40,60,80,100]:
                    balance=balance-withdrawal
                    print("\nyour balance is now $",balance)
                    restart=input("would you like  to go back ?")
                    if restart in ("n","NO","no","N") :
                        print("thankyou")
                        break
                elif withdrawal!=[10,20,40,60,80,100]:
                    print("invalid amount ,please retry\n:")
                    restart=("y")
                elif withdrawal==1:
                    withdrawal=float(input("please enter desired amount:"))
            elif option==3:
                pay_in=float(input("how much would you like to pay in?"))
                balance=balance+pay_in
                print("\n your balancr is now $",balance)
                restart=input("would you like to go back ?")
                if restart in ("n","NO","no","n"):
                    print("thank you")
                    break
            elif option==4:
                print("please wait till your card is returned...\n")
                print("thank you for your service")
                break
            else:
                print("please enter a correct number\n")
                restart=("y")
    elif pin!=("1234"):
        print("incorrect password")
        chance=chance-1
        if chance==0:
            print("no more tries")
            break
