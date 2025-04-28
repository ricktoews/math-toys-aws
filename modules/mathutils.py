from primes import primes
SQRT_5 = 5**.5
PHI = (SQRT_5 + 1) / 2
BASE = 10

def is_relative_prime(a, b):
	[a, b] = [min(a, b), max(a, b)]
	while a > 1:
		[a, b] = [min(b%a, a), max(b%a, a)]

	return a == 1

def is_prime(p):
	_result = True
	for prime in primes:
		if prime*prime > p:
			break

		if p % prime == 0:
			_result = False
			break
	return _result


# Example:
#   digits: '076923', ndx = 1
#   returns '769230'
# This function is called only when the denominator is a prime number with a repeating period.
# The digits string is the period for the minimum numerator containing this group of digits.
# Example, for the 13ths, there are two groups '076923' (1/13) and '153846' (2/13).
# For 10/13, the decimal expansion is .769230... So the digits are '076023', and the ndx is 1,
# since the expansion for this fraction uses the '076923' group but starts at zero-based ndx 1.
def digits_to_expansion(digits, ndx):
    period_digits = f"{digits[ndx:]}{digits[:ndx]}"
    return period_digits


def divide(num, denom):
    digits = []
    numerators = {}
    position = 1

    while num > 0 and num not in numerators:
        numerators[num] = position
        position += 1
        digit = (num * BASE) // denom
        digits.append(digit)
        num = num * BASE - digit * denom

    begin_repeat = numerators[num] if num > 0 else -1  # num is 0 if decimal resolves
    result = {
        'expansion': ''.join(map(str, digits)),
        'expansionNumerators': numerators,
        'beginRepeat': begin_repeat
    }

    return result
