def to_rna(dna_strand):
    nucl = {'G': 'C', 'C': 'G', 'T': 'A', 'A':'U'}
    return_string = ""
    for char in dna_strand:
        return_string += nucl[char]
    return return_string
