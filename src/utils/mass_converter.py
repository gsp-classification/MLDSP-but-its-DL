from dna2signal import toNumeric
from signal2spec import toSpectrogram

import numpy as np
import os
import glob


class massConvertToSpec():
    def __init__(self, path_to_dataset):
        self.path_to_dataset = path_to_dataset
        self.dataDict = dict()
        self.MLDSP_phyla = ['3classes', 'Amphibians', 'BacteriaTest', 'Birds-Fish-Mammals', 'ClassToSubclass(Actinopterygii)', 'Dengue', 'DomainToKingdom(Eukaryota)', 'DomainToKingdom(Eukaryota_noProtists)', 
                            'FamilyToGenus(Cyprinidae)', 'Fungi', 'Influenza', 'Insects', 'KingdomToPhylum(Animalia)', 'Mammalia', 'Mammals', 'NewVertSequences', 'OrderToFamily(Cypriniformes)', 'PhylumToSubphylum(Chordata)', 
                            'Plants', 'Primates', 'Protists', 'SubclassToSuperorder(Neopterygii)', 'SubfamilyToGenus(Acheilognathinae)', 'SubphylumToClass(Vertebrata)', 'SuperorderToOrder(Ostariophysi)', 'Vertebrates']

    def generate_dict(self, class_name):

        self.dataDict[class_name] = {}

        for file in glob.glob(os.path.join(self.path_to_dataset, class_name, '*.txt')):
            with open(file) as f:
                data = f.read().replace('\n', '')

            data = data[12:][:5000]

            X = toNumeric(data).Voss()
            spec = toSpectrogram(X).inNumpy()
            f_name = file[len(class_name+self.path_to_dataset)+2:][:-4]
            
            self.dataDict[class_name][f_name] = {}
            self.dataDict[class_name][f_name]['Sequence'] = data
            self.dataDict[class_name][f_name]['Signal'] = X
            self.dataDict[class_name][f_name]['Spec'] = spec

            print('Added ', class_name, ": ", f_name)


    def save_to_numpy(self, path):
        np.save(path, self.dataDict)
        print("Saved to ", path)

if __name__ == "__main__":
    path = os.path.join('data/external/ML-DSP', 'Vertebrates')
    
    class_names = ['Amphibians', 'Birds', 'Fish', 'Mammals', 'Reptiles']

    class_name = class_names[4]

    convert = massConvertToSpec(path_to_dataset=path)
    convert.generate_dict(class_name=class_name)
    convert.save_to_numpy(path="data/processed/Vertebrates/{}.npy".format(class_name))
