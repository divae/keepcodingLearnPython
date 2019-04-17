entrada = 10

def retrocontador(e):
    print("{},".format(e),end=" ")
    if e > 0:
        retrocontador(e-1)

retrocontador(entrada)

def sumatorio(e):
    if e > 0:
        return e + sumatorio(e-1)
    else:
        return 0

print(sumatorio(4))
    