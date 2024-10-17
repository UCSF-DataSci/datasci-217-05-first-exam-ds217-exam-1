#!/bin/bash

#create main project directory
mkdir -p bioinformatics_project

#create subdirectories within the main directory
mkdir -p bioinformatics_project/data
mkdir -p bioinformatics_project/scripts
mkdir -p bioinformatics_project/results

#create empty Python files inside the scripts directory
touch bioinformatics_project/scripts/generate_fasta.py
touch bioinformatics_project/scripts/dna_operations.py
touch bioinformatics_project/scripts/find_cutsites.py

#create an empty file inside the results directory
touch bioinformatics_project/results/cutsite_summary.txt

#create an empty file in the data directory
touch bioinformatics_project/data/random_sequence.fasta

#create README.md file in the main directory
echo "# Bioinformatics Project Structure" > bioinformatics_project/README.md
echo "This project contains the following directories and files:" >> bioinformatics_project/README.md
echo "" >> bioinformatics_project/README.md
echo "## Directories:" >> bioinformatics_project/README.md
echo "- data: Contains data files such as sequences, e.g., random_sequence.fasta" >> bioinformatics_project/README.md
echo "- scripts: Contains Python scripts for processing and analysis" >> bioinformatics_project/README.md
echo "- results: Stores output files such as analysis summaries" >> bioinformatics_project/README.md
echo "" >> bioinformatics_project/README.md
echo "## Files:" >> bioinformatics_project/README.md
echo "- scripts/generate_fasta.py: Script to generate FASTA files" >> bioinformatics_project/README.md
echo "- scripts/dna_operations.py: Script to perform DNA-related operations" >> bioinformatics_project/README.md
echo "- scripts/find_cutsites.py: Script to find cut sites in DNA sequences" >> bioinformatics_project/README.md
echo "- results/cutsite_summary.txt: Summary of found cut sites" >> bioinformatics_project/README.md
echo "- data/random_sequence.fasta: Placeholder for a random DNA sequence in FASTA format" >> bioinformatics_project/README.md

#make script executable
chmod +x setup_project.sh


