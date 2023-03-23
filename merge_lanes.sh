#!/bin/bash

for file in $(ls /data/san/data1/users/linda/Soil_samples/raw_fastq); do
file_id=$( echo $file | cut -f1-2 -d_)
files_R1=$( find /data/san/data1/users/linda/Soil_samples/raw_fastq -name "$file_id*_R1_001.fastq.gz")
files_R2=$( find /data/san/data1/users/linda/Soil_samples/raw_fastq -name "$file_id*_R2_001.fastq.gz")
echo $files_R1
echo $files_R2
echo "--------------------------------------------------"
cat $files_R1 > /data/san/data1/users/linda/Soil_samples/lanes_merged/"$file_id"_R1_001.fastq.gz
cat $files_R2 > /data/san/data1/users/linda/Soil_samples/lanes_merged/"$file_id"_R2_001.fastq.gz
done;
