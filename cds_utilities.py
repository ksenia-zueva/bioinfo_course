#Coding sequences utilities

def test_if_seq_begins_start_codon(sequence) :
    if sequence[0:3].upper() == "ATG" :
        return("correctStart")
    else :
        return("wrongStart")