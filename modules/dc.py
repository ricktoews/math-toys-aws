from mathutils import divide
from mathutils import is_prime
from mathutils import digits_to_expansion

def get_expansions(denom):
    prime = is_prime(denom)
    expansions = {}
    
    for num in range(1, denom):
        # Check each numerator, and calculate the expansion if it hasn't already been done
        if num not in expansions:
            result = divide(num, denom)
            expansion = result['expansion']
            expansion_numerators = result['expansionNumerators']
            begin_repeat = result['beginRepeat']
            
            expansions[num] = {
                'digits': expansion,
                'expansion': expansion,
                'position': expansion_numerators[num],
                'beginRepeat': begin_repeat
            }
            
            # This block is only for prime numbers
            if prime:
                for n in expansion_numerators.keys():
                    expansions[int(n)] = {
                        'digits': expansion,
                        'expansion': expansion,
                        'position': expansion_numerators[int(n)],
                        'beginRepeat': begin_repeat
                    }
        else:
            expansions[num]['expansion'] = digits_to_expansion(expansions[num])
    
    output = {}
    for num in range(1, denom):
        digits = expansions[num]['digits']
        numerator = num
        position = expansions[num]['position']
        begin_repeat = expansions[num]['beginRepeat']
        
        if digits not in output:
            output[digits] = []
        output[digits].append({
            'numerator': numerator,
            'position': position,
            'beginRepeat': begin_repeat
        })

    return {'byExpansion': output, 'byNumerator': expansions}