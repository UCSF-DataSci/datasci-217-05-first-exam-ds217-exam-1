import random
import textwrap

#define nucleotides
nucleotides = ['A', 'C', 'G', 'T']

#generate random sequence
length = 1000000
random_sequence = ''.join(random.choices(nucleotides, k=length))

#format sequence with 80 base pairs per line
formatted_sequence = '\n'.join(textwrap.wrap(random_sequence, 80))

#specify output file in data directory
output_file = 'bioinformatics_project/data/random_sequence.fasta'

#write sequence to output file
with open(output_file, 'w') as fasta_file:
    fasta_file.write(">Random_DNA_Sequence\n")
    fasta_file.write(formatted_sequence)

print(f"Random DNA sequence saved to {output_file}")    

