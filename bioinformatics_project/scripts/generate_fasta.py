import random
import textwrap

def generate_random_dna_sequence(length):
    """Generates a random DNA sequence of a specified length."""
    return ''.join(random.choice('ACGT') for _ in range(length))

def save_as_fasta(sequence, file_path, description="Random DNA sequence"):
    """Saves a DNA sequence in FASTA format with 80 characters per line."""
    with open(file_path, 'w') as fasta_file:
        # Write the description line (FASTA header)
        fasta_file.write(f">{description}\n")
        
        # Wrap the sequence into lines of 80 characters and write to the file
        fasta_file.write("\n".join(textwrap.wrap(sequence, 80)))
        fasta_file.write("\n")

if __name__ == "__main__":
    # Generate a random DNA sequence of 1 million base pairs
    dna_sequence = generate_random_dna_sequence(1_000_000)
    
    # Save the sequence in FASTA format in the data directory
    file_path = "data/random_sequence.fasta"
    save_as_fasta(dna_sequence, file_path)

    print(f"Random DNA sequence saved in {file_path}")
