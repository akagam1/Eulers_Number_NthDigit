def factorial(n):
    if n == 0:
        return(1)
    else:
        return(n*factorial(n-1))

def euler(m):
    e = 1
    for x in range(1,21):
        e = e + 1/factorial(x)
        #Construct a formatted string
        fmt_string = '%.' + str(m) + 'f'
    #Return e
    return fmt_string % e

print(euler(int(input("Number of decimals: "))))







