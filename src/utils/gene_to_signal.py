
# *Import packages
from os import error
import math 
import csv
import sys

# !Specify the type of representation you want the DNA sequence to be converted into. Choose from: ['Voss', 'Tetrahedron', 'Integer', 'Real', 'Complex']. Default = 'Voss'
# *This is the only variable that needs to be set in this script.
metric = 'Voss'

# !Functions
# *Function to make a list out of the gene sequence. Outputs a list from a string input.
def split(gene):
    return [base for base in gene]

# *Function to flatten nested lists into list. Outputs a linear list from a nested list input.
def merge(nuclist):
    lis = []
    for el in sum(nuclist, []):
        lis.append(el)
    return lis

# *Funtion to change sequences to signals. Inputs a seq (string) and type(string) of representation and outputs a list of DNA signal.
def DNAtoSignal(seq, type):
    # *Splitting the seq string into a seq list."
    baselist = split(seq)

    # *Voss Representation. (signal[0], signal[1], signal[2], signal[3]) ~ (A, G, T, C) respectively.
    if (type == "Voss"):

        # *Output list called signal.
        signal = [[],[],[],[]]
        for base in baselist:
            if base == 'C' or base == 'c':
                signal[3].append(1)
                signal[1].append(0)
                signal[0].append(0)
                signal[2].append(0)
            elif base == 'G' or base == 'g':
                signal[3].append(0)
                signal[1].append(1)
                signal[0].append(0)
                signal[2].append(0)
            elif base == 'A' or base == 'a':                
                signal[3].append(0)
                signal[1].append(0)
                signal[0].append(1)
                signal[2].append(0)
            elif base == 'T' or base == 't':
                signal[3].append(0)
                signal[1].append(0)
                signal[0].append(0)
                signal[2].append(1)
            elif base == 'U' or base == 'u':
                signal[3].append(0)
                signal[1].append(0)
                signal[0].append(0)
                signal[2].append(1)
            elif base == 'R' or base == 'r':
                signal[3].append(0)
                signal[1].append(1)
                signal[0].append(1)
                signal[2].append(0)
            elif base == 'Y' or base == 'y':
                signal[3].append(1)
                signal[1].append(0)
                signal[0].append(0)
                signal[2].append(1)
            elif base == 'K' or base == 'k':
                signal[3].append(0)
                signal[1].append(1)
                signal[0].append(0)
                signal[2].append(1)
            elif base == 'M' or base == 'm':
                signal[3].append(1)
                signal[1].append(0)
                signal[0].append(1)
                signal[2].append(0)
            elif base == 'S' or base == 's':
                signal[3].append(1)
                signal[1].append(1)
                signal[0].append(0)
                signal[2].append(0)
            elif base == 'W' or base == 'w':
                signal[3].append(0)
                signal[1].append(0)
                signal[0].append(1)
                signal[2].append(1)
            elif base == 'B' or base == 'b':
                signal[3].append(1)
                signal[1].append(1)
                signal[0].append(0)
                signal[2].append(1)
            elif base == 'D' or base == 'd':
                signal[3].append(0)
                signal[1].append(1)
                signal[0].append(1)
                signal[2].append(1)
            elif base == 'H' or base == 'h':
                signal[3].append(1)
                signal[1].append(0)
                signal[0].append(1)
                signal[2].append(1)
            elif base == 'V' or base == 'v':
                signal[3].append(1)
                signal[1].append(1)
                signal[0].append(1)
                signal[2].append(0)
            elif base == 'N' or base == 'n':
                signal[3].append(1)
                signal[1].append(1)
                signal[0].append(1)
                signal[2].append(1)
            elif base == 'X' or base == 'x':
                signal[3].append(1)
                signal[1].append(1)
                signal[0].append(1)
                signal[2].append(1)

        # *Returning a flattened list.
        return merge(signal)

    # *Tetrahedron Representation. The formula is taken from the paper <https://dx.doi.org/10.7717%2Fpeerj.4264>
    elif type == 'Tetrahedron':
        signal = [[],[],[]]
        for base in baselist:
            if base == 'A' or base == 'a':
                signal[0].append(0*math.sqrt(2)/3)
                signal[1].append(0*math.sqrt(6)/3)
                signal[2].append(3/3)
            if base == 'G' or base == 'g':
                signal[0].append(-1*math.sqrt(2)/3)
                signal[1].append(-1*math.sqrt(6)/3)
                signal[2].append(-1/3)
            if base == 'T' or base == 't':
                signal[0].append(2*math.sqrt(2)/3)
                signal[1].append(0*math.sqrt(6)/3)
                signal[2].append(-1/3)
            if base == 'C' or base == 'c':
                signal[0].append(-1*math.sqrt(2)/3)
                signal[1].append(1*math.sqrt(6)/3)
                signal[2].append(-1/3)
            if base == 'U' or base == 'u':
                signal[0].append(2*math.sqrt(2)/3)
                signal[1].append(0*math.sqrt(6)/3)
                signal[2].append(-1/3)
        return merge(signal)

    # *Integer Representation. (0,1,2,3) ~ (A, T, G, C) respectively.
    elif type == 'Integer':
        signal = []
        for base in baselist:
            if base == 'C' or base == 'c':
                signal.append(3)
            if base == 'G' or base == 'g':
                signal.append(2)
            if base == 'A' or base == 'a':
                signal.append(0)
            if base == 'T' or base == 't':
                signal.append(1)
            if base == 'U' or base == 'u':
                signal.append(1)
        return signal

    # *Real Representation. (-1.5, -0.5, 0.5, 1.5) ~ (A, T, G, C) respectively.
    elif type == 'Real':
        signal = []
        for base in baselist:
            if base == 'C' or base == 'c':
                signal.append(1.5)
            if base == 'G' or base == 'g':
                signal.append(0.5)
            if base == 'A' or base == 'a':
                signal.append(-1.5)
            if base == 'T' or base == 't':
                signal.append(-0.5)
            if base == 'U' or base == 'u':
                signal.append(-0.5)
        return signal
    
    # *Complex Representation. ((1,1), (1,-1), (-1,1), (-1,-1)) ~ (A, T, G, C) respectively.
    elif type == 'Complex':
        signal = [[],[]]
        for base in baselist:
            if base == 'C' or base == 'c':
                signal[0].append(-1)
                signal[1].append(-1)
            if base == 'G' or base == 'g':
                signal[0].append(-1)
                signal[1].append(1)
            if base == 'A' or base == 'a':
                signal[0].append(1)
                signal[1].append(1)
            if base == 'T' or base == 't':
                signal[0].append(1)
                signal[1].append(-1)
            if base == 'U' or base == 'u':
                signal[0].append(1)
                signal[1].append(-1)
        return merge(signal)

# *List to make DNASignal.csv
DNASignal = []

# *Check to see error in choosing representation.
if metric in ['Voss', 'Tetrahedron', 'Integer', 'Real', 'Complex']:

    # *Opening dataset.csv with gene sequences.
    with open('../../data/interim/dataset.csv', mode='r') as csv_file:
        rows = csv.DictReader(csv_file)

        # *To check if running properly.
        current_class = 'Birds'
        print("\nConverting DNA sequences to "+metric+" representation.")
        print("---------------------------------------------------------------------------------------------------------------")
        print("Converting class of "+current_class+".")

        # *Looping through the various gene sequences in dataset.csv.
        for row in rows:
            if current_class != row['Class']:
                current_class = row['Class']
                print("Converting class of "+current_class+".")
            
            # *Calling the DNAtoSignal function to generate DNA signal.
            signal = DNAtoSignal(row['Gene Sequence'], metric)

            # *Making new csv row with 'Signal' key.
            data_row = {'Class': row['Class'], 'ID': row['ID'], 'Gene Sequence': row['Gene Sequence'], 'Signal': signal}
            DNASignal.append(data_row)

    # *Creating the csv at ../../data/processed/DNASignal.csv.
    with open('../../data/processed/DNASignal.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=DNASignal[0].keys())
        writer.writeheader()
        writer.writerows(DNASignal) 

    # *Statement signfying end of script.
    print("---------------------------------------------------------------------------------------------------------------")
    print("Sequences converted and stored at gene-to-signal/data/processed/DNASignal.csv.\n")

# *In case of wrong representation variable.
else:
    print("\n---------------------------------------------------------------------------------------------------------------")
    print("\nError: Type of representation is not supported. Please check the variable 'metric'.\n")
    print("---------------------------------------------------------------------------------------------------------------")
    sys.exit()