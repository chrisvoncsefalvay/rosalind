class RosalindProblem:
    """Harness for running a Rosalind problem."""
    def __init__(self, func, input_file):
        self.func = func
        self.input_file = input_file
        self.output_file = input_file.replace("rosalind_", "").replace(".txt", "_solution.txt")

    def process(self):
        """Process the input file and write the output file."""
        with open(self.input_file, 'r') as infile, open(self.output_file, 'w') as outfile:
            arguments = []
            for line in infile:
                arguments.append(line.strip())

            print(arguments)
            result = self.func(*arguments)
            if isinstance(result, list):
                result = [str(item) for item in result]
                for item in result:
                    outfile.write(str(item) + '\n')
            else:
                outfile.write(str(result) + '\n')