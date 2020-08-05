# f = open('test.txt')
# try:
#     f = open('test.txt')
# except Exception:
#     print('Something went wrong')
#
# # ie, it try first checks for exception if no exception then goes with else and then executes finallyz

# try:
#     f = open('text.txt')
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(f.read())
#     f.close()
# finally:
#     print('Executing finally...')

# # We can manually raise the exception

try:
    f = open('text.txt')
    if f.name == 'text.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally...')
