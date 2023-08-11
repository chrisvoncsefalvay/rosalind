# Rosalind problem: PERM
# https://rosalind.info/problems/perm/

from itertools import permutations

def permutations_of_length(n: int) -> list:
    """Returns a list of all permutations of length n."""
    return list(permutations(range(1, n + 1)))


def number_of_permutations(n: int) -> int:
    """Returns the number of permutations of length n."""
    return len(permutations_of_length(n))


# create a text file output
with open("perm.txt", "w") as output_file:
    perms = permutations_of_length(7)
    output_file.write(str(number_of_permutations(7)) + "\n")
    for perm in perms:
        output_file.write(" ".join((str(y) for y in perm)) + "\n")

