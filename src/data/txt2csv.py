import numpy as np
import os
import glob

import pandas as pd


class TXT2CSV():
    def __init__(self, path_to_dataset):
        self.path_to_dataset = path_to_dataset
        self.dataFrame = pd.DataFrame(columns = ['Class', 'Gene', 'Sequence'])
        
        self.MLDSP_phyla = ['3classes', 'Amphibians', 'BacteriaTest', 'Birds-Fish-Mammals', 'ClassToSubclass(Actinopterygii)', 'Dengue', 'DomainToKingdom(Eukaryota)', 'DomainToKingdom(Eukaryota_noProtists)', 
                            'FamilyToGenus(Cyprinidae)', 'Fungi', 'Influenza', 'Insects', 'KingdomToPhylum(Animalia)', 'Mammalia', 'Mammals', 'NewVertSequences', 'OrderToFamily(Cypriniformes)', 'PhylumToSubphylum(Chordata)', 
                            'Plants', 'Primates', 'Protists', 'SubclassToSuperorder(Neopterygii)', 'SubfamilyToGenus(Acheilognathinae)', 'SubphylumToClass(Vertebrata)', 'SuperorderToOrder(Ostariophysi)', 'Vertebrates']

    def Convert(self, output_path):

        class_names = ['Amphibians', 'Birds', 'Fish', 'Mammals', 'Reptiles']

        for class_name in class_names:

            for file in glob.glob(os.path.join(self.path_to_dataset, class_name, '*.txt')):
                with open(file) as f:
                    sequence = f.read().replace('\n', '')

                sequence = sequence[12:]
                gene = file[len(class_name+self.path_to_dataset)+2:][:-4]
                
                self.dataFrame = self.dataFrame.append(pd.DataFrame({'Class': class_name, 'Gene': gene, 'Sequence': sequence}, index=[0]), ignore_index=True)

                print('Added ', class_name, ": ", gene)
        
        self.dataFrame.to_csv(os.path.join(output_path, 'Vertebrates.csv'))


if __name__ == "__main__":
    path = os.path.join('data/external/ML-DSP', 'Vertebrates')

    convert = TXT2CSV(path_to_dataset = path)
    convert.Convert(output_path = 'data/interim/ML-DSP/Vertebrates')
