balance = 5000
password=9292
print ("Enter Your Card")
pin=int(input('enter your pin '))
if pin==password:
    x=int(input('''    Press 1 to withdrawal money
    Press 2 to change pin
    Press 3 to deposit money 
    Press 4 to check balance ; '''))

    if x==1 :
        withdrawal_amount= int(input('enter withdrawal amount : '))
        if withdrawal_amount < balance:
            print(f'please take your money,{withdrawal_amount} deducted from your account')
        else:
            print('insufficiant balance')

    elif x==2:
        pin=int(input('enter your new pin : '))
        print('new created sucessfully')
        
      
    elif x==3:
        deposit_amount= int(input('enter deposit amount : '))
        if deposit_amount>0 :
            print(f'{deposit_amount} successfully credit to your account ')
    elif x==4:
        print(f'{balance} rupees')
    else:
        print ('Invalid keypress')
    
else:
    print('incorrect pin, try again')