def hello_func():
    print('Hello hello World')


hello_func()


def hello_func():
    return 'Hello hello World'


print(hello_func())
print(hello_func().upper())


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('john', 'Kavitha', subject1='Maths', subject2='Science')

course = ['Maths', 'Art']
name = {'name1': 'john', 'name2': 'Kavitha'}


student_info(*course, **name)



