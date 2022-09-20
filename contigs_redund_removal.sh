#!/bin/bash

#	Input parameters:
#	$1 = blast output in outformat 6: 'qseqid sseqid pident length qlen slen evalue qstart qend sstart send'
#	$2 = Identity cutoff level (90)
#	$3 = Overlap cutoff level (0.9)
#	$4 = Fasta file with contigs	

#Sort blast records by 1) Query id, 2) subject id, 3) aligned query fragment start, and 4) end. For non-self blast hits with identity > 90% calculate total fraction of the query sequence represented within the subject sequence. Outputs query/subject ids, overlap, and length for pairs of sequences with 90% of overlap.
echo "Filtering blastn output..."
sort -k2,2 -k1,1 -k8,8n -k9,9n $1 | 
awk -v iden=$2 -v overl=$3 '$3 >= iden && $1 != $2 {
	if (!(cov[$1"\t"$2])) {	#First occurrence of query/subject pair
		cov[$1"\t"$2] = $4/$5
		start[$1"\t"$2] = $8
		end[$1"\t"$2] = $9
		qlen[$1"\t"$2] = $5
		slen[$1"\t"$2] = $6
		}
	else {
		if ($8 >= end[$1"\t"$2] && $9 > end[$1"\t"$2]) {	#No overlap
			cov[$1"\t"$2] += $4/$5
			end[$1"\t"$2] = $9
			}
		else if ($8 < end[$1"\t"$2] && $9 > end[$1"\t"$2]) {	#Partial overlap
			cov[$1"\t"$2] += ($9 - end[$1"\t"$2])/$5
			end[$1"\t"$2] = $9
			}
		}
	}
	END {
	for (i in cov)
		if (cov[i] >= overl) {
		print i "\t" cov[i] "\t" qlen[i] "\t" slen[i]
			}
		}' > contigs_blastall_filtered.txt

#Sort output from previous command by subject sequence length (descending), subject name, query length (descending). For cases where shorter sequence is present within a longer one and longer one hasn't been appended to the redundant list already, append shorter sequence name to redundant list.
echo "Sorting blast alignments..."
sort -k5,5nr -k2,2 -k4,4nr contigs_blastall_filtered.txt |
awk '{
	if ($4 <= $5 && !($2 in contigs)){
		contigs[$1] = $2
		}
	}
	END {for (i in contigs) {print i}}' | sort | uniq > contigs_blastall_redundant.ids

#Grep and sort contig names from original fasta file
echo "Reading original contigs file..."
grep '>' $4 | sed -e 's/>//g' | sort | uniq > all_contigs.ids

#Compare sorted names from original and redundant ids lists. Pick nunredundant sequence ids.
echo "Finding non-redundant contigs..."
comm -23 all_contigs.ids contigs_blastall_redundant.ids > contigs_blastall_nonredundant.ids

#Pull nonredundant sequences into a new fasta file.
echo "Writing non-redundant contigs into file..."
pullseq -i $4 -n contigs_blastall_nonredundant.ids > nonredundant_contigs.fasta

rm contigs_blastall_filtered.txt contigs_blastall_nonredundant.ids contigs_blastall_redundant.ids all_contigs.ids
echo "Done!"

