# write a Armstrong Program using while loop
# num1  = int(input("Enter num1:"))
# sum = 0 
# original_num1 = num1
# l=len(str(num1))
# while num1 > 0:
#     rem = num1 % 10
#     sum += rem ** l
#     num1 = num1 // 10  
# print(sum)
# if sum == original_num1:
#     print("Armstrong number")
# else:
#     print("Not a armstrong") 
    

# write a Armstrong Program using for loop   
num1=int(input("Enter the Number= "))
num2=int(input("Enter the Number= "))
print('Armstrong number between', num1, 'and' ,num2 ,'are:')

for num in range(num1,  num2+ 1):
    n = len(str(num))
    result = 0

    for digit in str(num):   # for loop to calculate sum of powers
        result += int(digit) ** n

    if result == num:        # check Armstrong condition
        print(num)
