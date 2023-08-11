# Rosalind problem: LEXF
# http://rosalind.info/problems/lexf/

from itertools import product

def lexicographic_product(alphabet: str, length: int) -> list:
    """Returns the lexicographic product of alphabet and itself length times."""
    return list(product(alphabet, repeat=length))

# create a text file output
with open("lexf.txt", "w") as output_file:
    alphabet = "A B C D E F G H".split()
    perms = lexicographic_product(alphabet, 3)
    for perm in perms:
        output_file.write("".join(perm) + "\n")

