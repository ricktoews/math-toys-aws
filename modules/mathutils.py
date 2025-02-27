SQRT_5 = 5**.5
PHI = (SQRT_5 + 1) / 2
BASE = 10

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 183, 191, 193, 199]

def is_relative_prime(a, b):
	[a, b] = [min(a, b), max(a, b)]
	while a > 1:
		[a, b] = [min(b%a, a), max(b%a, a)]

	return a == 1

def is_prime(p):
	_result = True
	for prime in PRIMES:
		if prime*prime > p:
			break

		if p % prime == 0:
			_result = False
			break
	return _result


def digits_to_expansion(data):
    expansion = data['expansion']
    position = data['position']
    begin_repeat = data['beginRepeat']
    
    digits = list(expansion)
    ndx = position - 1
    expansion_digits = []
    
    for i in range(len(digits)):
        expansion_digits.append(digits[ndx])
        ndx = (ndx + 1) % len(digits)
    
    return ''.join(expansion_digits)


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
