#this file storage the code for the operations

from colorama import Fore, Style
import syntax


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


def plus(x, type_):
    if type_ == 0:
        output = 0
        for o in x:
            if "-" in o:
                subExpression = o.split("-")
                type_ = 0
                for i in subExpression[0]:
                    for n in i:
                        if not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and ord(
                                n) != 46 and ord(
                                n) != 47:
                            type_ = 1
                type__ = 0
                for i in subExpression[1]:
                    for n in i:
                        if not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and ord(
                                n) != 46 and ord(
                                n) != 47:
                            type__ = 1
                if type_ != type__:
                    print(Fore.RED + "Error: Line", syntax.row,
                          ": comparing numeral variables with string variables. Code:", Fore.YELLOW + syntax.rawCode)
                    print(Style.RESET_ALL)
                    return
                else:
                    o = minus(subExpression, type_)
            if "*" in o:
                subExpression = o.split("*")
                o = times(subExpression)
            if "/" in o:
                subExpression = o.split("/")
                o = divide(subExpression)
            output += float(o)
    else:
        output = ""
        for i in x:
            output += i
    return str(output)


def minus(x, type_):
    if type_ == 0:
        for h in range(0, len(x)):
            index_ = h
            if "(" in x[h]:
                everySubExpression(h, x)
        for i in range(0, len(x)):
            if "+" in x[i]:
                subExpression = x[i].split("+")
                x[i] = plus(subExpression)
            if "*" in x[i]:
                subExpression = x[i].split("*")
                x[i] = times(subExpression)
            if "/" in x[i]:
                subExpression = x[i].split("/")
                x[i] = divide(subExpression)
        output = float(x[0])
        for i in range(1, len(x)):
            output -= float(x[i])
    else:
        output = x[0]
        if x[1] in x[0]:
            output = output.replace(x[1], "")
        else:
            print(Fore.RED + "Error: Line", syntax.row,
                  ": content does not exist. Code:", Fore.YELLOW + syntax.rawCode)
            print(Style.RESET_ALL)
    return str(output)


def times(x):
    output = 1
    for h in range(0, len(x)):
        index_ = h
        if "(" in x[h]:
            for i in range(h, len(x)):
                if "+" in x[i]:
                    subExpression = x[i].split("+")
                    x[i] = plus(subExpression)
                if "-" in x[i]:
                    subExpression = x[i].split("-")
                    type_ = 0
                    for i in subExpression[0]:
                        for n in i:
                            if not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and ord(
                                    n) != 46 and ord(
                                n) != 47:
                                type_ = 1
                    type__ = 0
                    for i in subExpression[1]:
                        for n in i:
                            if not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and ord(
                                    n) != 46 and ord(
                                n) != 47:
                                type__ = 1
                    if type_ != type__:
                        print(Fore.RED + "Error: Line", syntax.row,
                              ": comparing numeral variables with string variables. Code:",
                              Fore.YELLOW + syntax.rawCode)
                        print(Style.RESET_ALL)
                        return
                    else:
                        x[i] = minus(subExpression, type_)
                if "*" in x[i]:
                    subExpression = x[i].split("*")
                    x[i] = times(subExpression)
                if "/" in x[i]:
                    subExpression = x[i].split("/")
                    x[i] = divide(subExpression)
    for o in x:
        if "+" in o:
            subExpression = o.split("-")
            o = plus(subExpression)
        if "-" in o:
            subExpression = o.split("-")
            type_ = 0
            for i in subExpression[0]:
                for n in i:
                    if not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and ord(
                            n) != 46 and ord(
                        n) != 47:
                        type_ = 1
            type__ = 0
            for i in subExpression[1]:
                for n in i:
                    if not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and ord(
                            n) != 46 and ord(
                        n) != 47:
                        type__ = 1
            if type_ != type__:
                print(Fore.RED + "Error: Line", syntax.row,
                      ": comparing numeral variables with string variables. Code:", Fore.YELLOW + syntax.rawCode)
                print(Style.RESET_ALL)
                return
            else:
                o = minus(subExpression, type_)
        if "/" in o:
            subExpression = o.split("/")
            o = divide(subExpression)
        output *= float(o)
    return str(output)


def divide(x):
    output = float(x[0]) ** 2
    for o in x:
        if "+" in o:
            subExpression = o.split("+")
            o = plus(subExpression)
        if "-" in o:
            subExpression = o.split("-")
            type_ = 0
            for i in subExpression[0]:
                for n in i:
                    if not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and ord(
                            n) != 46 and ord(
                        n) != 47:
                        type_ = 1
            type__ = 0
            for i in subExpression[1]:
                for n in i:
                    if not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and ord(
                            n) != 46 and ord(
                        n) != 47:
                        type__ = 1
            if type_ != type__:
                print(Fore.RED + "Error: Line", syntax.row,
                      ": comparing numeral variables with string variables. Code:", Fore.YELLOW + syntax.rawCode)
                print(Style.RESET_ALL)
                return
            else:
                o = minus(subExpression, type_)
        if "*" in o:
            subExpression = o.split("*")
            o = times(subExpression)
        output /= float(o)
    return str(output)


def when(x, code):
    if x:
        syntax.outsideBracket = code.split(":")[0]
        syntax.insideBracket = code.split(":")[1]
        syntax.run(code, syntax.row)

def everySubExpression(h, x):
    wantedOpenBracket = 0
    wantedCloseBracket = 0
    for i in range(h, len(x)):
        if wantedOpenBracket == 0:
            for n in range(0, len(x[i]) - 1):
                print("x[i]:", x[i])
                print("n:", n)
                print("i:", i)
                if x[i][n] == "(":
                    x[i] = syntax.replacer(x[i], "", n)
                    wantedOpenBracket = 1
        for n in range(0, len(x[i])):
            if x[i][n] == ")":
                wantedCloseBracket = n
        if wantedCloseBracket != 0:
            x[i] = syntax.replacer(x[i], "", wantedCloseBracket)
    for i in range(h, len(x)):
        if "+" in x[i]:
            subExpression = x[i].split("+")
            x[i] = plus(subExpression)
        if "-" in x[i]:
            subExpression = x[i].split("-")
            type_ = 0
            for t in subExpression[0]:
                for n in t:
                    if (not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and
                            ord(n) != 46 and ord(n) != 47):
                        type_ = 1
            type__ = 0
            for t in subExpression[1]:
                for n in t:
                    if (not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and
                            ord(n) != 46 and ord(n) != 47):
                        type__ = 1
            if type_ != type__:
                print(Fore.RED + "Error: Line", syntax.row,
                      ": comparing numeral variables with string variables. Code:",
                      Fore.YELLOW + syntax.rawCode)
                print(Style.RESET_ALL)
                return
            else:
                x[i] = minus(subExpression, type_)
        if "*" in x[i]:
            subExpression = x[i].split("*")
            x[i] = times(subExpression)
        if "/" in x[i]:
            subExpression = x[i].split("/")
            x[i] = divide(subExpression)