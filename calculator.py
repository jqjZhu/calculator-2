"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True: 
    user_input = input('Enter your equation: ')
    tokens = user_input.split(' ')
    operator, *nums = tokens

    if 'q' in tokens:
        print('You will exit.')
        break

    num1 = nums[0]
    num2 = nums[1]

    result = None

    if operator == '+':
        result = add(float(num1), float(num2))

    if operator == '-':
        result = subtract(float(num1), float(num2))

    if operator == '*':
        result = multiply(float(num1), float(num2))

    if operator == '/':
        result = divide(float(num1), float(num2))

    if operator == 'square':
        result = square(float(num1))

    if operator == 'cube':
        result = cube(float(num1))

    if operator == 'pow':
        result = power(float(num1), float(num2))

    if operator == 'mod':
        result = mod(float(num1), float(num2))

    print(result)

