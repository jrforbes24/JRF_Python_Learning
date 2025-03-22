# x = int(input("Please enter and integer?"))

# if x < 0:
#     x = 0
#     print('Negative change to zero.')
# elif x == 0:
#     print('The number that is not a number.')
# elif x == 1:
#     print('The lonliest number.')
# else:
#     print('Now we are getting somewhere.')

# def countCapitals(text):
#     count = 0
#     for char in text:
#         if char.isupper():
#             count += 1    
#     return count

# names = ['LucIEie', 'Sam', 'Lucinda']

# for n in names:
#     print(n, '\nNumber of characters:', len(n), '\nNumber of capitals:', str(countCapitals(n)))

# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# for user, status in users.copy().items():
#     print(user, status)
#     if status == 'inactive':
#         print("Deleting the following user:", user)
#         del users[user]

# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status

# print(active_users)

# for i in range(10, 21):
#     print(i, end=" ")
#     print("")

# a = 'Washington'

# for i in range(len(a)):
#     print(i+1, a[i]) 

# print(sum(range(10)))

# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# seasonIndex = list(enumerate(seasons))
# print(seasonIndex[0])

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(f"{n} equals {x} * {n//x}")
#             break
#     else:
#         # loop fell through without finding a factor
#         print(f"{n} is a prime number.")


# for num in range(2, 30):
#     if num % 3 == 0:
#         print(f"Found a number divisible by 3: {num}.")
#         continue
#     need to add a check for even and a continue  
#     print(f"Found an odd number {num}.")

# def initlog(*args):
#     pass #TODO


# if 'bar' in ['bar', 'baz', 'qux']:
#     print('Expression was true')
#     print('Executing statement in suite')
#     print('...')
#     print('Done.')
# print('After conditional')

# if 'f' in 'boo': 
#     print(1) 
#     print(2)
#     print('3')
# elif 'b' in 'poo': print('f'); print('b')
# else: print('no boo ');print('or poo ');print('here.')

# x = 0 
# while True:
#     x += 1
#     print("I one am adding to x: ", str(x))
#     if x == 10:
#         break

# y = 0
# while y < 10:
#     y += 1
#     print("I am adding one to y: ", str(y))


# import random

# print('I am selecting a random number between 1 and 10 inclusive.')
# random_Number = random.randint(1,10)
# print('Can you guess the number?')
# global_guess = int(input('what is your guess?'))

# def check_Guess_Type(guess):
#     if isinstance(guess, int):
#         return True
#     else:
#         print('that is not an integer (whole number)')
#         return False

# def guess_eq_random(guess):
#     if guess == random_Number:
#         return True
#     elif guess < random_Number:
#         print('Too low.')
#     else:
#         print('Too high.')


# while random_Number != global_guess:

#     if check_Guess_Type(global_guess):
#         if guess_eq_random(global_guess):
#             break
    
#     global_guess = int(input('what is your guess?'))
        

# print(f'You got it the random number is: {global_guess}')



thisDict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
thisDict['color'] = 'red'
thisDict['horsepower'] = 271

# # print(len(thisDict))
# # print(type(thisDict))
# # print(thisDict)
# # print(thisDict['brand'])
# print(thisDict.keys())
# print(thisDict.get('horsepower','umm not there'))
# thisDict['horsepower'] = 250
# print(thisDict.keys())
# print(thisDict.get('horsepower','umm not there'))
# print(thisDict.values())
# print(thisDict.items())

# if 'horsepower' in thisDict:
#     print('Yep found horsepower.')



# print(thisDict)
# thisDict['year'] = 2025
# print(thisDict)
# thisDict.update({'year':2015})
# print(thisDict)
# popped = thisDict.pop('color')
# print('What was popped:', popped)
# print(thisDict)
# popped_Item = thisDict.popitem()
# print('The item popped:', popped_Item)
# print(thisDict)
# del thisDict['year']
# print(thisDict)
# thisDict.clear()
# print(thisDict)

# Dad = {
#     'name': 'John',
#     'age': 35,
#     'sex': 'male'
# }

# Mom = {
#     'name': 'Cindy',
#     'age': 31,
#     'sex': 'male'
# }

# child6 = {
#     'name': 'Lucie',
#     'age': 8,
#     'sex': 'female'
# }

# family_at_home = {
#     'Dad': Dad,
#     'Mom': Mom,
#     'child6': child6
# }

# print( family_at_home )

# print( "Mom's name:", family_at_home['Mom']['name'])

# print('Now looping!')

# for x, obj in family_at_home.items():
#     print(x)

#     for y in obj:
#         print(y + ':', obj[y])

# print(family_at_home['Dad']['name'])

# squares = [x**2 for x in range(10,15)]

# print(squares)

# name = input('Hi, what is your name? ')

# def greeting(the_name):
#     print('Hello', the_name, 'welcome to my world!')

# def addNumbers(num1, num2):
#     return num1 + num2

# greeting(name)

# number1 = int(input('What is the first number you would like to play? '))
# number2 = int(input('What is the second number you would like to play? '))

# print('The sum of your numbers is: ', str(addNumbers(number1, number2)))

# print("Fibonacci series")

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# fib(10000)

# i = 5

# def f(arg=i):
#     print(arg)

# i = 15

# f()
# f(i)

# def my_sum(*args):
#     result = ''
#     for x in args:
#         result = result + x + ' '
#     return result

# print(my_sum('Go', '2', 'Town'))

def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(e="!",a="Real", f="Python", c="Is", d="Great" ))








