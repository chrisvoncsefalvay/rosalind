# Rosalind problem: PRTM
# http://rosalind.info/problems/prtm/

from utils.harness import RosalindProblem
from assets import MASS_TABLE


def calculate_protein_mass(protein: str) -> float:
    """Returns the mass of the given protein string."""
    mass = 0
    for aa in protein:
        mass += MASS_TABLE[aa]
    return mass


h = RosalindProblem(calculate_protein_mass, "rosalind_prtm.txt")
h.process()
