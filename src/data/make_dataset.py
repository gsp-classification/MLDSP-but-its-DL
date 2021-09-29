
# !Script to make a csv dataset to feed into the spectrogram from the ML-DSP dataset from DOI: <https://doi.org/10.1186/s12864-019-5571-y>
# *Import packages
import glob
import os
import csv

# *Making a list of the folders
classes = os.listdir('../../data/external/Vertebrates')

# *Initialising the dataset list
dataset = []

print("\nBeginning extraction from genomic sequences in .txt format present in gene-to-signal/data/external/Vertebrates.")
print("---------------------------------------------------------------------------------------------------------------\n")
# *Iterating over the class folders
for vert_class in classes:
    print("Extracting from class of "+vert_class+".")

    # *Iterating over genome files in each class
    for genome in glob.iglob('../../data/external/Vertebrates/'+vert_class+"/*.txt"):

        # *Reading the genome
        with open(genome) as f:
            seq = f.read()
        
        # *Sectioning the first 5000 nucleotides of the genome because my laptop is dying
<<<<<<< HEAD
        geneseq = seq[13:1013]
=======
        geneseq = seq[13:5013]
>>>>>>> gsp/main

        # *Spliting the path for the ID
        id = genome.split('/')[-1][:-4]

        # *Making a row of the csv
        row = {'Class': vert_class, 'ID': id, 'Gene Sequence': geneseq}

        # *Appending to the final dataset
        dataset.append(row)

# *Creating the csv in the 'interim' folder under 'data'
with open('../../data/interim/dataset.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=dataset[0].keys())
    writer.writeheader()
    writer.writerows(dataset)

print("\n---------------------------------------------------------------------------------------------------------------")
<<<<<<< HEAD
print("Dataset with Class, ID and gene sequences (first 1000 bases) created at gene-to-signal/data/interim/dataset.csv.\n")
=======
print("Dataset with Class, ID and gene sequences (first 5000 bases) created at gene-to-signal/data/interim/dataset.csv.\n")
>>>>>>> gsp/main
# ?Can this be done better? Is a csv necessary or can it just be a folder full of the dataset? 