#this files run codes

from main import *
from colorama import Fore, Back, Style

functions = ["when", "log"]
operators = [">", "<", "==", ">=", "<=", "!=", "&&", "||", "!"]
mathOperators = ["+", "-", "*", "/"]
functionLine = False
operationLine = False
mathOperationLine = False
insideBracket = ""
outsideBracket = ""
rawCode = ""
error = False
whenMode = False
whenLine = 0
equalCounter = 0
resultOfStatement = False

row = 0

def run(code, line, variablesSaved):
    global functionLine, operationLine, mathOperationLine, insideBracket, outsideBracket, row, error, rawCode, whenMode, equalCounter
    rawCode = code
    row = line
    """
    #variable system, not working yet
    if variablesSaved != []:
        for i in range(0, len(variablesSaved)):
            tempCode = rawCode
            print("fuck", tempCode)
            print(variablesSaved[i])
            for n in operators + mathOperators:
                print(tempCode)
                tempCode = tempCode.split(n)[0]
            print("kys", tempCode)
            print("here dumb fuck:", tempCode)
            if variablesSaved[i][0] in tempCode:
                rawCode = rawCode.replace(variablesSaved[i][0], variablesSaved[i][1])
    """
    if "when" in code:
        code = code.split(";")
    else:
        code = code.split(":")

    outsideBracket = code[0].replace(" ", "")

    for i in range(1, len(code)):
        insideBracket += code[i]

    for i in functions:
        if outsideBracket == i:
            functionLine = True

    if not functionLine:
        for i in operators:
            if i in insideBracket:
                operationLine = True

    if not operationLine:
        for i in mathOperators:
            if i in code:
                mathOperationLine = True
    for i in code[0]:
        if i == "=":
            equalCounter += 1
    if not operationLine and not functionLine and "End" not in code and equalCounter != 1 and equalCounter != 2:
        print(Fore.RED + "Error: Line " + str(row) + ": code is neither a function code nor an operation code. Check if there "
                                             "is any"
              " syntax problems or spelling mistakes.", "Code:", Fore.YELLOW + rawCode)
        print(Style.RESET_ALL)
        error = True
        return

    if functionLine:
        functionRunner(variablesSaved)

    if operationLine:
        operationRunner(insideBracket, variablesSaved)

    if mathOperationLine:
        MathOperation(code)

    functionLine = False
    operationLine = False
    insideBracket = ""
    outsideBracket = ""

    return

def functionRunner(variablesSaved):
    global error, whenMode, resultOfStatement, whenLine, insideBracket
    if functionLine:
        varBracketCounter = 0
        for n in insideBracket:
            if n == "{":
                for i in range(0, len(insideBracket)):
                    if insideBracket[i] == "{" or insideBracket[i] == "}":
                        varBracketCounter += 1
        if varBracketCounter % 2 == 0:
            print(insideBracket.replace("{", "").replace("}", ""))
        else:
            print(Fore.RED + 'Error: Line ' + str(row) + ': syntax error: "{" and "}" is not in pair.', "Code:", Fore.YELLOW + rawCode)
            print(Style.RESET_ALL)
            error = True
            return

        if outsideBracket.replace(" ", "") == "log":


            operationInLog = False
            for i in operators:
                if i in insideBracket:
                    operationInLog = True
            counter = 0
            for i in range(len(insideBracket)):
                if insideBracket[i] == '"':
                    counter += 1
            if insideBracket[0] == '"':
                if counter % 2 == 0:
                    print(insideBracket.split('"')[1])
                else:
                    print(Fore.RED + 'Error: Line ' + str(row) + ': syntax error: {"} is not in pair.', "Code:", Fore.YELLOW + rawCode)
                    print(Style.RESET_ALL)
                    error = True
                    return
            elif ("+" in insideBracket or "-" in insideBracket or "*" in insideBracket or "/" in insideBracket or "=" in insideBracket):
                if counter % 2 != 0:
                    print(Fore.RED + 'Error: Line ' + str(row) + ': syntax error: {"} is not in pair.', "Code:", Fore.YELLOW + rawCode)
                    print(Style.RESET_ALL)
                    error = True
                    return
                elif operationInLog == False:
                    output = MathOperation(insideBracket)
                    if not error and len(output) >= 2:
                        if 48 <= ord(output[1]) <= 57:
                            output = float(output)
                            if int(output) == output:
                                log(int(output))
                                return
                            else:
                                log(output)
                                return
                        else:
                            log(output)
                            return
                else:
                    output = operationRunner(insideBracket, variablesSaved)
                    print(output)
            else:
                errorChecker = True
                for i in operators:
                    if i in insideBracket:
                        print(insideBracket)
                        return

                if errorChecker:
                    print(Fore.RED + 'Error: syntax error: {"} not found. Check if you spelt some variable wrong or '
                                     'extra spacing'
                                     ' after {:} at Line ' + str(row) + ". Code:", Fore.YELLOW + rawCode)
                    print(Style.RESET_ALL)
                    error = True
                return

        resultOfStatement = False
        if outsideBracket.replace(" ", "") == "when" and not whenMode:
            whenMode = True
            whenLine += 1
            statement = insideBracket.split(":")[0]
            #print(insideBracket)
            #thenStatement =
            resultOfStatement = operationRunner(statement, variablesSaved)
            #print(resultOfStatement)
            if resultOfStatement == False:
                return
            #else:
                #print('here')
            return

        if whenMode:
            if resultOfStatement:
                #print(rawCode)
                #print("here fucker", rawCode.split(":")[0] + ":" + rawCode.split(":")[1])
                print("statement result:", resultOfStatement)
                if resultOfStatement == True:
                    when(resultOfStatement, rawCode.split(":")[0] + ":" + rawCode.split(":")[1])
                return
            else:
                whenMode = False
            return

    return


#variables[0][1] = variables[0][1].replace('"', "")

def operationRunner(content, variablesSaved):
    global operators, main
    output = None
    if "&&" in content:
        output_ = []

        variables = content.split("&&")
        for i in range(len(variables)):
            if variables[i].isspace() or variables[i] == "":
                print(Fore.RED + 'Error: operator error: {&&} operator requires two conditional statement. '
                                 'Only one is found. '
                                 'Line ' + str(row) + ". Code:", Fore.YELLOW + rawCode)
                print(Style.RESET_ALL)
                return

        output = CAnd(doubleStatementRunner(variables))
    elif "||" in content:
        variables = content.split("||")
        output = COr(doubleStatementRunner(variables))

    elif "==" in content:
        variables = content.split("==")
        variables[0] = variables[0].replace('"', "").replace('\n', "")
        variables[1] = variables[1].replace('"', "").replace('\n', "")
        checkMath(variables)

        type_ = 0
        for i in variables:
            for n in i:
                if not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and ord(n) != 46 and ord(n) != 47:
                    type_ = 1
        if type_ == 0:
            output = eq(float(variables[0]), float(variables[1]))
        else:
            output = eq(str(variables[0]), str(variables[1]))

    elif "!=" in content:
        variables = content.split("!=")
        variables[0] = variables[0].replace('"', "").replace('\n', "")
        variables[1] = variables[1].replace('"', "").replace('\n', "")
        checkMath(variables)
        type_ = 0
        for i in variables:
            for n in i:
                if not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and ord(n) != 46 and ord(n) != 47:
                    type_ = 1
        if type_ == 0:
            output = neq(float(variables[0]), float(variables[1]))
        else:
            output = neq(str(variables[0]), str(variables[1]))

    elif ">=" in content:
        variables = content.split(">=")
        variables[0] = variables[0].replace('"', "")
        variables[1] = variables[1].replace('"', "")
        checkMath(variables)

        # print(variables)
        output = lteq(float(variables[0]), float(variables[1]))

    elif "<=" in content:
        variables = content.split("<=")
        variables[0] = variables[0].replace('"', "")
        variables[1] = variables[1].replace('"', "")
        checkMath(variables)

        # print(variables)
        output = steq(float(variables[0]), float(variables[1]))

    elif ">" in content:
        variables = content.split(">")
        variables[0] = variables[0].replace('"', "")
        variables[1] = variables[1].replace('"', "")
        checkMath(variables)

        # print(variables)
        output = lt(float(variables[0]), float(variables[1]))

    elif "<" in content:
        variables = content.split("<")
        variables[0] = variables[0].replace('"', "")
        variables[1] = variables[1].replace('"', "")
        checkMath(variables)

        # print(variables)
        output = st(float(variables[0]), float(variables[1]))

        #print("here you dumbass", CAnd(variables[0], variables[1]))
    else:
        print(Fore.RED + "Error: Line", row,
              ": when-statement invalid. Code:", rawCode)
        print(Style.RESET_ALL)

    if "!" in content:
        output = not output
    return output

def checkMath(variables):
    if "+" in variables[0] or "-" in variables[0] or "*" in variables[0] or "/" in variables[0]:
        variables[0] = MathOperation(variables[0])
    if "+" in variables[1] or "-" in variables[1] or "*" in variables[1] or "/" in variables[1]:
        variables[1] = MathOperation(variables[1])

def MathOperation(expression):
    global error, rawCode
    output = ""
    if "+" in expression:
        expression = expression.split("+")
        type_ = 0
        for i in expression:
            for n in i:
                if not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and ord(n) != 46 and ord(n) != 47:
                    type_ = 1
        output = plus(expression, type_)
    if "-" in expression:
        expression = expression.split("-")
        type_ = 0
        for i in expression:
            for n in i:
                if not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and ord(n) != 46 and ord(n) != 47:
                    type_ = 1
        output = minus(expression, type_)
    if "*" in expression:
        expression = expression.split("*")
        expressionErrorCheckerException = expression
        for o in range(0, len(expressionErrorCheckerException)):
            expressionErrorCheckerException[o] = expressionErrorCheckerException[o].replace("True", "").replace("False", "")
            for n in operators:
                expressionErrorCheckerException[o] = expressionErrorCheckerException[o].replace(n, "")
        for i in expressionErrorCheckerException:
            for n in i:
                if not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and ord(n) != 46 and ord(n) != 47:
                    print(Fore.RED + "Error: Line" + str(row) + ": expecting int or float with * operator, received boolean or string. Check is there's any unwanted symbols. Code:", Fore.YELLOW + rawCode)
                    print(Style.RESET_ALL)
                    error = True
                    return
        output = times(expression)
    if "/" in expression:
        expression = expression.split("/")
        expressionErrorCheckerException = expression
        for o in range(0, len(expressionErrorCheckerException)):
            expressionErrorCheckerException[o] = expressionErrorCheckerException[o].replace("True", "").replace("False", "")
            for n in operators:
                expressionErrorCheckerException[o] = expressionErrorCheckerException[o].replace(n, "")
        for i in expressionErrorCheckerException:
            for n in i:
                if not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and ord(n) != 46 and ord(n) != 47:
                    print(Fore.RED + "Error: Line" + str(row) + ": expecting int or float with / operator, received boolean or string. Check if there's any unwanted symbols. Code:", Fore.YELLOW + rawCode)
                    print(Style.RESET_ALL)
                    error = True
                    return
        output = divide(expression)

    return output

def doubleStatementRunner(variables):
    output_ = []
    for i in range(0, len(variables)):
        variables[i] = variables[i].replace('"', "").replace('\n', "")
        if "==" in variables[i]:
            variables[i] = variables[i].split("==")
            checkMath(variables[i])
            type_ = 0
            for o in variables[i]:
                for n in o:
                    if not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and ord(n) != 47:
                        type_ = 1

            # print(variables)
            if type_ == 0:
                output_.append(eq(float(variables[i][0]), float(variables[i][1])))
            else:
                output_.append(eq(str(variables[i][0]), str(variables[i][1])))

        elif "!=" in variables[i]:
            variables[i] = variables[i].split("!=")
            checkMath(variables[i])
            type_ = 0
            for o in variables[i]:
                for n in o:
                    if not 48 <= ord(n) <= 57 and ord(n) != 42 and ord(n) != 43 and ord(n) != 45 and ord(n) != 47:
                        type_ = 1

            # print(variables)
            if type_ == 0:
                output_.append(neq(float(variables[i][0]), float(variables[i][1])))
            else:
                output_.append(neq(str(variables[i][0]), str(variables[i][1])))
        elif ">=" in variables[i]:
            variables[i] = variables[i].split(">=")
            checkMath(variables[i])

            # print(variables)
            output_.append(lteq(float(variables[i][0]), float(variables[i][1])))

        elif "<=" in variables[i]:
            variables[i] = variables[i].split("<=")
            checkMath(variables[i])

            # print(variables)
            output_.append(steq(float(variables[i][0]), float(variables[i][1])))

        elif ">" in variables[i]:
            variables[i] = variables[i].split(">")
            checkMath(variables[i])

            # print(variables)
            output_.append(lt(float(variables[i][0]), float(variables[i][1])))

        elif "<" in variables[i]:
            variables[i] = variables[i].split("<")
            checkMath(variables[i])

            # print(variables)
            output_.append(st(float(variables[i][0]), float(variables[i][1])))
        else:
            if variables[i] == 'False':
                output_.append(False)
            if variables[i] == 'True':
                output_.append(True)
    return output_
