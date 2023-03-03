import shelve

myTrans = open('C:\\Users\\johnr\\Documents\\GitHub\\JRF_Python_Learning\\TestArtifacts\\newTestFile.txt', 'w')
myTrans.write('hello world, this is john, again. the first time..\n')
myTrans.write('hello world, this is john, again the second time...\n')
""" for line in theContent:
    theList = line.split(',')
    print(theList[3], '\n') """
myTrans.close()

baconFile = open('C:\\Users\\johnr\\Documents\\GitHub\\JRF_Python_Learning\\TestArtifacts\\bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('C:\\Users\\johnr\\Documents\\GitHub\\JRF_Python_Learning\\TestArtifacts\\bacon.txt', 'a')
baconFile.write('\n\n Bacon is deliciosa.')
baconFile.close()

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Garfield','Simon','Dawg','Hairless']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()


