from mathutils import divide, digits_to_expansion
from primes import primes

# Note on digits vs expansion:
# The digits of the periods for the 7ths are 142857.
# Each n/7 fraction uses these digits, regardless of which one the period begins with:
# 1/7 = .142857... (Starts at position 1. So digits = '142857', expansion = '142857'.)
# 2/7 = .285714... (Starts at position 3. So digits = '142857', expansion = '285714'.)
# &c.
def get_expansions(denom):
    is_prime = denom in primes
    by_numerator = {}
    by_expansion = {}
    
    for num in range(1, denom):
        # Check each numerator to see if it's already been calculated.
        if num in by_numerator:
            by_numerator[num]['expansion'] = digits_to_expansion(by_numerator[num])
            continue

        # Calculate the expansion if it hasn't already been done
        result = divide(num, denom)
        expansion = result.get('expansion', '')
        expansion_numerators = result.get('expansionNumerators', {})

        by_numerator[num] = {
            'expansion': expansion,
            'position': expansion_numerators[num],
            'beginRepeat': result.get('beginRepeat', -1)
        }
        if expansion not in by_expansion:
            by_expansion[expansion] = []

        by_expansion[expansion].append({
            'numerator': num,
            'position': expansion_numerators[num],
            'beginRepeat': result.get('beginRepeat', -1)
        })

        # This block is only for prime numbers
        if not is_prime:
            continue

        for n in expansion_numerators.keys():
            if n == num:
                continue

            by_expansion[expansion].append({
                'numerator': n,
                'position': expansion_numerators[n],
                'beginRepeat': 1
            })
            by_numerator[int(n)] = {
                'expansion': expansion,
                'position': expansion_numerators[int(n)],
                'beginRepeat': 1
            }

    return {'byExpansion': by_expansion, 'byNumerator': by_numerator}



def get_single_expansion(num, denom):
    result = divide(num, denom)
    result['expansionLength'] = len(result.get('expansion', ''))
    return result

