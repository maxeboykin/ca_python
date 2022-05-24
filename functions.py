def add_three(num1, num2, num3):
    sum_three = num1 + num2 + num3
    return sum_three


sum_output = add_three(2, 4, 6)

print(sum_output)


def greetings(language):
    if language == 'Spanish':
        greeting = 'Hola'

    elif language == 'English':
        greeting = 'Hello'

    elif language == 'French':
        greeting = 'Bonjour'

    print(greeting)


greetings('French')


def factorial(num):
    call_stack = []
    if num == 1:
        print('base case reached! Num is 1.')
        return 1
    else:
        call_stack.append({'input': num})
        print('call stack: ', call_stack)
        return num * factorial(num - 1)


res = factorial(5)
print(res)

add_two = lambda x: x + 2  #  lambda functions are good for quick one ine func or when we want to combine with map filter or apply functions
lambdaResult = add_two(5)
print(lambdaResult)

