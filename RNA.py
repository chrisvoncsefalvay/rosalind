# Rosalind problem: RNA
# http://rosalind.info/problems/dna/

from utils.harness import RosalindProblem

def dna_to_rna(dna_sequence: str) -> str:
    """
    Given a DNA sequence, return the RNA sequence.
    """
    return dna_sequence.replace("T", "U")


h = RosalindProblem(dna_to_rna, "rosalind_rna.txt")
h.process()