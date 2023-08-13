# Rosalind problem: PROT
# http://rosalind.info/problems/prot/

from utils.harness import RosalindProblem
from assets import CODON_TABLE

def translate_rna_to_protein(rna: str) -> str:
    """Returns the protein string encoded by the given RNA string."""
    protein = ""
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if CODON_TABLE[codon] == ".": # stop codon
            break
        protein += CODON_TABLE[codon]
    return protein

h = RosalindProblem(translate_rna_to_protein, "rosalind_prot.txt")
h.process()