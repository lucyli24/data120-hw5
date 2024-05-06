def gcd(a, b):
    if b == 0:
        return a
    else:
        if a >= b:
            nw = gcd(b, a%b)
        else:
            a, b = b, a
            nw = gcd(b, a%b)
    return nw


def remove_pairs(str):
    if len(str) <= 1:
        return str

    else:
        if (str[0] == 'E' and str[1] == 'W') or \
           (str[0] == 'W' and str[1] == 'E') or \
           (str[0] == 'S' and str[1] == 'N') or \
           (str[0] == 'N' and str[1] == 'S'):
            return remove_pairs(str[2:])

        else:
            return str[0] + remove_pairs(str[1:])


def bisection_root(func, x1, x2):
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
        