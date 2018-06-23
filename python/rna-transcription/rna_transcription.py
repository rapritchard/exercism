def to_rna(dna_strand):
    rna_strand = []
    dna_to_rna = {'A': 'U', 'C' : 'G', 'G' : 'C', 'T' : 'A'}
    for dna in dna_strand:
        for key, value in dna_to_rna.items():
            if dna == key:
                rna_strand.append(value)
            elif dna not in dna_to_rna:
                raise ValueError("Character has to be G, C, T, or A")
    return "".join(rna_strand)
    # Could also use:
    # rna_strand = dna_strand.maketrans('GCTA'. 'CGAU')
    # This makes a translation table suitable to pass to translate()
    # then return dna_strand.translate(rna_strand)
