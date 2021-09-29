
# *Import packages
import glob
import os
import csv
from pyfaidx import Fasta

posgenes = Fasta('data/external/VFDB_setA_nt.fasta')

# *Initialising the dataset list
VFDBset = []

print("\nBeginning extraction from genomic sequences in .fasta format present in gene-to-signal/data/external/VFDB_setA_nt.fasta")
print("---------------------------------------------------------------------------------------------------------------\n")
# *Iterating over IDs
for gene in posgenes.keys():
    print("Extracting "+gene)
    # *Reading the genome
    seq=posgenes[gene][0:1000].seq
    id = gene
    # *Making a row of the csv
    row = {'ID': id, 'Gene Sequence': seq, 'Class': 1}

    # *Appending to the final dataset
    VFDBset.append(row)

print("\n---------------------------------------------------------------------------------------------------------------")
print("Dataset with ID and gene sequences (first 1000 bases) created at gene-to-signal/data/interim/VFDBset.csv.\n")
# ?Can this be done better? Is a csv necessary or can it just be a folder full of the dataset? 

neggenes = Fasta('data/external/DEG10.nt')

print("\nBeginning extraction from genomic sequences in .fasta format present in gene-to-signal/data/external/DEG10.nt")
print("---------------------------------------------------------------------------------------------------------------\n")
# *Iterating over IDs
for gene in neggenes.keys():
    print("Extracting "+gene)
    # *Reading the genome
    seq=neggenes[gene][0:1000].seq
    id = gene

    # *Making a row of the csv
    row = {'ID': id, 'Gene Sequence': seq, 'Class': 0}

    # *Appending to the final dataset
    VFDBset.append(row)

# *Creating the csv in the 'interim' folder under 'data'
with open('data/interim/VFDBset.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=VFDBset[0].keys())
    writer.writeheader()
    writer.writerows(VFDBset)

print("\n---------------------------------------------------------------------------------------------------------------")
print("Dataset with ID and gene sequences (first 1000 bases) created at gene-to-signal/data/interim/VFDBset.csv.\n")

