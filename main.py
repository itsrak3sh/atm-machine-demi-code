balance = 5000                        #store user's daata 
password=9292

print ("Enter Your Card")            #tell user to input there card
pin=int(input('enter your pin '))         #take pin from user as input 


if pin==password:             #check the pin is corrrect or not 

#ask to user what he/she want to do

    x=int(input('''    Press 1 to withdrawal money
    Press 2 to change pin.                             
    Press 3 to deposit money 
    Press 4 to check balance ; '''))

#respone user according to the input

    if x==1 :     
        withdrawal_amount= int(input('enter withdrawal amount : '))
        if withdrawal_amount < balance:
            print(f'please take your money,{withdrawal_amount} deducted from your account')
        else:
            print('insufficiant balance')

    elif x==2:
        pin=int(input('enter your new pin : '))
        print('new pin created sucessfully')
        
      
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