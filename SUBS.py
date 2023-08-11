# Rosalind problem: SUBS
# http://rosalind.info/problems/subs/

from utils.harness import RosalindProblem


def find_substring_locations(string: str, substring: str):
    """Find the locations of a substring within a string."""
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos == -1:  # No more occurrences
            return
        yield pos + 1  # Convert to 1-indexed position
        start = pos + 1  # Move past the last found occurrence


def find_motif_locations(string: str, substring: str) -> str:
    """Find the locations of a substring within a string."""
    return " ".join([str(i) for i in find_substring_locations(string, substring)])


h = RosalindProblem(find_motif_locations, "rosalind_subs.txt")
h.process()
