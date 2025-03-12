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

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break