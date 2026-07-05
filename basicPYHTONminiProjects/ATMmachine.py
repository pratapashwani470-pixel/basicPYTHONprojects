password = '123'
balance = 1000

pas = input('Enter your password:-')
if pas == password:
    print('Access Granted')
    while True:
        print('<---ATM MENU--->')
        print('1. check balance')
        print('2. deposit money')
        print('3. withdraw money')
        print('4. exit')
    
    
        a = int(input('choose option ( 1 - 4)'))
        if a == 1:
            print('your balance is :-',balance)
        elif a == 2:
            amount= int(input('enter deposite amount'))
            balance += amount
            print('deposited! new balance :',balance)
        elif a == 3:
        
            withdraw = int(input('enter withdraw amount'))
            if withdraw <= balance:
                balance -= withdraw
                print('withdrawn! new balance :',balance)
            else:
                print('not enough balance!')
        elif a == 4:
            print('thank you for using ATM!')
            break
else:
    print('WRONG pin , ACCESS denied')