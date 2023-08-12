class RosalindProblem:
    """
    Constructor for RosalindProblem class.

    Args:
        func (function): The function to be called.
        input_file (str): The input file name.
        fasta (bool, optional): Indicates if the input file is in FASTA format. Defaults to False.
    """
    def __init__(self, func, input_file, fasta=False):
        self.func = func
        self.fasta = fasta
        self.input_file = input_file
        self.output_file = input_file.replace("rosalind_", "").replace(".txt", "_solution.txt")

    def process(self):
        """Process the input file and write the output file."""
        with open(self.input_file, 'r') as infile, open(self.output_file, 'w') as outfile:
            arguments = []

            if self.fasta:
                arguments = [infile.read()]
            else:
                for line in infile:
                    arguments.append(line.strip())

            print(arguments)
            result = self.func(*arguments)
            if isinstance(result, list) or isinstance(result, tuple):
                result = [str(item) for item in result]
                for item in result:
                    outfile.write(str(item) + '\n')
            else:
                outfile.write(str(result) + '\n')