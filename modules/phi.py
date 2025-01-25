from mathconst import SQRT_5

def lucas(nth: int, a: int, b: int):
    for i in range(1, nth + 1):
        result = a
        [a, b] = [b, a + b]
    return result


def fib(nth: int):
    [a, b] = [1, 1]
    for i in range(1, nth + 1):
        result = a
        [a, b] = [b, a+b]
    return result


def get_phi(max: int):
    rows = []
    for i in range(1, max+1):
        [f, l] = [fib(i), lucas(i, 1, 3)]
        phi = "(%d V5 + %d) / 2" % (f, l)
        real = (f * SQRT_5 + l) / 2
        a_sqrt_5 = f * SQRT_5
        b = l
        diff = a_sqrt_5 - b
        row = { 
            "nth": i,
            "fraction": phi,
            #"real": real,
            "[a*V5, b]": [a_sqrt_5, b],
            "diff": diff,
            "[F, L]": [f, l]
        }
        rows.append(row)
    return rows


def phi_a(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return phi_a(n-2) + phi_a(n-1)


def phi_first_n(n):
    _p = 1
    _phi_powers = []
    while _p <= n:
        _a = phi_a(_p)
        _b = fib(_p)
        _phi_str = '(%d + %d /5) / 2' % (_a, _b)
        _phi_powers.append(_phi_str)
        _p += 1
    return _phi_powers
