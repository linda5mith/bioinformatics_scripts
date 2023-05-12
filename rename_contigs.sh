for i in $(ls /data/san/data1/users/linda/Soil_samples/spades/contigs_1000); do
file_id=$( echo $i | cut -f1 -d c)
sed -i "s/^>/>$file_id/g" /data/san/data1/users/linda/Soil_samples/spades/contigs_1000/"$i"
done;
