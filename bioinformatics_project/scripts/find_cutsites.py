import re
import sys
import argparse

def read_fasta(filepath):
    """Reads a FASTA file and returns the sequence as a single string, omitting whitespace and newlines."""
    sequence = []
    with open(filepath, 'r') as fasta_file:
        for line in fasta_file:
            if not line.startswith(">"):  # Ignore header lines starting with '>'
                sequence.append(line.strip())  # Remove newline and any surrounding spaces
    return ''.join(sequence)

def find_cut_sites(sequence, cut_site):
    """Finds all occurrences of the cut site in the DNA sequence."""
    # Remove the pipe '|' character from the cut site
    cut_site_cleaned = cut_site.replace("|", "")
    
    # Use regex to find all positions of the cut site in the sequence
    return [match.start() for match in re.finditer(cut_site_cleaned, sequence)]

def find_cut_site_pairs(positions, min_distance=80000, max_distance=120000):
    """Finds all pairs of cut sites that are between min_distance and max_distance apart."""
    pairs = []
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            distance = positions[j] - positions[i]
            if min_distance <= distance <= max_distance:
                pairs.append((positions[i], positions[j]))
    return pairs

def save_summary(pairs, output_file):
    """Saves a summary of the results to a file."""
    with open(output_file, 'w') as summary_file:
        summary_file.write(f"Total number of cut site pairs found: {len(pairs)}\n")
        summary_file.write("Positions of the first 5 pairs:\n")
        for i, (start, end) in enumerate(pairs[:5], 1):
            summary_file.write(f"Pair {i}: Start = {start}, End = {end}, Distance = {end - start} bp\n")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Find pairs of restriction enzyme cut sites in a DNA sequence")
    parser.add_argument("fasta_file", type=str, help="Path to the FASTA file")
    parser.add_argument("cut_site", type=str, help="Cut site sequence (e.g., 'G|GATCC')")
    
    args = parser.parse_args()

    # Read the DNA sequence from the FASTA file
    sequence = read_fasta(args.fasta_file)

    # Find all occurrences of the cut site
    cut_sites_positions = find_cut_sites(sequence, args.cut_site)

    # Find pairs of cut sites that are between 80,000 and 120,000 base pairs apart
    cut_site_pairs = find_cut_site_pairs(cut_sites_positions, 80000, 120000)

    # Print the results to the terminal
    print(f"Total number of cut site pairs found: {len(cut_site_pairs)}")
    print("Positions of the first 5 pairs:")
    for i, (start, end) in enumerate(cut_site_pairs[:5], 1):
        print(f"Pair {i}: Start = {start}, End = {end}, Distance = {end - start} bp")

    # Save the summary to a file in the results directory
    output_file = "../results/distant_cutsite_summary.txt"
    save_summary(cut_site_pairs, output_file)
    print(f"Summary saved to {output_file}")

if __name__ == "__main__":
    main()