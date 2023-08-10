# Transcribing DNA into RNA

def dna_to_rna(dna_sequence: str) -> str:
    """
    Given a DNA sequence, return the RNA sequence.
    """
    return dna_sequence.replace("T", "U")

rna = dna_to_rna("ACGCGGTAACGTTCAGTAGAATGAGCTATTCGATTCCTGAAGAGTTAGACGGAGACCCCGCAGGAACAATATTAATCCGAGTACCCCCCTACGCTCGCCGATTGGCGAATGGCATGAGTCTCGATCAGGAGGTCAGGTAAGCTCTCATTTATTGGTTTGCTCAAGCACTCTCGTGCCGTACGAACTTGAGCCGTCGAATTGACCGAACGACTACGGGGCACGGGCGGTGCACCGCGACCTTGCGTCTCATTCTAACCGTTCGAGTCCCGCCGATCCTGCCTCGTCACCCCTACTGAATGTCGCATCTAACGTTTATCCCAAGGCGGGCCACACACCTCCTACATCAACGCTGCCCTGAGCCCCGAGCCTTAGAGAGATGTACACCGGAAGTAATGAGGGCCATGGAAAGTAGCAGTAAGTACGTTCTCATGGGGGGAGGTCTCTCGCCCGGATTTGCACTTCCTCAAAACTTCGCAAAGGCTAAGGCTTCTCGGACAACTATGGATGCATCATAGGTGCTTGGGTTGCCTATCTGTGACATAACGTGTAAGCAAAACTATCCGGATTCTCGTTTCGTTAATAAAACGTGTATACTAAAACTACTAGGCGGAAAAGTGCGTGGTAATAAAGGCATCAAATCTGGTGTACTTGAAACGGCTTAGTCTAATATATCGGGTCCAACCTCGGCGAAAATTGCAGGTGCTGTATTATAGCGCCCAGAGTTTCCCAGGGGACTACTCACTGCGCGCACGAAACGTAATCGGGATCGTGAATCGAAGGCGCCACGCCTAGGACTTATAACACGGATGCCCCCCTGGGCCAATAAGCCACTAACTGAGTGGAGGATAGTACTTGGTCATGCTTAATCGGCGAGTCCGTCTCGTGCAAGACAATGGCTGTATGCACCTCATGCGAGATAAGGGCCGCGTAAAGGTGCTATTCACCCCACTCATCTTAAGCAGTATGATATCTAGGCCGGGACAT")

print(rna)