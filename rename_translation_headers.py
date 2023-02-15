from Bio import SeqIO
import pandas as pd
import os


def list_files(path):
    path_to_files = []
    for root, dir, files in os.walk(path):
        for f in files: 
            if 'japan' in f:
                path_to_files.append(os.path.join(root, f))
    return path_to_files

def get_basename(path_to_file):
    filepath = os.path.splitext(path_to_file)
    base = filepath[0].split('/')[-1]
    return base

df = pd.read_csv('/data/san/data1/users/linda/crAss_DB/circular_genomes/japan4D/genbank_to_contig_map.csv',sep='\t',header=None)
df.columns = ['ncbi_accn','contig']
print(df.head())

japan_opt_translations = list_files('/data/san/data1/users/linda/crAss_DB/optimal_translations_a_i_jap_mon')
for fiLe in japan_opt_translations:
    fiLeName = get_basename(fiLe)
    corrected = f'/data/san/data1/users/linda/crAss_DB/circular_genomes/japan4D/corrected_transl_headers/{fiLeName}.faa'
    with open(fiLe) as original, open(corrected, 'w') as corrected:
        records = SeqIO.parse(fiLe, 'fasta')
        for record in records:
            if record.id:
                try:
                    print('\n')
                    print(record.id)
                    protein_no = record.id.rsplit('_',1)[1]
                    print(protein_no)
                    seq_to_search=(record.id.replace('_k141',''))
                    search_string=seq_to_search.replace('japan4D_','')
                    search_string=search_string.rsplit('_',1)[0]
                    print(search_string)
                    accn = (df.loc[df.contig.str.contains(search_string)]['ncbi_accn'].values[0])
                    print(accn)
                    record.id=f'{accn}_japan4D_{search_string}_{protein_no}'
                    record.description=record.id
                    SeqIO.write(record, corrected, 'fasta')
                except Exception as e:
                    print('printing ERROR')
                    print(f"{e}")
                    record.id=f'{accn}_japan4D_{search_string}'
                    print(record.id)

   
