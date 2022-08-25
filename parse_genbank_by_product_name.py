from Bio import SeqIO
import re

gb_file = "PROKKA_08252022/PROKKA_08252022.gbk"

features=[]
for record in SeqIO.parse(open(gb_file,"r"), "genbank"):
    for f in record.features:
        if f.type == 'CDS':
            product=(f.qualifiers.get('product')[0].split('[')[0].strip())
            #print(product)
            if 'DNA polymerase' in product:
                print(f.seq)
