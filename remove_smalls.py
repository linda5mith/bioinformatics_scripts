from Bio import SeqIO
import os

path = "/data/san/data1/users/linda/Soil_samples/spades/contigs"

# output path for contigs with length >= 1000
# Then pullseq these contigs from file
outpath = "/data/san/data1/users/linda/Soil_samples/spades/contigs_1000"


for fIle in os.listdir(path):
    seqs_over_1000 = []
    with open(os.path.join(outpath,fIle),'w') as output:
        print(output)
        for record in SeqIO.parse(os.path.join(path,fIle), "fasta"):
            if len(record.seq) >= 1000:
                SeqIO.write(record, output, 'fasta')


