# Rosalind problem: DNA
# http://rosalind.info/problems/dna/

from typing import List
from utils.harness import RosalindProblem

def count_bases(sequence: str) -> List[int]:
    """
    Given a DNA sequence, return a list of the counts of each base.
    """
    counts = [0, 0, 0, 0]
    for base in sequence:
        if base == 'A':
            counts[0] += 1
        elif base == 'C':
            counts[1] += 1
        elif base == 'G':
            counts[2] += 1
        elif base == 'T':
            counts[3] += 1
    return " ".join([str(count) for count in counts])

h = RosalindProblem(count_bases, "rosalind_dna.txt")
h.process()