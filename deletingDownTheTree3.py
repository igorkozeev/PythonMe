import os, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') # This is a basic 'logging module' config call
logging.disable(logging.CRITICAL) # This function enables/disables logging (also it's possible to set a lower level of logging CRITICAL > ERROR > WARNING > INFO > DEBUG 
logging.debug('Starting program') # 1st Checkpoint  

os.chdir('c:\\Windows\\Temp')     # Sets a current working directory

logging.debug('The current working directory is: ' + os.getcwd()) # 2nd Checkpoint

for folderName, subfoldernames, filenames in os.walk(os.getcwd()): # Loop with three variables i.e. Folder\subfolder\filename 'os.walk' starts "moving" down the tree, starting from cwd. 
    logging.debug('folder name is ' + folderName + ' subfolders are ' + str(subfoldernames)) # 3rd Checkpoint
    print('The folder name is ' + folderName) # Prints current folder
    print('file names are:\n') # Not important. Just a title string.

    for i in range(len(filenames)): # Inner loop for files enumeration. Since 'filenames' is a list it takes it's lenght and lenght value passes to 'range'function.
        os.unlink(os.path.join(folderName) + '\\' + str(filenames[i])) # 'unlink' function deletes files with specified paths. 'path.join' represents that concantination as a string.
        #print(os.path.join(folderName) + '\\' + str(filenames[i]))    # "Dry run" print function. Before uncomment 'unlink' function above, that's the safe way to ensure that you're gonna deal with right files. 
    

logging.debug('End of the program') # Last Checkpoint

