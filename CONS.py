# Rosalind problem: CONS
# http://rosalind.info/problems/cons/

from utils.harness import RosalindProblem
from collections import Counter


def get_profile_matrix(*sequences) -> str:
    # Transpose sequences
    t_seqs = list(zip(*sequences))

    # Initialize a dictionary of lists to store the profile matrix.
    profile_matrix = {'A': [], 'C': [], 'G': [], 'T': []}

    # For each position, count the frequency of each nucleotide and append it to the profile matrix.
    for pos in t_seqs:
        cnt = Counter(pos)  # Count the frequencies.
        profile_matrix['A'].append(cnt['A'])
        profile_matrix['C'].append(cnt['C'])
        profile_matrix['G'].append(cnt['G'])
        profile_matrix['T'].append(cnt['T'])

    return profile_matrix


def get_consensus(profile_matrix: dict) -> str:
    consensus = []

    # Loop through each position in the sequences.
    for i in range(len(profile_matrix['A'])):
        max_nuc_count = max(
            profile_matrix['A'][i],
            profile_matrix['C'][i],
            profile_matrix['G'][i],
            profile_matrix['T'][i]
        )

        # Determine which nucleotide is most common. Inelegant, but it works.
        if max_nuc_count == profile_matrix['A'][i]:
            consensus.append('A')
        elif max_nuc_count == profile_matrix['C'][i]:
            consensus.append('C')
        elif max_nuc_count == profile_matrix['G'][i]:
            consensus.append('G')
        else:
            consensus.append('T')

    return ''.join(consensus)


def format_profile_matrix(profile_matrix: dict) -> str:
    formatted = ''

    for key in profile_matrix.keys():
        formatted += f'{key}: {" ".join([str(i) for i in profile_matrix[key]])}\n'

    return formatted


def consensus_and_profile(*sequences: list) -> str:
    """Returns the consensus string and profile matrix for the given list of sequences."""
    profile_matrix = get_profile_matrix(*sequences)
    consensus = get_consensus(profile_matrix)
    formatted_profile_matrix = format_profile_matrix(profile_matrix)

    return f'{consensus}\n{formatted_profile_matrix}'


h = RosalindProblem(consensus_and_profile, "rosalind_cons.txt", fasta=True)
h.process()
