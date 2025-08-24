# Topic: Inbuilt functions in set
# Task :  Operations on strings &Operations on set


#  String inbuilt func:
#  To get char to ascii - ord(char) 
#  To change ascii to char -chr(ascii value)

str = "Hello"
print(ord("e"))
print(chr(101))
# Output: 101
#          e
# Case convertion builtin methods only works for Alphabets.
#  upper() : to convert the lowercase to upper case
#  lower() : to convert the uppercase to lowercase 

str1 = "Programming"
print(str1.lower())
print(str1.upper())
# Output: programming
#         PROGRAMMING

#  islower() : To check whether lower or not
#  isupper() :  To check whether upper or not

s = "flower"
print(s.islower())
print(s.isupper())
# Output: True
#         False

# swapcase() : converts the chars from if they are small then it converts into upper and viceversa.
# len() : To find the lengthe of the string
# count() : To count the number of occurances of a subsrting in the given string
# index() : I t returns the lowest index of the substiring if found in the given string. if not found it raises a value error

s1 = 'Good MoRniNg'
print(s1.swapcase())
print(len(s1))
print(s1.count('o'))
print(s1.index('M'))
# Output: gOOD mOrNInG
#              12
#               3
#               5

# title() : It is used to Capitalize the first letter in the each word 
# capitalize : only converts the first char in the word .

s2 = "this is the title method"
print(s2.title())
print(s2.capitalize())
# Output: This Is The Title Method
#         This is the title method






# strip() :  To remove the excess spaces in the start and end .  we need to reassigned the value again for its operations
# lstrip() : To remove the excess space in the starting
# rstrip() : To remove the excess space in the Ending

s = " hi Hello  "
s.lstrip()
s.rstrip()
s = s.strip()
print(s)
# Output:-hi hello
#             hi hello-
#             -hi Hello-

# Replace("old" , "new") : to replace old val to new value

S1 = "The captial of AP is kadapa"
s1 = S1.replace("kadapa" , "Amaravathi")
print(S1)
# Output: The captial of AP is Amaravathi

# string -find,split,join,startswith,endswith
# find : it returns the lowest index of the substring if it is found in given string. if not found then returns -1

str1 = "Good Morning"
print(str1.find("Good"))
Output: 0

# startswith :  it returns true if the string starts with the specified value otherwise false

print(str1.startswith("Goo"))
print(str1.startswith("morn"))
# Output: True
#         False

# endswith : it returns true if the string ends with the specified values otherwise false

print(str1.endswith("ing"))
print(str1.endswith("mor"))
# Output: True
#         False

# split : it splits the string at the specified separator and returns a list

input_nums = input("Enter all the numbers in csv format:")
for i in input_nums.split(","):
    print(i)

num1,num2 = input("Enter two numbers in csv format:").split()
print(num1,num2)

num1,num2,num3 = map(int,input("Enter the numbers in csv format:").split())
print(num1, num2, num3)

input1 = list( map(int,input("Enter the numbers in csv format:").split()))
print(num1,num2,num3)

# join : it joins the elements of an iterable to the end of the string ,we can use any delimeter to seperate the list elements into strings

list1 = ["1",'2','3','hi']
encoded_str = ','.join(list1)
print(encoded_str)
# Output: 1,2,3,hi


# 3. SET: A set is a collection of unordered, mutable (changeable) elements, but it does not allow duplicates.
#               Sets are written in curly braces {}
my_set = {10, 20, 30, 40}

# 1. add(x) → Adds an element
my_set.add(50)
print(my_set)  
Output: {40, 10, 50, 20, 30}

#  2. update(iterable) → Adds multiple elements
my_set.update([60, 70])
print(my_set)  
Output:  {70, 40, 10, 50, 20, 60, 30}

# 3. remove(x) → Removes element (Error if not found)
my_set.remove(20)
print(my_set)

# 4. discard(x) → Removes element (No error if not found)
my_set.discard(100)  
# Output:  No error

# 5. pop() → Removes random element
print(my_set.pop())

# 6. clear() → Removes all items
temp = my_set.copy()
temp.clear()
print(temp)  
# Output:  set()

#  7. union() → Combines sets
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  
Output: {1, 2, 3, 4, 5}

#  8. intersection() → Common elements
print(a.intersection(b))  
Output: {3}

#  9. difference() → Elements in a but not in b
print(a.difference(b))  
Output: {1, 2}

# 10. symmetric_difference() → Elements not common
print(a.symmetric_difference(b))  
Output: {1, 2, 4, 5}

# 11. issubset() → Checks subset
print({1, 2}.issubset(a))  
Output : True

# 12. issuperset() → Checks superset
print(a.issuperset({1, 2}))  
Output:  True

# 13. isdisjoint() → No common elements
print({6, 7}.isdisjoint(a))  
Output: True

# 14. copy() → Creates copy
copy_set = a.copy()
print(copy_set)  
Output: {1, 2, 3}

