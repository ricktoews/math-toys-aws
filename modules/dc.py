from mathutils import divide, digits_to_expansion
from primes import primes

# Example of what `divide` returns: divide(1, 7):
# {'expansion': '142857', 'expansionNumerators': {1: 1, 3: 2, 2: 3, 6: 4, 4: 5, 5: 6}, 'beginRepeat': 1}
# `expansionNumerators` is a table:
#   key is a numerator, 
#   value is the position at which the numerator's decimal expansion begins within `expansion`.
# Example: 3/7 = .428571. It begins at position 2 within `expansion`, since 4 is the second digit in 142857.
# For the 7ths, there is no need to calculate each decimal expansion, since all use the same digits,
# just beginning at a different position. This is what `if num in by_numerator` detects.
# Note that the short-circuiting of decimal expansion calculation is performed only for prime numbers.

def get_expansions(denom):
    is_prime = denom in primes
    by_numerator = {}
    by_expansion = {}
    
    for num in range(1, denom):
        # Check each numerator to see if it's already been calculated.
        # This will usually be the case for prime denominators other than 2 and 5.
        # This will never be the case for composite denominators or 2 or 5.
        if num in by_numerator:
            by_numerator[num]['expansion'] = digits_to_expansion(digits=by_numerator[num]['expansion'], ndx=by_numerator[num]['position'] - 1)
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

