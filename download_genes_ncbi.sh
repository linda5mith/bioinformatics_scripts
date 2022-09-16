 esearch -db gene -query "crAssphage major capsid protein" | efetch -format docsum | grep 'Id' | sed -e 's/<[^>]*>//g' | xargs -n 1 sh -c 'datasets download gene gene-id "$0" --filename "$0"'
