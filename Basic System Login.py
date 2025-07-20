#Basic System Login Using if-else condition
stored_username="Naga"
stored_password="1234"

Username_=input('enter the Username= ')
password_=input('enter the password= ')
if Username_==stored_username and  password_==stored_password: 
       print( 'Login Successful')  
else:
    print('Not valid. Please try Again')

#Basic System Login Using if-else condition  
stored_username="Naga"
stored_password="1234"

Username_=input('enter the Username= ')
password_=input('enter the password= ')

if Username_==stored_username:
       if password_==stored_password:
           print( 'Login Successful') 
else:
    print('Not valid. Please try Again')


#Basic System Login Using if-else condition 
stored_username="Naga"
stored_password="1234"

Username_=input('enter the Username= ')
password_=input('enter the password= ')

if Username_==stored_username and password_==stored_password:
     print( 'Login Successful') 
elif Username_!=stored_username and password_==stored_password:
     print('Invalid username.')
elif Username_==stored_username and password_!=stored_password:
     print('Invalid Password. Please try Again')

else:
    print('Not valid. Please try Again')