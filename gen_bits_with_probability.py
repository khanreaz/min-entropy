''' function to generate a random bit string of length "length" with the given probabilities 
Example: 
length = 8
probabilities = [0.2, 0.8] # probability of  0 and 1 respectively
bit_string = generate_bit_string(length, probabilities)
bit_string = int(bit_string, base=2)
bit_string= format(bit_string, '08b')
print(bit_string)
'''
from numpy import random

def gen_bits_with_probability(length, probabilities):
    if sum(probabilities) != 1.0:
        raise ValueError('Probabilities must sum to 1.0')
    bit_string = ""

    for _ in range(length):
        rand_num = random.random()
        cumulative_prob = 0
        for bit, prob in enumerate(probabilities):
            cumulative_prob += prob
            if rand_num < cumulative_prob:
                bit_string += str(bit)
                break
    return bit_string