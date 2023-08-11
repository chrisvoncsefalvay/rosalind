# Rosalind problem: PERM
# https://rosalind.info/problems/perm/

from itertools import permutations
from utils.harness import RosalindProblem

def permutations_of_length(n: int) -> list:
    """Returns a list of all permutations of length n."""
    return list(permutations(range(1, n + 1)))

def generate_permutations(n: str) -> list:
    perms = permutations_of_length(int(n))
    num_of_perms = len(perms)
    return [num_of_perms] + [" ".join([str(i) for i in perm]) for perm in perms]

h = RosalindProblem(generate_permutations, "rosalind_perm.txt")
h.process()