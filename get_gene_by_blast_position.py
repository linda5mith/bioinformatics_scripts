import pandas as pd
import numpy as np
from Bio import SeqIO

# read in blast output
# read fasta containing query sequences
# read fasta containing database sequences

#magicblast_out = pd.read_csv('/data/san/data0/users/linda/crAss/crass_find_new_seqs/SRA_sequence_searches/nucl/crAss_MCP_magicblast_env_20_09_22.txt',sep='\t',skiprows=2)

headerList = ['query','target','pident', "length", "mismatch", "gapopen","qstart", "qend", "sstart", "send", "evalue", "bitscore"]
blast_out = pd.read_csv('/data/san/data0/users/linda/crAss/crass_find_new_seqs/SRA_sequence_searches/environment_raw/SRR15714818/meta_spades/SRR15714818_vs_crAss_outfmt6.txt',sep='\t',names=headerList)
blast_out.sort_values(by=['query','sstart','send'],ascending=False)

query_seqs = "/data/san/data0/users/linda/crAss/crass_find_new_seqs/Andrey_base_data/redundancy_removal/nonredundant_contigs.fasta"
db_seqs = "/data/san/data0/users/linda/crAss/crass_find_new_seqs/SRA_sequence_searches/environment_raw/SRR15714818/meta_spades/nonredundant_contigs.fasta"

querySeqs = SeqIO.parse(query_seqs, "fasta")
dbSeqs = SeqIO.parse(db_seqs, "fasta")

#print(record.seq[80171:80243])

query_names = blast_out['query'].to_list()
db_names = blast_out['target'].to_list()

record_dict={}
for record in dbSeqs:
    if record.id in query_names:
        record_dict[record.id] = str(record.seq)

for index, row in blast_out.iterrows():
    if row['query'] in record_dict.keys():
        print(record_dict.get(row['query'])[int(row['qstart']):int(row['qend'])])






