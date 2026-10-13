Balance = 0.0
change = 0.0
item_price = 0.0
insufficient_balance = 0
Done = "FALSE"


while insufficient_balance == 0:


    while Done == "FALSE": # Allows for  repeated attempts to input money as many times the user wants
        coins = float(input("Enter 10p, 20p, 50p, 100p coins: "))
        if coins == 10 or coins == 20 or coins == 50 or coins == 100:
            Balance = Balance + coins 
            if Balance >= 100:
                print(f"Your current balance is £{(Balance / 100):.2f}")
            else:
                print(f"Your current balance is {(Balance / 100 ):.2f}")
        else:
            print("Invalid coins. Please try again.")
        Done = input("Done? True or False: ").upper()

    item_code = input("Enter the item code you want to purchase(01 = Cereal bar, 02 = Crisps, 03 = Chocolate bar, 04 = Bottled water, 05 = Fanta ): ")

    if item_code == "01":
        item_price = 50
        if Balance >= item_price:
            Change = Balance - item_price
            print(f"Successful purchase, Your change is {(Change / 100):.2f}p")
            insufficient_balance = 1
        else:
            print("Not enough balance. Refunded", Balance)
            insufficient_balance = 1
    elif item_code == "02":
        item_price = 60
        if Balance >= item_price:
            Change = Balance - item_price
            print(f"Successful purchase, Your change is {(Change / 100):.2f}p")
            insufficient_balance = 1
        else:
            print("Not enough balance. Refunded", Balance)
            insufficient_balance = 1
    elif item_code == "03":
        item_price = 80
        if Balance >= item_price:
            Change = Balance - item_price
            print(f"Successful purchase, Your change is {(Change / 100):.2f}p")
            insufficient_balance = 1
        else:
            print("Not enough balance. Refunded", Balance)
            insufficient_balance = 1
    elif item_code == "04":
        item_price = 90
        if Balance >= item_price:
            Change = Balance - item_price
            print(f"Successful purchase, Your change is {(Change / 100):.2f}p")
            insufficient_balance = 1
        else:
            print("Not enough balance. Refunded", Balance)
            insufficient_balance = 1
    elif item_code == "05":
        item_price = 140
        if Balance >= item_price:
            Change = Balance - item_price
            print(f"Successful purchase, Your change is {(Change / 100):.2f}")
            insufficient_balance = 1
        else:
             print("Not enough balance. Refunded", Balance)  
             insufficient_balance = 1  

    continuation = input("Do you want to continue?: y/n: ") # Added a repeat function for concecutive use of the machine back to back without stacking the variables  from before
    if continuation.upper() == "Y" or continuation.upper() == "YES":
        insufficient_balance = 0
        Done = "FALSE" 
        Balance = 0
        Change = 0
        coins = ""
        item_code = ""


























