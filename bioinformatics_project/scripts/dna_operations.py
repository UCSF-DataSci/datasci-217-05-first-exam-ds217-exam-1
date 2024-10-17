import sys

#dictionary for DNA complement mapping
complement_map = {
    'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', #handle uppercase
    'a': 't', 't': 'a', 'c': 'g', 'g': 'c'  #handle lowercase
}

#functions
def complement(sequence): #returns the complement of a DNA sequence
    return ''.join([complement_map[base] for base in sequence])

def reverse(sequence): #returns the reverse of a sequence
    return sequence[::-1]

def reverse_complement(sequence): #returns the reverse complement of a DNA sequence
    return reverse(complement(sequence))

def main():
    if len(sys.argv) !=2:
        print ("Invalid input.")
        print ("Usage: python 3 dna_operations.py <DNA_sequence>")
        sys.exit(1)

    sequence = sys.argv[1]

    original_sequence = sequence
    complement_sequence = complement(sequence)
    reverse_sequence = reverse(sequence)
    reverse_complement_sequence = reverse_complement(sequence)

    print(f"Original sequence:        {original_sequence}")
    print(f"Complement sequence:      {complement_sequence}")
    print(f"Reverse sequence:         {reverse_sequence}")
    print(f"Reverse complement:       {reverse_complement_sequence}")

if __name__ == "__main__":
    main()  