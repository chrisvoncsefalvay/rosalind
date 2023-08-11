# Rosalind problem: LEXV
# http://rosalind.info/problems/lexv/

from itertools import product
from utils.harness import RosalindProblem


def generate_strings(alphabet: str, n: str):
    alphabet = alphabet.split()

    # Initialize an empty list to hold the results
    results = []

    for i in range(1, int(n) + 1):
        # Generate all permutations of the given length
        permuts = [''.join(p) for p in product(alphabet, repeat=i)]

        # Add them to the results list
        results += permuts

    # Sort results lexicographically
    results.sort(key=lambda word: [alphabet.index(c) for c in word])
    return results

h = RosalindProblem(generate_strings, "rosalind_lexv.txt")
h.process()