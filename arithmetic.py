# a = float(input('Введите первое число: '))
# b = float(input('Введите второе число: '))
# i = input('Що зробити?')

# def just_print(a,b,i):
#     print(a)
#     print(b)
#     print(i)

# def arithmetic(a,b,i):
#     c = 0
#     if(i == '/'):
#        c = a / b
#        print(c)
#     elif(i == '*'):
#        c = a * b
#        print(c)
#     elif(i == '+'):
#        c = a + b
#        print(c)
#     elif(i == '-'):
#        c = a - b
#        print(c)
#     else:
#         print('Неизвестная операция!')

# arithmetic(a,b,i)
arg1 = int(input())
arg2 = int(input())
op = input()

def arithmetic(arg1, arg2, op):
    if op == '+':
        return arg1 + arg2
    elif op == '-':
        return arg1 - arg2
    elif op == '*':
        return arg1 * arg2
    elif op == '/':
        return arg1 / arg2
    else:
        return "Неизвестная операция"

import unittest


class ArithmeticTestCase(unittest.TestCase):

    def test_plus(self):

        self.assertEqual(arithmetic(3, 4, '+'), 7)

    def test_minus(self):

        self.assertEqual(arithmetic(3, 4, '-'), -1)

    def test_multiply(self):

        self.assertEqual(arithmetic(3, 4, '*'), 12)

    def test_divide(self):

        self.assertEqual(arithmetic(3, 4, '/'), 3/4)

    def test_unknown(self):

        self.assertEqual(arithmetic(3, 4, '.'), "Неизвестная операция")


if __name__ == "__main__":
    print(unittest.main())

    



        

    