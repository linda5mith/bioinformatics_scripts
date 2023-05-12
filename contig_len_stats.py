import pandas as pd
from Bio import SeqIO
import os
import numpy as np

files = []
len_min = []
len_max = []
len_avg = []
len_median = []
for fIle in os.listdir('/data/san/data1/users/linda/Soil_samples/spades/contigs_1000'):
    print(fIle)
    try:
        lengths = []
        for record in SeqIO.parse(f'/data/san/data1/users/linda/Soil_samples/spades/contigs_1000/{fIle}', "fasta"):
                lengths.append(len(record.seq))
        files.append(fIle.split('.')[0])
        #print(lengths)
        print(max(lengths))
        len_min.append(min(lengths))
        len_max.append(max(lengths))
        len_avg.append(np.mean(lengths))
        len_median.append(np.median(lengths))
    except Exception as e:
        print(e)

print(len(files), len(len_min), len(len_max), len(len_avg), len(len_median))
    
dict = {'file':files, 'len_min':len_min, 'len_max':len_max, 'len_avg':len_avg, 'len_median':len_median}
df = pd.DataFrame.from_dict(dict, orient='index')
df = df.transpose()
df.to_csv('/data/san/data1/users/linda/Soil_samples/exploratory_analysis/contig_length_stats.csv', index=False)

# CA13_S21_003_004_contigs.fasta
# min() arg is an empty sequence
