# Rosalind problem: GC
# http://rosalind.info/problems/GC/

from utils.harness import RosalindProblem
from typing import Tuple


def parse_fasta(fasta: str) -> dict:
    """Parse FASTA strings into a dictionary keyed by their label."""
    sequences = fasta.strip().split(">")[1:]
    return {seq.split("\n", 1)[0]: seq.split("\n", 1)[1].replace("\n", "") for seq in sequences}


def calc_gc_content(seq: str) -> float:
    """Calculate GC content in a sequence."""
    return round((seq.count("G") + seq.count("C")) / len(seq) * 100, 6)


def highest_gc_content(fasta: str) -> Tuple[str, float]:
    """Find the sequence with the highest GC content."""
    sequences = parse_fasta(fasta)
    max_gc_content = -1
    max_gc_label = ""

    for label, sequence in sequences.items():
        gc_content = calc_gc_content(sequence)

        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_gc_label = label

    return max_gc_label, max_gc_content


h = RosalindProblem(highest_gc_content, "rosalind_gc.txt", fasta=True)
h.process()
