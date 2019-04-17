entrada = 10

def counter(e):
    print("{},".format(e),end=" ")
    if e > 0:
        counter(e-1)

counter(entrada)

