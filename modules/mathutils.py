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


def digits_to_expansion(data):
    expansion = data.get('expansion', '')
    position = data.get('position', -1)
    begin_repeat = data.get('beginRepeat', -1)
    
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
