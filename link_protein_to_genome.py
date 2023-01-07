import pandas as pd
from Bio import SeqIO

translations = pd.read_csv('/data/san/data0/users/linda/crAss_DB/all_sources_merged/optimal_translations.csv')
print(translations.head())

genome_dict={}
protein_dict={}

for index, row in translations.iterrows():
    try:
        if row['Optimal Table'] == 11:
            seq = row['contig']
            #print(seq)
            for record in SeqIO.parse(f'/data/san/data0/users/linda/crAss_DB/all_sources_merged/all_individual_genomes/{seq}.fasta','fasta'):
                #print(len(record.seq))
                genome_dict[seq] = len(record.seq)
            records = list(SeqIO.parse(f'/data/san/data0/users/linda/crAss_DB/all_sources_merged/table_11/{seq}.faa','fasta'))
            record_ids = [record.id for record in records]
            #print(record_ids)
            protein_dict[seq] = record_ids
        else:
            seq = row['contig']
            #print(seq)
            for record in SeqIO.parse(f'/data/san/data0/users/linda/crAss_DB/all_sources_merged/all_individual_genomes/{seq}.fasta','fasta'):
                #print(len(record.seq))
                genome_dict[seq] = len(record.seq)
            records = list(SeqIO.parse(f'/data/san/data0/users/linda/crAss_DB/all_sources_merged/table_15/{seq}.faa','fasta'))
            record_ids = [record.id for record in records]
            #print(record_ids)
            protein_dict[seq] = record_ids
    except Exception as e:
        print(e)


df_protein_genome_linked = pd.DataFrame.from_dict(protein_dict, orient='index').T
print(df_protein_genome_linked.head())
