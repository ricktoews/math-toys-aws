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
        fib_approx = real / SQRT_5
        fib_exact = round(fib_approx)
        diff = fib_exact - fib_approx
        row = { "nth": i, "fraction": phi, "real": real, "fib_approx": fib_approx, "fib_exact": fib_exact, "diff": diff, "[F, F*SQRT_5, L, L/SQRT_5]": [f, f * SQRT_5, l, l/SQRT_5] }
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