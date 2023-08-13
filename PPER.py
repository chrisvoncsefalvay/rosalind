# Rosalind problem: PPER
# http://rosalind.info/problems/pper/

from utils.harness import RosalindProblem

# A note on this problem
# This is a remarkably frustrating problem, for one simple reason: the elegant solution is to use the factorial
# function, but that will introduce a precision error in Python. The solution is to use an identity whereby
# (n! / (n - k)!) % m = (n * (n - 1) * ... * (n - k + 1)) % m
# and rely on the modulo identity of (a * b) % m = ((a % m) * (b % m)) % m.
# This is a very inelegant solution, but it works.

def partial_permutations(vals: str) -> int:
    """Returns the number of partial permutations of length k from a set of length n, modulo 1_000_000."""
    n, k = (int(i) for i in vals.split(" "))

    ppers = 1

    # This is going to be incredibly inelegant, but we need to do it instead of the simple factorial division as Python
    # would otherwise screw up handling large numbers.
    for i in range(n - k + 1, n + 1):
        ppers = (ppers * i) % 1_000_000

    return ppers

h = RosalindProblem(partial_permutations, "rosalind_pper.txt")
h.process()
