def gcd(a, b):
    '''
    Finding the greatest common divisor of two natural numbers
    '''
    if b == 0:
        return a
    if a >= b:
        nw = gcd(b, a%b)
    else:
        a, b = b, a
        nw = gcd(b, a%b)
    return nw


def remove_pairs(path):
    '''
    Take in a direction string path, and return a direction
    string such that all “turnaround pairs” have been removed
    '''
    if len(path) <= 1:
        return path
    if (path[0] == 'E' and path[1] == 'W') or \
        (path[0] == 'W' and path[1] == 'E') or \
        (path[0] == 'S' and path[1] == 'N') or \
        (path[0] == 'N' and path[1] == 'S'):
        return remove_pairs(path[2:])
    return path[0] + remove_pairs(path[1:])


def bisection_root(func, x1, x2):
    '''
    Use bisection method to find a root (zero or x-intercept) of a function
    '''
    f1, f2 = func(x1), func(x2)
    if f1*f2 > 0:
        raise ValueError
    if abs(f1) <= 0.0000001:
        return x1
    elif abs(f2) <= 0.0000001:
        return x2
    else:
        x_mid = (x1+x2)/2
        y_mid = func(x_mid)

        if y_mid * f1 < 0:
            return bisection_root(func, x1, x_mid)
        elif y_mid * f2 < 0:
            return bisection_root(func, x_mid, x2)
        else:
            raise ValueError("The bisection method failed to find a root.")
        