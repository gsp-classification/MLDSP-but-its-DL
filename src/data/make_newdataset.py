
# !Script to make a csv dataset to feed into the spectrogram from the ML-DSP dataset from DOI: <https://doi.org/10.1186/s12864-019-5571-y>
# *Import packages
import glob
import os
import csv
from pyfaidx import Fasta

genes = Fasta('data/external/VFDB_setA_nt.fasta')

# *Initialising the dataset list
VFDBset = []

print("\nBeginning extraction from genomic sequences in .txt format present in gene-to-signal/data/external/VFDB_setA_nt.fasta")
print("---------------------------------------------------------------------------------------------------------------\n")
# *Iterating over the class folders
for gene in genes.keys():
    print("Extracting "+gene)
    # *Reading the genome
    seq=genes[gene][0:1000].seq

    # *Spliting the path for the ID
    id = gene

        # *Making a row of the csv
    row = {'ID': id, 'Gene Sequence': seq}

        # *Appending to the final dataset
    VFDBset.append(row)

# *Creating the csv in the 'interim' folder under 'data'
with open('data/interim/VFDBset.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=VFDBset[0].keys())
    writer.writeheader()
    writer.writerows(VFDBset)

print("\n---------------------------------------------------------------------------------------------------------------")
print("Dataset with ID and gene sequences (first 1000 bases) created at gene-to-signal/data/interim/VFDBset.csv.\n")
# ?Can this be done better? Is a csv necessary or can it just be a folder full of the dataset? 