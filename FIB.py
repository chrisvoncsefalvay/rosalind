# Rosalind problem: FIB
# http://rosalind.info/problems/fib/

from utils.harness import RosalindProblem


def fib(vals: str) -> int:
    """
    Returns the number of rabbit pairs after n months if each pair of rabbits produces k offspring.
    """
    n, k = (int(i) for i in vals.split(" "))
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, k * a + b
    return b

h = RosalindProblem(fib, "rosalind_fib.txt")
h.process()
