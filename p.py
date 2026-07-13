# a=10
# b=10
# print(a/b)

# try:
#     a=int(input('first number='))
#     b=int(input('second number='))
#     print(a/b)
# except ZeroDivisionError:
#     print('division by zero is not allowed')
# except ValueError:
#     print('please enter a valid number')

# try:
#     li=[1,2,3]
#     a=int(input('enter the index='))
#     print(li[a])
# except IndexError:
#     print('pls enter a valid index')
# except ValueError  as e:
#     print(e)


'''
num=0-->zeroexception
-ve  negatuveexception

+ve  success
'''

class zeroexception(Exception):
    pass
class negativeexception(Exception):
    pass

try:
    num=int(input('enter your number'))
    if num==0:
        raise zeroexception
    elif num<0:
        raise negativeexception
    else:
        print('success')
except zeroexception:
    print('enter a positive number')
except negativeexception:
    print('enter a positive number')   