import os

for folderName, subfolders, filenames in os.walk('c:\\Users\\Dave\\Desktop\\testFolder1'): # Set a path here.
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are:' + str(subfolders))
    print('The filenames in ' + folderName + ' are:' + str(filenames))
    print()
