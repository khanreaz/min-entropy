def shannon_entropy(bit_string):
    """Return the   binary entropy of a bit string which is of array type."""
    from math import log2
    from collections import Counter

    bit_string = str(bit_string)
    count_0 = bit_string.count('0')
    count_1 = bit_string.count('1')

    prob_0 = count_0 / len(bit_string)
    prob_1 = count_1 / len(bit_string)

    prob_0 = max(prob_0, 1e-10) # to avoid log(0)
    prob_1 = max(prob_1, 1e-10)

    entropy_H0 = -prob_0 * log2(prob_0) - (1 - prob_0) * log2(1 - prob_0)
    entropy_H1 = -prob_1 * log2(prob_1) - (1 - prob_1) * log2(1 - prob_1)

    return (entropy_H0 + entropy_H1)