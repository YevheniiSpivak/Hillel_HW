import os

print(os.getcwd())  # directory

os.chdir('/Hillel_HW/HW-7/DEMO')   # change directory

os.mkdir('Test1')    # create directory

os.makedirs('Test2/Subdir')  # create sub directory

os.rmdir('Test1')     # delete directory

os.removedirs('Test2/Subdir')    # delete directory with subdirectories

os.mkdir('File_name_1')
os.rename('File_name_1', 'File_name_2')     # rename directory
os.rmdir('File_name_2')

print(os.stat('new.txt'))   # get static info

print(os.environ)   # get environments

print(os.environ.get('APPDATA'))    # get environment variables

file_path = os.path.join(os.environ.get('APPDATA'), 'Test.txt')     # join one or more path components
print(file_path)

print(os.path.split(file_path))     # get a tuple representing the start and tail of the specified path

print(os.path.basename(file_path))  # get base filename

print(os.path.dirname(file_path))   # get directory name from the specified path
