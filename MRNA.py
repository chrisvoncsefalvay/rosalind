# Rosalind problem: MRNA
# http://rosalind.info/problems/mrna/

from utils.harness import RosalindProblem
from collections import Counter
from assets import CODON_TABLE


def reverse_codon_table() -> dict:
    return dict(Counter(CODON_TABLE.values()))


def reverse_translate(protein: str) -> int:
    """Returns the number of RNA strings from which the given protein could have been translated."""
    reverse_table = reverse_codon_table()
    num_of_rna_strings = 1
    for aa in protein:
        num_of_rna_strings *= reverse_table[aa]
    return num_of_rna_strings * reverse_table["."] % 1_000_000


h = RosalindProblem(reverse_translate, "rosalind_mrna.txt")
h.process()
