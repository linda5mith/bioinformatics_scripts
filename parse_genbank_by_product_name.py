from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import re

gb_file = "PROKKA_08252022/PROKKA_08252022.gbk"

with open('DNA_polymerase_crAss.fasta','w') as handle:
    for record in SeqIO.parse(open(gb_file,"r"), "genbank"):
        for feature in record.features:
            if feature.type == 'CDS':
                product=(feature.qualifiers.get('product')[0].split('[')[0].strip())
                if 'DNA polymerase' in product:
                    #print(feature.qualifiers.get('product')[0])
                    #print(feature)
                    header=(f'{record.id} {product} {feature.location}')
                    nt_seq=(feature.extract(record.seq))
                    SeqIO.write(SeqRecord(record.seq,id=header,description=''),handle,'fasta')
    handle.close()
    print('Done')

