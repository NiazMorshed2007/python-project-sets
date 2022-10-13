import re
def arithmetic_arranger(problems, solve = False):
    arranged_problems = ""
    datasets = []
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    if len(problems) <= 5:
        for problem in problems:
            sp = problem.split()
            if re.match('^[0-9]*$', sp[0] + sp[-1]):
                if sp[1] == "+" or sp[1] == "-":
                    if len(sp[0]) > 4 or len(sp[-1]) > 4:
                        return "Error: Numbers cannot be more than four digits."
                    else:
                        largest_operand = max([int(sp[0]), int(sp[-1])])
                        dict = {
                            "fo": sp[0],
                            "sbf": 2 if str(largest_operand) == sp[0] else 2 + len(str(largest_operand)) - len(sp[0]),
                            "operator": sp[1],
                            "lo": sp[-1],
                            "sbl": 1 if str(largest_operand) == sp[-1] else 1 + len(str(largest_operand)) - len(sp[-1])
                        }
                        # print(datasets)
                        spacer = 4*" " if problem != problems[-1] else ""

                        line1 += dict["sbf"]*" " + dict["fo"] + spacer
                        line2 += dict["operator"] + dict["sbl"]*" " + dict["lo"] + spacer
                        computed = int(dict["fo"]) + int(dict["lo"]) if dict["operator"] == "+" else int(dict["fo"]) - int(dict["lo"])
                        line3 += len(dict["operator"] + dict["sbl"]*" " + dict["lo"])*"-" + spacer
                        if solve:
                            line4 += (len(dict["operator"] + dict["sbl"]*" " + dict["lo"]) - len(str(computed)))*" " + str(computed) + spacer
                else:
                    return "Error: Operator must be '+' or '-'."
            else:
                return "Error: Numbers must only contain digits."
        else:
            return "Error: Too many problems."

    if solve:
        return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    else:
        return line1 + "\n" + line2 + "\n" + line3


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))