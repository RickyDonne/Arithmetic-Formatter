def arithmetic_arranger(problems, show_result=False):

    arranged_problem = first = second = third = four = ""
    begin = True

    size = len(problems)
    if size > 5:
        return "Error: Too many problems."

    for i in range(size):
        x = problems[i]

        x_list = x.split()

        operator = x_list[1]
        if "+" not in x_list[1] and "-" not in x_list[1]:
            return "Error: Operator must be '+' or '-'."

        x_list.remove(operator)

        a = x_list[0]
        b = x_list[1]

        if a.isdigit() == False or b.isdigit() == False:
            return "Error: Numbers must only contain digits."

        if len(a) > 4 or len(b) > 4:
            return "Error: Numbers cannot be more than four digits."

        space = max(len(a), len(b))

        dot = "-" * (space + 2)

        num1 = int(a)
        num2 = int(b)

        if begin == True:
            first += a.rjust(space + 2)
            second += operator + ' ' + b.rjust(space)
            third += dot

            if operator == "+":
                four += str(num1 + num2).rjust(space+2)
            else:
                four += str(num1 - num2).rjust(space+2)

            begin = False
        else:
            first += a.rjust(space + 2 + 4)
            second += operator.rjust(5) + ' ' + b.rjust(space)
            third += "    " + dot
            if operator == "+":
                four += "    " + str(num1 + num2).rjust(space+2)
            else:
                four += "    " + str(num1 - num2).rjust(space+2)

    if show_result == True:
        arranged_problem = (first + '\n' + second + '\n' + third + '\n' + four)
    else:
        arranged_problem = (first + '\n' + second + '\n' + third)

    return arranged_problem