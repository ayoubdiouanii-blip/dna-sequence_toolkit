#project name : "DNA Sequence Analyzer"

#create a random DNA sequence 
import random 
DNA_letters="ATGC"
DNA_sequence=""

for i in range(20):
    DNA_sequence += random.choice(DNA_letters)

print(f"The DNA seq is : {DNA_sequence}") 
#Count A, T, G and C nucleotides

A=print(f"The number of A is : {DNA_sequence.count("A")}")
T=print(f"the number of T is : {DNA_sequence.count("T")}")
G=print(f"the number of G is : {DNA_sequence.count("G")}")
C=print(f"the number of C is : {DNA_sequence.count("C")}")

#Calculate GC content as a percentage
gc_count= DNA_sequence.count("G") + DNA_sequence.count("C")
gc_content = (gc_count / len(DNA_sequence))*100 
print(f"gc_content is : {gc_content}%")
#Find the complementary DNA strand

DNA_COMP_SEQ=DNA_sequence.translate(str.maketrans("ATGC","TACG"))
print(f"DNA_comp_seq is : {DNA_COMP_SEQ}")

#Transcribe DNA into RNA

RNA_seq=DNA_sequence.replace("T","U")
print(f"The RNA seq is : {RNA_seq}")
 
#Detect invalid characters in a sequence

Valid_carac="ATGC"
for i in DNA_sequence:
    if i not in Valid_carac:
        print("error")