import numpy as np

class toNumeric:
    def __init__(self, seq):
        self.seq = np.array(list(str(seq)))
        self.numDict = dict()
        self.codons =  np.array(['TTT','TTC','TTA','TTG','CTT','CTC','CTA','CTG','TCT','TCC','TCA','TCG','AGT','AGC','TAT','TAC',
                                'TAA','TAG','TGA','TGT','TGC','TGG','CCT','CCC','CCA','CCG','CAT','CAC','CAA','CAG','CGT','CGC',
                                'CGA','CGG','AGA','AGG','ATT','ATC','ATA','ATG','ACT','ACC','ACA','ACG','AAT','AAC','AAA','AAG',
                                'GTT','GTC','GTA','GTG','GCT','GCC','GCA','GCG','GAT','GAC','GAA','GAG','GGT','GGC','GGA','GGG'])

    def replacer(self):
        for nucleotide, number in self.numDict.items():
            self.seq = np.char.replace(self.seq, nucleotide, number)

    def Int_0(self):
        self.numDict = {'T':'0',  'C':'1',  'A':'2',  'G':'3'}

        self.replacer()
        return self.seq.astype(int)

    def Int_1(self):
        self.numDict = {'T':'1',  'C':'2',  'A':'3',  'G':'4'}

        self.replacer()
        return self.seq.astype(int)

    def Real(self):
        self.numDict = {'T':'-1.5',  'C':'0.5',  'A':'1.5',  'G':'-0.5'}

        self.replacer()
        return self.seq.astype(float)
    
    def Atomic(self):
        self.numDict = {'T':'6',  'C':'58',  'A':'70',  'G':'78'}

        self.replacer()
        return self.seq.astype(int)

    def EIIP(self):
        self.numDict = {'T':'0.1335',  'C':'0.1340',  'A':'0.1260',  'G':'0.0806'}

        self.replacer()
        return self.seq.astype(float)

    def PP(self):
        self.numDict = {'T':'1',  'C':'1',  'A':'-1',  'G':'-1'}

        self.replacer()
        return self.seq.astype(int)

    def AT_CG(self):
        self.numDict = {'T':'1',  'C':'-1',  'A':'1',  'G':'-1'}

        self.replacer()
        return self.seq.astype(int)

    def JustA(self):
        self.numDict = {'T':'0',  'C':'0',  'A':'1',  'G':'0'}

        self.replacer()
        return self.seq.astype(int)

    def JustC(self):
        self.numDict = {'T':'0',  'C':'1',  'A':'0',  'G':'0'}

        self.replacer()
        return self.seq.astype(int)

    def JustG(self):
        self.numDict = {'T':'0',  'C':'0',  'A':'0',  'G':'1'}

        self.replacer()
        return self.seq.astype(int)

    def JustT(self):
        self.numDict = {'T':'1',  'C':'0',  'A':'0',  'G':'0'}

        self.replacer()
        return self.seq.astype(int)

    def Codons(self):

        seq_len = len(self.seq)

        extend_seq = np.concatenate((self.seq, self.seq[0:3 - seq_len%3]), axis=None)
        extend_seq = extend_seq.astype('|S1').tobytes().decode('utf-8')
        combos = np.empty(seq_len, dtype = "<U{}".format(seq_len))

        for i in range(len(combos)):
            combos[i] = extend_seq[i:i+3]
    #Not figured out yet

    def Doublet(self):
        pass
    #Not figured out yet

if __name__ == "__main__":
    toNumeric()
