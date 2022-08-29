#!/bin/bash

# Download gene and protein sequences by gene-id ncbi datasets toolkit
# Unzips folder
# 1. conda activate ncbi_datasets
# 2. yes Y | ./download_ncbi_by_gene_id.sh # replace README.md? [y]es, [n]o, [A]ll, [N]one, [r]ename: A

for i in $(cat crass_dna_pol_ids.txt); do
    datasets download gene gene-id $i --filename crAss_dna_pols/$i.zip
    # Unzipping the file naturally decompresses to ncbi_dataset, to suppress this: rename extraction directory while unzipping
    unzip -d crAss_dna_pols/$i -j  crAss_dna_pols/$i.zip
done;

rm *.zip




