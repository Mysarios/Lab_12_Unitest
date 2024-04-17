import math
def calc(a,b,sym):
    if sym == '+':
        return a+b
    if sym == '-':
        return a-b
    if sym == '*':
        return a*b
    if sym == '/':
        if b != 0:
            return a/b
        else:
            return "Error"
    if sym == "**":
        return a**b

    return "Error"
def calc_dif(a,sym):
    if sym == "^(1/2)":
        if a>=0:
            return a**(1/2)
        else:
            return "Error"
    if sym == "!":
        return math.factorial (a)
    return "Error"