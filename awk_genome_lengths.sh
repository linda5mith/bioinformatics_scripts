awk '/^>/ {if (seqlen){print seqlen}; printf$0"," ;seqlen=0;next; } { seqlen += length($0)}END{print seqlen}' pooled_translations.faa > pooled_genome_lengths.txt
