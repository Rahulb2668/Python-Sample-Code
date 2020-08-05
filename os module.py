import os


print(dir(os))  # gets all the methods and attributes in os module
print(os.getcwd())  # get current working directory

# # Changing directory
# os.chdir('/home/rahul/Desktop/')
#
# print(os.getcwd())
#
# print(os.listdir())  # Prints files in the current directory unless you share a path

# # Create a file in the desktop
# # Two ways
# os.mkdir('Demo1')  # Used to creat.e a directory
#
# os.makedirs('Demo2/sub-demo2')  # Used to create a directory with sub folders
#
# print(os.listdir())
#
# # How to delete a directory
# # Two ways
# os.rmdir('Demo1')  # Used to delete just
# os.removedirs('Demo2/sub-demo2')
# print(os.listdir())

# How to rename a directory

# os.rename('Demo1', 'Demo2')

# print(os.stat('Demo2'))
# print(os.stat('Demo2').st_mtime)
# # TO get the time in human readable form we import datetime module and just print the time
# # using fromtimestamp method
# from datetime import datetime
#
# mod_time = os.stat('Demo2').st_mtime
#
# print(datetime.fromtimestamp(mod_time))

# os.walk method returns all the details of all the dir and files
# and it return three parameters in name path,name,files

for dirpath, dirname, filenames in os.walk('/home/rahul/Desktop/Music/'):
    print('Dirpath: ', dirpath)
    print('Dirname:', dirname)
    print('files in it ', filenames)

