def maxlen(operation):
    return len(max(operation.split(" "), key=len))


def spaceCalc(problem):
    if len(str(eval(problem))) == len(problem.split(" ")[0]):
        print(len(str(eval(problem))), len(problem.split(
            " ")[0]), len(problem.split(" ")[2]), "space 1")
        space = 2
    elif len(str(eval(problem))) == len(problem.split(" ")[2]):
        space = 2
    else:  
        print(len(str(eval(problem))), len(problem.split(
            " ")[0]), len(problem.split(" ")[2]), "space 2")
        space = 1
    return space


def checkSyntax(data):
    if len(data) > 5:
        return "Error: Too many problems."
    for problem in data:
        if not problem.split(" ")[0].isnumeric() or not problem.split(" ")[2].isnumeric():
            return "Error: Numbers must only contain digits."
        if len(problem.split(" ")[0]) > 4 or len(problem.split(" ")[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if "*" == problem.split(" ")[1] or "/" == problem.split(" ")[1]:
            return "Error: Operator must be '+' or '-'."
    return False


def arithmetic_arranger(problems, calc=False):
    arranged_problems = ""
    if checkSyntax(problems):
        return checkSyntax(problems)
    # if len(problems) > 5:
    #     arranged_problems = "Error: Too many problems."
    #     return arranged_problems

    # FOR PRINTING TOP LINE NUMBERS
    for problem in problems:
        arranged_problems = arranged_problems + \
            problem.split(" ")[0].rjust(maxlen(problem)+2) + "    "
    arranged_problems = arranged_problems[:-4] + "\n"

    # FOR PRINTING OPERATORS AND DOWN NUMBERS
    for problem in problems:
        arranged_problems = arranged_problems + \
            problem.split(
                " ")[1] + problem.split(" ")[2].rjust(maxlen(problem)+1) + "    "
    arranged_problems = arranged_problems[:-4] + "\n"

    # FOR PRINTING LINES
    for problem in problems:
        arranged_problems = arranged_problems + \
            "-"*(maxlen(problem)+2) + "    "
    arranged_problems = arranged_problems[:-4]

    # FOR PRINTING BOTTOM LINE NUMBERS
    if calc == True:
        arranged_problems = arranged_problems + "\n"
        for problem in problems:
            space = spaceCalc(problem)
            arranged_problems = arranged_problems + \
                str(eval(problem)).rjust(
                    len(str(eval(problem)))+space) + "    "
        arranged_problems = arranged_problems[:-4]

    print(arranged_problems)
    return arranged_problems
