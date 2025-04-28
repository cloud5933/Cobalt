#this file reads code and send it to "syntax.py" line by line (I know I spelt syntex wrong)

import syntax
from colorama import Fore

fileDirectory = "cobaltTestFile.cb"  #the .cb file is the file saving the Cobalt program
CBfile = open(fileDirectory, "r")
codes = CBfile.readlines()
whenLine = 0
variablesSaved = []

line = 0
for i in codes:
    line += 1
    i = i.replace("\n", "")
    if not syntax.error and not i.isspace() and not i == "":
        equalCounter = 0
        for n in i:
            if n == "=":
                equalCounter += 1

        if equalCounter == 1:
            variablesSaved.append([i.replace(" ", "").split("=")[0], i.replace(" ", "").split("=")[1]])

        if i == "End":
            if syntax.whenMode:
                syntax.whenMode = False
            else:
                syntax.error = True
                print(Fore.RED + "Syntax Error: Found statement {End} but {when} statement is not found. Line",
                      line, Fore.RESET)
        #print("when mode:", syntex.whenMode)
        if syntax.whenMode:
            whenLine += syntax.whenLine
            """
            """
            if whenLine == 1 and i[0] != " ":
                syntax.error = True
                print(Fore.RED + "Indentation Error: Found statement {when} statement but indention is not found. Line",
                      line, Fore.RESET)
                break
            if i[0] != " ":
                syntax.whenMode = False
                whenLine = 0
                syntax.run(i, line)

            if not syntax.resultOfStatement:
                continue
            else:
                syntax.run(i, line)
                continue
        else:
            syntax.run(i, line)

input("Press Enter To Exit: ")
