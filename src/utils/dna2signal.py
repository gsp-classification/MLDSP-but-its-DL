import numpy as np

class toNumeric:
    def __init__(self, seq):
        self.seq_raw = np.array(list(seq))
        self.seq = np.char.upper(self.seq_raw)
        self.numDict = dict()
        self.codons =  np.array(['TTT','TTC','TTA','TTG','CTT','CTC','CTA','CTG','TCT','TCC','TCA','TCG','AGT','AGC','TAT','TAC',
                                'TAA','TAG','TGA','TGT','TGC','TGG','CCT','CCC','CCA','CCG','CAT','CAC','CAA','CAG','CGT','CGC',
                                'CGA','CGG','AGA','AGG','ATT','ATC','ATA','ATG','ACT','ACC','ACA','ACG','AAT','AAC','AAA','AAG',
                                'GTT','GTC','GTA','GTG','GCT','GCC','GCA','GCG','GAT','GAC','GAA','GAG','GGT','GGC','GGA','GGG'])

    def replacer(self):
        for nucleotide, number in self.numDict.items():
            self.seq = np.char.replace(self.seq, nucleotide, number)

    def Int_0(self):
        self.numDict = {'T':'0',  'C':'1',  'A':'2',  'G':'3', 'U': '0'}

        self.replacer()
        return self.seq.astype(float)

    def Int_1(self):
        self.numDict = {'T':'1',  'C':'2',  'A':'3',  'G':'4'}

        self.replacer()
        return self.seq.astype(float)

    def Real(self):
        self.numDict = {'T':'-1.5',  'C':'0.5',  'A':'1.5',  'G':'-0.5', 'U': '-1.5'}

        self.replacer()
        return self.seq.astype(float)

    def Complex(self):
        def Complex_n():
            self.numDict = {'T':'1',  'C':'-1',  'A':'1',  'G':'-1', 'U': '1'}
            
            self.replacer()
            return self.seq.astype(float)

        def Complex_i():
            self.numDict = {'T':'-1',  'C':'-1',  'A':'1',  'G':'1', 'U': '-1'}
            
            self.replacer()
            return self.seq.astype(float)

        #Merging
        complex_rep = np.concatenate([Complex_n(), Complex_i()], axis=0)
        return complex_rep


    def Atomic(self):
        self.numDict = {'T':'6',  'C':'58',  'A':'70',  'G':'78'}

        self.replacer()
        return self.seq.astype(float)

    def EIIP(self):
        self.numDict = {'T':'0.1335',  'C':'0.1340',  'A':'0.1260',  'G':'0.0806'}

        self.replacer()
        return self.seq.astype(float)

    def PP(self):
        self.numDict = {'T':'1',  'C':'1',  'A':'-1',  'G':'-1'}

        self.replacer()
        return self.seq.astype(float)

    def AT_CG(self):
        self.numDict = {'T':'1',  'C':'-1',  'A':'1',  'G':'-1'}

        self.replacer()
        return self.seq.astype(float)

    def JustA(self):
        self.numDict = {'T':'0',  'C':'0',  'A':'1',  'G':'0', 'R':'1', 'M':'1', 'W':'1', 'H':'1', 'V':'1', 'N': '1', 'X': '1'}

        self.replacer()
        return self.seq.astype(float)

    def JustC(self):
        self.numDict = {'T':'0',  'C':'1',  'A':'0',  'G':'0', 'Y':'1', 'M':'1', 'S':'1', 'B':'1', 'H':'1', 'V':'1', 'N': '1', 'X': '1'}

        self.replacer()
        return self.seq.astype(float)

    def JustG(self):
        self.numDict = {'T':'0',  'C':'0',  'A':'0',  'G':'1', 'R':'1', 'K':'1', 'S':'1', 'B':'1', 'V':'1', 'N': '1', 'X': '1'}

        self.replacer()
        return self.seq.astype(float)

    def JustT(self):
        self.numDict = {'T':'1',  'C':'0',  'A':'0',  'G':'0', 'U':'1', 'Y':'1', 'K':'1', 'W':'1', 'B':'1', 'H':'1', 'N': '1', 'X': '1'}

        self.replacer()
        return self.seq.astype(float)
    
    def Voss(self):
        voss_rep = np.concatenate([self.JustA(), self.JustC(), self.JustG(), self.JustT()], axis=0)
        return voss_rep

    # Calculating the Tetrahedron sides and array

    def Tetrahedron(self):

        def Tetrahedron_A():
            a = np.sqrt(2)/3
            self.numDict = {'T':str(2*a),  'C':str(-1*a),  'A':str(0*a),  'G':str(-1*a), 'U':str(2*a)}

            self.replacer()
            return self.seq.astype(float)

        def Tetrahedron_B():
            b = np.sqrt(6)/3
            self.numDict = {'T':str(0*b),  'C':str(1*b),  'A':str(0*b),  'G':str(-1*b), 'U':str(0*b)}

            self.replacer()
            return self.seq.astype(float)

        def Tetrahedron_C():
            self.numDict = {'T':'-1/3',  'C':'-1/3',  'A':'1',  'G':'-1/3', 'U':'-1/3'}

            self.replacer()
            return self.seq.astype(float)

        #Merging
        tetrahedron_rep = np.concatenate([Tetrahedron_A(), Tetrahedron_B(), Tetrahedron_C()], axis=0)
        return tetrahedron_rep


    '''
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
    '''

if __name__ == "__main__":
    sig = toNumeric()