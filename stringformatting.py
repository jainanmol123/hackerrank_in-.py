def print_formatted(number):
    w=len("{0:b}".format(n))
    for i in range(1,number+1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i,w=w))
    # your code goes here
