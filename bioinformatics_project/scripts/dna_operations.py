import sys
import argparse

# Define a dictionary for the complement of DNA bases
complement_dict = {
    'A': 'T', 'T': 'A',
    'C': 'G', 'G': 'C',
    'a': 't', 't': 'a',
    'c': 'g', 'g': 'c'
}

def complement(sequence):
    """Returns the complement of a DNA sequence."""
    return ''.join([complement_dict[base] for base in sequence])

def reverse(sequence):
    """Returns the reverse of a DNA sequence."""
    return sequence[::-1]

def reverse_complement(sequence):
    """Returns the reverse complement of a DNA sequence."""
    return reverse(complement(sequence))

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Perform operations on a DNA sequence")
    parser.add_argument("sequence", type=str, help="The DNA sequence to process")
    
    args = parser.parse_args()
    sequence = args.sequence

    # Validate the sequence (optional step)
    if not all(base in 'ACGTacgt' for base in sequence):
        print("Error: The sequence contains invalid characters. Please enter a valid DNA sequence.")
        sys.exit(1)

    # Perform operations
    comp_seq = complement(sequence)
    rev_seq = reverse(sequence)
    rev_comp_seq = reverse_complement(sequence)

    # Print results
    print(f"Original sequence:         {sequence}")
    print(f"Complement:               {comp_seq}")
    print(f"Reverse:                  {rev_seq}")
    print(f"Reverse complement:       {rev_comp_seq}")

if __name__ == "__main__":
    main()