def clear():
    print("\033[23")
    
def locale(line, column):
    print("\033[{};{}H".format(line,column), end="")