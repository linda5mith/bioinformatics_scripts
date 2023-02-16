# $1 = path to fasta file

name=$(basename "$1" .fasta)
echo $1
echo "$name"

awk '/^>/ {if (seqlen){print seqlen}; printf$0"," ;seqlen=0;next; } { seqlen += length($0)}END{print seqlen}' $1 > "$name"_lengths.txt

sed -i s'/>//g' "$name"_lengths.txt

cat "$name"_lengths.txt | rev | sed "s/,/:/2g" | sed 's/://' | rev > "$name"_clean.csv
rm "$name"_lengths.txt && mv "$name"_clean.csv "$name"_lengths.txt
