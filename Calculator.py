# Welcome to Python Calculator
num1=float(input('Enter the First Number= '))
num2=float(input('Enter the Second Number= '))
symbol=input('enter the Operator= ')
if symbol=='+':
    print( num1 + num2)
elif symbol== '-':
    print(num1 - num2)
elif symbol=='*':
    print(num1 * num2)
elif symbol=='/':
    if num2!=0:
        print(num1 / num2)
elif symbol=='%':
    print(num1 % num2)
else:
    print('Invalid')

        

