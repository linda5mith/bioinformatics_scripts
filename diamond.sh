# $1 path to matches.tsv
# $2 path to protein_lengths.txt

#grep '>' pooled_ICTV_proteomes.faa | sed s'/>//' > protein_metadata_catalog.txt
#sort protein_metadata_catalog.txt > tmp && mv tmp protein_metadata_catalog.txt
sort -k 2 -o matches_sort.tsv $1 && mv matches_sort.tsv matches.tsv

# join protein_lengths to calculate coverage
join -1 2 -2 1  matches.tsv $2 | awk '{swap=$1;$1=$2;$2=swap;print $0}' > tmp && mv tmp matches.tsv

# calculate coverage
awk '{$(NF+1) = 100*(($10-$9)/$13); print}' matches.tsv > matches_cov.tsv && mv matches_cov.tsv matches.tsv

# sort by target, %id, length, e-value,r, coverage
sort -k 2,2 -k 3,3rn -k 4,4rn -k 10,10rn matches.tsv > matches_sort.tsv 

# join protein metadata - protein name and virus
join -1 2 -2 1  matches_sort.tsv protein_metadata_catalog.txt | awk '{swap=$1;$1=$2;$2=swap;print $0}' > matches.tsv

# One last sort by both query and target
sort -k1,1 -k 2,2 -k 3,3rn -k 4,4rn -k 10,10rn matches.tsv > matches_sort.tsv && mv matches_sort.tsv matches.tsv

# Sum overlapping alignments to get total length


