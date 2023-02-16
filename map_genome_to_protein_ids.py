import pandas as pd
from Bio import SeqIO
import os
import argparse

# translations = pd.read_csv('/data/san/data0/users/linda/crAss_DB/all_sources_merged/optimal_translations.csv')
# print(translations.head())


# get path to every file in folder
def list_files(path):
    path_to_files = []
    for root, dir, files in os.walk(path):
        for f in files: 
            if 'gff' not in f:
                path_to_files.append(os.path.join(root, f))
    return path_to_files


def get_basename(path_to_file):
    filepath = os.path.splitext(path_to_file)
    base = filepath[0].split('/')[-1]
    return base


def link_genome_to_proteome(path_to_files):
    protein_lengths={}
    protein_dict={}
    for seq in path_to_files:
        nt_ID = get_basename(seq)
        #print(nt_ID)
        #for record in SeqIO.parse(seq,'fasta'):
        records = list(SeqIO.parse(seq,'fasta'))
        record_ids = [record.id for record in records]
        lens = [len(record) for record in records]
        protein_dict[nt_ID] = record_ids
        protein_lengths[nt_ID] = [lens]
        #print(protein_lengths)
    df_protein_map = pd.DataFrame(protein_dict.items())
    df_protein_lens = pd.DataFrame(protein_lengths.items())
    df_protein_map.columns = ['ID','protein_IDs']
    df_protein_lens.columns = ['ID','protein_lens']
    df_protein_map = df_protein_map.sort_values(by='ID')
    df_merged = df_protein_map.merge(df_protein_lens,left_on='ID',right_on='ID')
    df_merged.to_csv('genome_to_protein_metadata.csv',index=False)
    print(df_merged.head())
    df_merged.T.to_csv('output.csv', header=False, index=False)



def is_valid_folder(parser, arg):
    if not os.path.exists(arg):
        parser.error("The folder %s does not exist!" % arg)
    else:
        return arg

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="path to translations")
    parser.add_argument("-i", dest="foldername", required=True,
                        help="input folder to translations", metavar="FOLDER",
                        type=lambda x: is_valid_folder(parser, x))
    args = parser.parse_args()
    fIles = list_files(args.foldername)
    link_genome_to_proteome(fIles)



