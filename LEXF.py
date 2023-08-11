# Rosalind problem: LEXF
# http://rosalind.info/problems/lexf/

from itertools import product
from utils.harness import RosalindProblem

def lexicographic_product(alphabet: str, length: str) -> list:
    """Returns the lexicographic product of alphabet and itself length times."""
    return [''.join(i) for i in product(alphabet.split(" "), repeat=int(length))]


h = RosalindProblem(lexicographic_product, "rosalind_lexf.txt")
h.process()