# login (3 ATTEMPT) 
print("*************** WELCOME TO MY ATM ************\n")
attempt = 0
pin = 0
amount = 5000

while True:
    
    
    while attempt <= 3 :
        pin = int(input("\n----**** ENTER YOUR PIN (ex : 1234) : "))
        if 1000<= pin < 10000:
            while True:
                conform_pin = int(input("****-----CONFORM YOUR PIN : "))
                if conform_pin != pin:
                    print("GIVE CORRECT CONFORM PIN ￣へ￣")
                    continue
                   
                else:
                    print("\n!!!!___PIN SUCCESFULL ✅___!!!!")
                    print("\n1. BALANCE CHECK ^_^\n2. DEPOSIT ✿◡‿◡\n3. WITHDRAW ＞﹏＜\n")
                    break
            break    
        else:
            print("GIVE 4 DIGIT PIN ￣へ￣")
            attempt+=1
            
        if attempt == 3:
            print("YOUR ATTEMPT GONE , YOUR ACCOUNT HAS BLOCKED ＞︿＜")
            break
    break  
    # BALANCE CHECK
while 1000<= pin < 10000:
    
    user=int(input("\^o^/ ENTER YOUR GIVEN CHOICE (1/2/3) : "))
    
    if user > 3 :
        print("INVAILED CHOICE !")

    if user == 1:
        print("\nCHECK YOUR BALANCE....! \n")
        while True:
            user_pin = int(input("ENTER YOUR PIN : "))
            if user_pin != pin:
                    print("ENTER CORRECT PIN")
                    continue
            else:
                print("YOUR CURRENT BALANCE ",amount )
                break
        # DEPOSIT

    if user == 2:
        print("\nDEPOSIT YOUR MONEY ")
        while True:
            user_pin = int(input("ENTER YOUR PIN : "))
            if  user_pin == pin :
                deposit = int(input("HOW MUCH YOU DEPOSIT : "))
                amount = amount + deposit
                print(f"YOUR CURRENT BALANCE {amount}")
                break  
            else:
                print("ENTER CORRECT PIN ")
                continue
         
        # WITHDRAW (WITH BALANCE)

    if user == 3:
        print("\nWITHDRAW YOUR AMOUNT ")
        while True :
            user_pin = int(input("ENTER YOUR PIN : "))
            if  user_pin == pin :
                withdraw = int(input("HOW MUCH WITHDRAW YOUR MONEY : "))
                if withdraw > amount:
                    print(f"YOU HAVE NOT SUFFICIENT BALANCE , PLEASE WITHDRAW {amount} WITHIN ")
                    break 
                amount = amount - withdraw
                print(f"WITHDRAW SUCCESFULLY , YOUR CURRENT BALANCE {amount}")
                break
                    
            else:
                print("ENTER CORRECT PIN ")
                continue
 

