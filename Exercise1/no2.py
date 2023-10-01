#codon translation dictionary
tc = {
    "F": ["UUU", "UUC"],
    "L": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
    "I": ["AUU", "AUC", "AUA"],
    "M": ["AUG"],
    "V": ["GUU", "GUC", "GUA", "GUG"],
    "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
    "P": ["CCU", "CCC", "CCA", "CCG"],
    "T": ["ACU", "ACC", "ACA", "ACG"],
    "A": ["GCU", "GCC", "GCA", "GCG"],
    "Y": ["UAU", "UAC"],
    "H": ["CAU", "CAC"],
    "Q": ["CAA", "CAG"],
    "N": ["AAU", "AAC"],
    "K": ["AAA", "AAG"],
    "D": ["GAU", "GAC"],
    "E": ["GAA", "GAG"],
    "C": ["UGU", "UGC"],
    "W": ["UGG"],
    "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "G": ["GGU", "GGC", "GGA", "GGG"],
    }

#function to validate if aminoacid input is valid or not
def validate_amino(amino_seq):
    #only accepts the key alphabets that represent each aminoacids
    valid_amino = set(tc.keys())
    for i in amino_seq:
        #if not valid, false
        if i not in valid_amino:
            return False
    #if valid, true and can proceed with other functions
    return True

#function to translate the aminoacid to mRNA sequence and count codon frequency
def mRNA_and_codonfreq(amino_seq):
    mRNA_seq = ''
    codon_freq = {}
    #traverse through each char in the aminoacid sequence
    for i in amino_seq:
        #get the corresponding dictionary of the codon value from tc, 
        #if i is found, add to list, if none then empty list (invalid amino)
        codons = tc.get(i, [])
        if codons :
            #start with first codon
            codon = codons[0]
            #add the translated codon into the mrna sequence
            mRNA_seq += codon
            #increment the frequency of each codon found in the sequence
            codon_freq[codon] = codon_freq.get(codon, 0) + 1
    return mRNA_seq, codon_freq

def main():
    amino_input = input("Input Aminoacid = ")
    #validation process
    if validate_amino(amino_input)==False:
        print("Aminoacid sequence input invalid, try again with valid sequence.")
    elif validate_amino(amino_input)==True:
        print('')

        mRNA_seq, codon_freq = mRNA_and_codonfreq(amino_input)

        print("mRNA = " + mRNA_seq)
        for codon, frequency in codon_freq.items():
            print(f"{codon} = {frequency}")


main()