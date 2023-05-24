#$1 is ICTV_translations.faa
#$2 is translations_nr_contigs.faa 

# Input: protein fasta file
# >ref|NP_039777.1| ORF B-251 [Sulfolobus spindle-shaped virus 1]
# MVRNMKMKKSNEWLWLGTKIINAHKTNGFESAIIFGKQGTGKTTYALKVAKEVYQRLGHE
# PDKAWELALDSLFFELKDALRIMKIFRQNDRTIPIIIFDDAGIWLQKYLWYKEEMIKFYR
# IYNIIRNIVSGVIFTTPSPNDIAFYVREKGWKLIMITRNGRQPDGTPKAVAKIAVNKITI
# IKGKITNKMKWRTVDDYTVKLPDWVYKEYVERRKVYEEKLLEELDEVLDSDNKTENPSNP
# SLLTKIDDVTR

# Output: gene-to-geonome mapping file
# protein_id,contig_id,keywords
# ref|NP_039777.1|,Sulfolobus spindle-shaped virus 1,ORF B-251

# Extract protein ID
grep '>' $1 | sed 's/>//g' | awk -F' ' '{print $1}' > proteins.tmp

# Extract everything between brackets to get contig_ID
grep '>' $1 |  sed 's/>//g' | awk -F'[][]' '{print $2}' > contig_id.tmp

# If $3 field contains '[',print only $2
# Else print $2,$3
grep '>' $1 |  sed 's/>//g' | awk -F' ' '{if ($3 ~ /\[/) print $2; else if($4 ~ /\[/)print $2,$3; else print $2,$3,$4;}' > keywords.tmp

paste -d , proteins.tmp contig_id.tmp > protein_contig.tmp
echo "protein_id,contig_id,keywords" >> proteins.csv;
paste -d , protein_contig.tmp keywords.tmp >> proteins.csv;
 
# Clean all whitespace from file
sed -i '/^$/d' proteins.csv
#rm *.tmp

cat proteins.csv >> protein_to_genome_vcontact2_mapping.csv

# #echo "contig_id,protein_id,keywords" > proteins.csv;

# grep '>' $2 | sed 's/>//g' | cut -d# -f1 | sed 's/[[:blank:]]//g' | sed 's/$/,/'  > headers.tmp;
# cat headers.tmp | sed 's/$/None/' > proteins.tmp;
# paste -d "" headers.tmp proteins.tmp > proteins2.csv;
# sed -i '/^$/d' proteins2.csv
# rm *.tmp

# cat proteins.csv proteins2.csv >> protein_to_genome_vcontact2_mapping.csv
# rm proteins.csv proteins2.csv

# sort -s -n -k 1,1 -o proteins.csv proteins.csv



# grep '>' $1 | sed 's/>//g' | sed 's/ # .*//g'  > headers.tmp;
# cat headers.tmp | sed 's/$/,None/' > proteins.tmp;
# cat headers.tmp | sed 's/_[^_]*$/,/' > contigs.tmp;
# paste contigs.tmp proteins.tmp | sed 's/\t//g' >> proteins.csv;
# rm *.tmp;
# sed -i 's/ # .*//g' $1;


#(head -n 1 proteins.csv | sort -s -n -k 1,1) > proteins2.csv

#Creating proteins csv file for ICTV proteome file
# echo "contig_id,protein_id,keywords" > proteins.csv;

# grep '>' /backup/user_data/linda/fecal_dynamics_2022/ICTV_database/ICTV_ncbi_protein_sequences.faa | sed 's/>//g' | sed 's/,//g'| sed 's/ # .*//g' | sed 's/$/,/'  > headers.tmp;
# cat headers.tmp | sed 's/$/None/' > proteins.tmp;
# paste -d "" headers.tmp proteins.tmp

# cat headers.tmp | sed 's/$/,None/' > proteins.tmp;
# cat headers.tmp | sed 's/$/,/' > protein_names.tmp
# paste -d "" protein_names.tmp proteins.tmp > proteins.csv

