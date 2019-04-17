def max(*l):
    if len(l) == 0:
        return 0

    m = l[0]

    for ix in range(1,len(l)):
        if l[ix] > m:
            m = l[ix]

        return m

print(max(6,2,3))