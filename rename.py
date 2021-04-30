import os
import fnmatch
cwd = os.getcwd()
files = os.listdir(cwd)
print("Current working directory: {0}".format(cwd))
removeThisChar = input("enter the chartecter: ")
for index, file in enumerate(files):
    if not fnmatch.fnmatch(file, '*.py'):
        filename, file_extension = os.path.splitext(file)
        my_string = filename.replace(str(removeThisChar),' ')
        os.rename(os.path.join(cwd, file), os.path.join(cwd, ''.join([str(my_string), str(file_extension)])))
    print("Current working directory: {0}".format(file))