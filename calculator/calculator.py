def calculator():
    equation = input("enter your equation to solve: ")
    valid_chars = ["1", "2", "3", "0", "4", "5",
                   "6", "7", "8", "9", "+", "-", "*", "/"]
    has_all = all([char not in [*equation] for char in valid_chars])
    print(has_all)
    print(equation)


calculator()
