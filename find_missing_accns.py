import os

# get path to every file in folder
def list_files(path):
    path_to_files = []
    for root, dir, files in os.walk(path):
        for f in files: 
            if 'faa' in f:
                path_to_files.append(os.path.join(root, f))
    return path_to_files

def get_basename(path_to_file):
    filepath = os.path.splitext(path_to_file)
    base = filepath[0].split('/')[-1]
    return base

downloaded_proteomes = []
igor_proteomes_download = list_files('/data/san/data0/users/linda/crAss_DB/crAss_igor/proteomes')
for file in igor_proteomes_download:
    f = get_basename(file)
    downloaded_proteomes.append(f)


igor_accns = []
with open('/data/san/data0/users/linda/ICTV_DB/metadata/crassvirales_accessions_ICTV.csv','r') as f:
    for line in f:
        igor_accns.append(line.strip())

#print(downloaded_proteomes)

#find empty files
count = 0
empty_file = []
for file in igor_proteomes_download:
    if os.stat(file).st_size == 0:
        count+=1
        empty_file.append(file)
print(f'Number of empty files is: {count}')
print(empty_file)

c = sorted(list(set(igor_accns)) + list(set(downloaded_proteomes)))
#print(c) 
print(len(c))
print(len(igor_accns)) #635 potential crass
#print(list(set(igor_accns)-set(downloaded_proteomes)))
