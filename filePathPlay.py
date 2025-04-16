import os
import getpass
theFilePathResults = os.listdir('C:\\Users\\johnr\\Documents\\GitHub\\JRF_Python_Learning')
totalFileSize = 0
for i in theFilePathResults:
    if os.path.isfile(i):
        totalFileSize += os.path.getsize(i)
        print(i)   


print(totalFileSize)

totalFileSize = 0
for filename in os.listdir('C:\\Users\\johnr\\Documents\\GitHub\\JRF_Python_Learning'):
    if not os.path.isfile(os.path.join('C:\\Users\\johnr\\Documents\\GitHub\\JRF_Python_Learning', filename )):
        continue
    totalFileSize += os.path.getsize(os.path.join('C:\\Users\\johnr\\Documents\\GitHub\\JRF_Python_Learning', filename ))
    print(filename)

print(totalFileSize)

user = getpass.getuser()
print(user)