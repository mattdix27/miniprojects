'''
Basic calculator with user input
'''

import string
alphabet = list(string.ascii_lowercase)


def calculator_input():
    user_input = (input("Type in your equation here: ")).replace(" ", "")
    while 1 in [c in user_input for c in alphabet]:
        user_input = (input("Type in your equation here: ")).replace(" ", "")
    equation = string_splitter(user_input)
    return calculator(equation)

def calculator(equation):
    while '(' in equation:
        i = equation.index('(')
        if i!=0 and str(equation[i-1]) not in '/*-+^':
            equation.insert(i, '*')
            i+=1
        j = equation.index(')')
        if equation.index(equation[-1]) != j and str(equation[j+1]) not in '/*-+^':
            equation.insert(j+1, '*')
        sublist = equation[i+1:j]
        equation[i] = calculator(sublist)
        del equation[i+1:j+1]
        print(equation)
    while '^' in equation:
        i = equation.index('^')
        a=float(equation[i-1])
        b=float(equation[i+1])
        equation[i] = round(a**b, 3)
        c=equation[i-1]
        d=equation[i+1]
        equation.remove(c)
        equation.remove(d)
        print(equation)
    while '/' in equation:
        i = equation.index('/')
        a=float(equation[i-1])
        b=float(equation[i+1])
        equation[i] = round(a/b, 3)
        c=equation[i-1]
        d=equation[i+1]
        equation.remove(c)
        equation.remove(d)
        print(equation)
    while '*' in equation:
        i = equation.index('*')
        a=float(equation[i-1])
        b=float(equation[i+1])
        equation[i] = round(a*b, 3)
        c=equation[i-1]
        d=equation[i+1]
        equation.remove(c)
        equation.remove(d)
        print(equation)
    while '+' in equation:
        i = equation.index('+')
        a=float(equation[i-1])
        b=float(equation[i+1])
        equation[i] = round(a+b, 3)
        c=equation[i-1]
        d=equation[i+1]
        equation.remove(c)
        equation.remove(d)
        print(equation)
    while '-' in equation:
        i = equation.index('-')
        a=float(equation[i-1])
        b=float(equation[i+1])
        equation[i] = round(a-b, 3)
        c=equation[i-1]
        d=equation[i+1]
        equation.remove(c)
        equation.remove(d)
        print(equation)
    return equation[0]

def string_splitter(input_string):   
    new_string = ''
    stringlist = []
    original = input_string
    while len(input_string):
        for i in range(len(input_string)):
            if input_string[0] == '-' and original == input_string:
                new_string+=input_string[0]
                input_string=input_string[1:]
                break
            elif input_string[0] == '-' and stringlist[-1] not in '0123456789':
                new_string+=input_string[0]
                input_string=input_string[1:]
                break
            elif input_string[0] in '0123456789':
                new_string+=input_string[0]
                if len(input_string) == 1:
                    stringlist.append(new_string)
                elif input_string[1] not in '0123456789':
                    stringlist.append(new_string)
                    new_string = ''
                input_string=input_string[1:]
                break
            elif input_string[0] not in '0123456789':
                stringlist.append(input_string[0])
                input_string=input_string[1:]
                break
            else:
                break
    return stringlist

calculator_input()