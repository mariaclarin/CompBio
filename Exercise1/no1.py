#function to validate the input dna sequence
def validate_dna(dna_seq):
    #setting the valid DNA chars (both uppercase and lowercase)
    dna_chars = set("ACGTacgt")
    #checking if each char is a valid DNA char
    for char in dna_seq:
        if char not in dna_chars:
            return False
    return True

#function to return the reverse complement of the DNA sequence based on Ms Sera's notes
def complement(dna_seq):
    comp = ""
    for i in dna_seq.upper():
        if i == "A":
            comp = "T" + comp
        elif i == "T":
            comp = "A" + comp
        elif i == "G":
            comp = "C" + comp
        elif i == "C":
            comp = "G" + comp
    #added the slicing of [::-1] to reverse the comp string so the correct output is returned
    #if not, the complement string will end up being reversed (ex: input=TTACGA complement=TCGTAA (incorrect))
    return comp[::-1]

#function to replace all 'T' DNA value to 'U' mRNA value
def mRNA(comp):
    mRNA_seq = comp.replace('T', 'U')
    return mRNA_seq

#function to translate the mRNA sequence into aminoacids
def aminoAcid(mRNA_seq):
    #codon table dictionary
    tc = {
    "UUU": "Phenylalanine (F)", "UUC": "Phenylalanine (F)", 
    "UUA": "Leucine (L)", "UUG": "Leucine (L)", "CUU": "Leucine (L)", "CUC": "Leucine (L)", "CUA": "Leucine (L)", "CUG": "Leucine (L)",
    "AUU": "Isoleucine (I)", "AUC": "Isoleucine (I)", "AUA": "Isoleucine (I)", 
    "AUG": "Methionine (M)",
    "GUU": "Valine (V)", "GUC": "Valine (V)", "GUA": "Valine (V)", "GUG": "Valine (V)",
    "UCU": "Serine (S)", "UCC": "Serine (S)", "UCA": "Serine (S)", "UCG": "Serine (S)",
    "CCU": "Proline (P)", "CCC": "Proline (P)", "CCA": "Proline (P)", "CCG": "Proline (P)",
    "ACU": "Threonine (T)", "ACC": "Threonine (T)", "ACA": "Threonine (T)", "ACG": "Threonine (T)",
    "GCU": "Alanine (A)", "GCC": "Alanine (A)", "GCA": "Alanine (A)", "GCG": "Alanine (A)",
    "UAU": "Tyrosine (Y)", "UAC": "Tyrosine (Y)", 
    "UAA": "Stop (*)", "UAG": "Stop (*)",
    "CAU": "Histidine (H)", "CAC": "Histidine (H)", 
    "CAA": "Glutamine (Q)", "CAG": "Glutamine (Q)",
    "AAU": "Asparagine (N)", "AAC": "Asparagine (N)", 
    "AAA": "Lysine (K)", "AAG": "Lysine (K)",
    "GAU": "Aspartic Acid (D)", "GAC": "Aspartic Acid (D)", 
    "GAA": "Glutamic Acid (E)", "GAG": "Glutamic Acid (E)",
    "UGU": "Cysteine (C)", "UGC": "Cysteine (C)", 
    "UGA": "Stop (*)", 
    "UGG": "Tryptophan (W)",
    "CGU": "Arginine (R)", "CGC": "Arginine (R)", "CGA": "Arginine (R)", "CGG": "Arginine (R)",
    "AGU": "Serine (S)", "AGC": "Serine (S)", 
    "AGA": "Arginine (R)", "AGG": "Arginine (R)",
    "GGU": "Glycine (G)", "GGC": "Glycine (G)", "GGA": "Glycine (G)", "GGG": "Glycine (G)",
    }
    amino_seq = ''
    #traverse the mRNA sequence by every 3 chars
    for i in range(0, len(mRNA_seq), 3):
        codon =mRNA_seq[i:i+3]
        aminoacid = tc.get(codon,'')

        if aminoacid: #if not empty
            amino_seq += aminoacid
            # Add ' - ' between aminoacids
            if i+3 <len(mRNA_seq):
                amino_seq += " - "
    return amino_seq

#main function to run all the functions together
def main():
    dna_seq = input("Input DNA = ")
    if validate_dna(dna_seq)==False:
        print("DNA input invalid, try again with a valid sequence.")
    elif validate_dna(dna_seq)==True:
        print("")

        comp = complement(dna_seq)
        print("Complement = " + comp)

        mRNA_seq = mRNA(comp)
        print("mRNA = "+ mRNA_seq)

        amino = aminoAcid(mRNA_seq)
        print("Aminoacid = " + amino)

main()