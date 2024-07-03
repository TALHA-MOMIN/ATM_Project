print("Welcome to Python Bank ATM")
restart = ('Y')
chances = 3
balance = 100000
while chances>= 0:
    pin = int(input("Please Enter Your 4 Digit Pin : "))
    if pin == (8232):
        print("You Enterd Your Pin Correctly.")
        print("Press 1 For Your Balance : ")
        print("Press 2 To Make A Withdrawl : ")
        print("Press 3 To Pay In : ")
        print("Press 4 To Return Card\n : ")
        while restart not in ("n","NO","no","N"):
            print("Press 1 For Your Balance : ")
            print("Press 2 To Make A Withdrawl : ")
            print("Press 3 To Pay In : ")
            print("Press 4 To Return Card : ")
            option = int(input("What Would You Like To Choose ? : "))
            if option== 1:
                print("Your Balance Is ₹",balance)
                restart = input("Would You Like To Go Back ?")
                if restart in ("n","NO","no","N"):
                    print("Thank You")
                    break
            elif option== 2:
                option2 = ("y")
                withdrawl = float(input("How Much Would Like To Withdrawl ? 10,20,40,60,80,100 for other Enter 1 : "))
                if withdrawl in (10,20,40,60,80,100):
                    balance = balance - withdrawl
                    print("\n Your Balance Is Now ₹",balance )
                    restart = input("Would You Like To Go Back ?")
                    if restart in ("n","NO","no","N"):
                        print("Thank You")
                        break
                elif withdrawl != [10,20,40,60,80,100]:
                    print("Invalid Amount , Please Retry \n")
                    restart = ("y")
                elif withdrawl == 1:
                    withdrawl = float(input("Please Enter Your Desired Amount : " ))

            elif option == 3:
                Pay_in = float(input("How Much Would You Like To Pay In ? "))
                balance = balance + Pay_in
                print("\n Your Balance Is now ₹",balance)
                restart = input("Would You Like To Go Back ?")
                if restart in ("n","NO","no","N"):
                    print("Thank You")
                    break

            elif option == 4:
                print("Please Wait Whilst Your Card Is Returned......\n")
                print("Thank You For Your Service ")
                break
            else:
                print("Please Enter a Correct Number : \n")
                restart = ("y")
    elif pin != ('1234'):
        print("Incorrect Password ")
        chances = chances - 1
        if chances == 0:
            print("\n No More Tries ")
            break