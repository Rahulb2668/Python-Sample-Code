# General way opening

# f = open('text.txt', 'r')
#
# print(f.name)
# print(f.mode)
#
# f.close()


# Using Context manager to open the file
# with open('text.txt', 'r') as f:
#     f_contents = f.read()
#     print(f_contents)
#     for line in f:
#         print(line, end='')

# # Accessing Specified no of characters in file
# with open('text.txt', 'r') as f:
#
#     size_to_read = 10
#
#     f_contents = f.read(10)
#     print(f_contents)

    # This is used to get the current position
    # k = f.tell()
    # print(k)

    # while len(f_contents) > 0:
    #     print(f_contents, end='#')
    #     f_contents = f.read(10)
    #
# The normal working of f.read() updates the position automatically inorder to start the reading from the 1st
# position itself we can use f.seek(start position)


# # Writing

# with open('text2.txt', 'w') as f:
#     f.write('Test')
# #
# with open('text2.txt', 'r') as f:
#     f_contents = f.read()
#     print(f_contents)


# # Copy from one file to another

# with open('text.txt', 'r') as rf:
#     with open('text_copy.txt', 'w') as wf:
#         for lines in rf:
#             wf.write(lines)
# #

# Copying a image using files
# Inorder to deal with images we have to use the files in binary mode thats why rb and wb

with open('/home/rahul/Desktop/animation-wallpaper-4.jpg', 'rb') as rf:
    with open('/home/rahul/Desktop/animation-wallpaper-4.jpg_copy', 'wb') as wf:
        for lines in rf:
            wf.write(lines)

