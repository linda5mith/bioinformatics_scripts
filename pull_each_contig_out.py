from Bio import SeqIO, SeqRecord, Seq

records = list(SeqIO.parse('/data/san/data0/users/linda/crAss_DB/pooled_andrey_igor/nonredundant_contigs.fasta', "fasta"))
#lens = [len(record) for record in records]

for record in records:
    record.description = record.id
    SeqIO.write(record, f"/data/san/data0/users/linda/crAss_DB/pooled_andrey_igor/nr_contigs_indiv_genomes/{record.id}.fasta", 'fasta')
    
