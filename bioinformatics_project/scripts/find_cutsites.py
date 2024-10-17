import sys
import os

#functions
def read_fasta(filepath):   #reads the FASTA file and save the DNA sequence to a variable omitting white space
    with open(filepath, 'r') as file:
        lines = file.readlines()

    dna_sequence = ''.join(line.strip() for line in lines)
    return dna_sequence

def find_cutsites(sequence, cut_site):  #find all occurrences of the cut site in the DNA sequence
    cut_site = cut_site.replace('|', '')
    cut_positions = []
    index = sequence.find(cut_site)

    while index != -1:  
        cut_positions.append(index)
        index = sequence.find(cut_site, index + 1)

    return cut_positions

def find_cut_sitepairs(cut_positions):  #find all pairs of cut site locations that are 80-120 bkp apart
    pairs = []
    for i in range(len(cut_positions)):
        for j in range(i + 1, len(cut_positions)):
            distance = cut_positions[j] - cut_positions[i]
            if 80000 <= distance <= 120000:
                pairs.append((cut_positions[i], cut_positions[j]))
    
    return pairs

def save_summary(filepath, total_pairs, first_five_pairs):  #print the total number of cut site pairs found and the positions of the first 5 pairs
    with open(filepath, 'w') as file:
        file.write(f"Total number of cut site pairs found: {total_pairs}\n")
        file.write("Positions of the first 5 cut site pairs:\n")
        for idx, pair in enumerate(first_five_pairs, 1):
            file.write(f"{idx}. {pair[0]} - {pair[1]}\n")

def main():
    if len(sys.argv) != 3:
        print ("Invalid input.")
        print("Usage: python3 find_cutsites.py <FASTA_file> <cut_site_sequence>")
        sys.exit(1)

    #specify arguments
    fasta_file = sys.argv[1]
    cut_site = sys.argv[2]

    if not os.path.isfile(fasta_file):  #ensure FASTA file exits
        print(f"Error: The file {fasta_file} does not exist.")
        sys.exit(1)
        
    dna_sequence = read_fasta(fasta_file)   #read DNA sequence from FASTA file
    cut_positions = find_cutsites(dna_sequence, cut_site)   #find all occurrences of the cut site in the sequence
    cut_site_pairs = find_cut_sitepairs(cut_positions)  #find all pairs of cut sites 80-120 kbp apart

    #print total number of cut site pairs found and the positions of the first 5 pairs
    print(f"Analyzing cut site: {cut_site}")
    print(f"Total cut sites found: {len(cut_positions)}")
    print(f"Cut site pairs 80-120 kbp apart: {len(cut_site_pairs)}")
    print("First 5 pairs:")
    first_five_pairs = cut_site_pairs[:5]
    for idx, pair in enumerate(first_five_pairs, 1):
        print(f"{idx}. {pair[0]} - {pair[1]}")

    #save a summary of the results in the results directors
    summary_file_path = 'bioinformatics_project/results/cutsite_summary.txt'
    save_summary(summary_file_path, len(cut_site_pairs), first_five_pairs)

    print(f"Summary saved to {summary_file_path}")

if __name__ == "__main__":
    main()