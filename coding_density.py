import os
from Bio import SeqIO
import pandas as pd
import statistics

# get path to every file in folder
def list_files(path):
    path_to_files = []
    for root, dir, files in os.walk(path):
        for f in files: 
            if 'faa' in f:
                path_to_files.append(os.path.join(root, f))
    return path_to_files

def get_basename(path_to_file):
    filepath = os.path.splitext(path_to_file)
    base = filepath[0].split('/')[-1]
    return base

proteome_11 = list_files('/data/san/data0/users/linda/ICTV_DB/crAss_proteomes_11')
proteome_15 = list_files('/data/san/data0/users/linda/ICTV_DB/crAss_proteomes_15')
nuccore = list_files('/data/san/data0/users/linda/ICTV_DB/crAss_nuccore')

# print(proteome_11)

virus_cds_11 = {}
avg_lens = []
for file in proteome_11:
    virus = get_basename(file)
    records = list(SeqIO.parse(file, "fasta"))
    lens = [len(record) for record in records]
    virus_cds_11[virus]=sum(lens)
    if lens:
        avg = statistics.mean(lens)
        avg_lens.append(avg)
    else:
        avg_lens.append(0)

# print(virus_cds_11)
df_11 = pd.DataFrame(virus_cds_11.items()) 
df_11['avg_orf_len_11'] = avg_lens
df_11.to_csv('df_11.csv',index=False)

print(df_11.head())

virus_cds_15 = {}
avg_lens = []
for file in proteome_15:
    virus = get_basename(file)
    records = list(SeqIO.parse(file, "fasta"))
    lens = [len(record) for record in records]
    virus_cds_15[virus]=sum(lens)
    if lens:
        avg = statistics.mean(lens)
        avg_lens.append(avg)
    else:
        avg_lens.append(0)

#print(virus_cds_15)
df_15 = pd.DataFrame(virus_cds_15.items()) 
df_15['avg_orf_len_15'] = avg_lens
df_15.to_csv('df_15.csv',index=False)

print(df_15.head())

# # get genome lengths
# genome_length = {}
# for file in nuccore:
#     virus = get_basename(file)
#     with open(file) as handle:
#         for record in SeqIO.parse(handle,'fasta'):
#             #virus_lengths.append(len(record.seq))
#             genome_length[virus] = len(record.seq)

# df_length = pd.DataFrame(genome_length.items())
# df_length.to_csv('df_lengths.csv',index=False)

# some translation files are empty e.g. BK024708.1

df_11 = pd.read_csv('df_11.csv',names=['Genome','ORF_lens_11','avg_orf_len_11'])
df_15 = pd.read_csv('df_15.csv',names=['Genome','ORF_lens_15','avg_orf_len_15'])
df_len = pd.read_csv('df_lengths.csv',names=['Genome','Genome_lens'])
df_m = pd.merge(df_11, df_15, left_on=['Genome'], right_on=['Genome'])
print(df_m.head())
df_mm = pd.merge(df_m, df_len)
print(df_mm)
df_mm.to_csv('crass_11_vs_15.csv',index=False)
