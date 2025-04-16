import shutil
import os
import send2trash

# shutil.copy('C:\\Users\\johnr\\Documents\\GitHub\\JRF_Python_Learning\\spam.txt','TestArtifacts\\newSpam.txt')

# shutil.copytree('TestArtifacts','C:\\Users\\johnr\\TestArtifacts')
# shutil.move('TestArtifacts\\bacon.txt','baconRules.txt')

""" shutil.move('baconRules.txt', 'TestArtifacts\\bacon.txt')
shutil.move('eggsAndBacon.txt', 'TestArtifacts\\eggs.txt')
shutil.move('spam.txt', 'TestArtifacts\\spam.txt') """

# os.unlink('TestArtifacts\\eggs.txt')
""" try:
    os.rmdir('TestArtifacts\\SubFolder')
except:
    print('Folder had content. Using shutil.rmtree.')
    shutil.rmtree('TestArtifacts\\SubFolder') """
 
""" os.chdir('TestArtifacts\\SubFolder')
for filename in os.listdir():
    if filename.endswith('.txt'):
        # os.unlink(filename)
        print(filename) """

# send2trash.send2trash('TestArtifacts\\SubFolder')




        
        