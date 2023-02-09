import pandas as pd
from Bio import SeqIO

df = pd.read_csv('/data/san/data1/users/linda/crAss_DB/andrey_igor_base_seqs/crass_ncbi_embargoed.txt')
print(df.head())
X_list = df.X.to_list()

with open('/data/san/data1/users/linda/crAss_DB/andrey_igor_base_seqs/crassvirales_embargoed_fixed_accn.fasta', 'w') as corrected:
    for record in SeqIO.parse('/data/san/data1/users/linda/crAss_DB/andrey_igor_base_seqs/crassvirales_embargoed.fasta','fasta'):
        if record.id in X_list:
            record.id = df.loc[df.X==record.id]['ncbi_acc'].values[0]
            record.description=record.id
            #print(record.description)
            SeqIO.write(record, corrected, 'fasta')
