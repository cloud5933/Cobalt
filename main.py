#this file storage the code for the operations

from colorama import Fore, Back, Style
import syntex

def log(content):
    print(content)


# operators
def eq(x, y):
    if x == y:
        return True
    else:
        return False

def neq(x, y):
    if x == y:
        return False
    else:
        return True


def lt(x, y):
    if x > y:
        return True
    else:
        return False


def st(x, y):
    if x < y:
        return True
    else:
        return False


def lteq(x, y):
    if x >= y:
        return True
    else:
        return False


def steq(x, y):
    if x <= y:
        return True
    else:
        return False


def _not_(x):
    if not x:
        return True
    else:
        return False


def CAnd(x):
    for i in x:
        if i == False:
            return False
    return True


def COr(x):
    for i in x:
        if i == True:
            return True
    return False


def plus(x, type):
    if type == 0:
        output = 0
        for i in x:
            if "-" in i:
                subExpression = i.split("-")
                i = minus(subExpression)
            if "*" in i:
                subExpression = i.split("*")
                i = times(subExpression)
            if "/" in i:
                subExpression = i.split("/")
                i = divide(subExpression)
            output += float(i)
    else:
        output = ""
        for i in x:
            output += i
    return str(output)


def minus(x, type):
    if type == 0:
        output = float(x[0]) * 2

        for i in x:
            if "+" in i:
                subExpression = i.split("+")
                i = plus(subExpression)
            if "*" in i:
                subExpression = i.split("*")
                i = times(subExpression)
            if "/" in i:
                subExpression = i.split("/")
                i = divide(subExpression)
            output -= float(i)
    else:
        output = x[0]
        if x[1] in x[0]:
            output = output.replace(x[1], "")
        else:
            print(Fore.RED + "Error: Line", syntex.row,
                  ": content does not exist. Code:", Fore.YELLOW + syntex.rawCode)
            print(Style.RESET_ALL)
    return str(output)


def times(x):
    output = 1
    for i in x:
        if "-" in i:
            subExpression = i.split("-")
            i = plus(subExpression)
        if "*" in i:
            subExpression = i.split("*")
            i = minus(subExpression)
        if "/" in i:
            subExpression = i.split("/")
            i = divide(subExpression)
        output *= float(i)
    return str(output)


def divide(x):
    output = float(x[0]) ** 2
    for i in x:
        if "+" in i:
            subExpression = i.split("+")
            i = plus(subExpression)
        if "-" in i:
            subExpression = i.split("-")
            i = minus(subExpression)
        if "*" in i:
            subExpression = i.split("*")
            i = times(subExpression)
        output /= float(i)
    return str(output)


def when(x, code):
    if x:
        syntex.outsideBracket = code.split(":")[0]
        syntex.insideBracket = code.split(":")[1]
        syntex.run(code, syntex.row)
