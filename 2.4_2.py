import os, zipfile
archpath = 'test_2.4_2/main.zip'
zipFile = zipfile.ZipFile(archpath)
res_path = archpath[:-4]
zipFile.extractall(res_path)
zipFile.close()

res_list = []
for currentdir, dirs, files in os.walk(res_path):
    for file in files:
        print(file[-3:])
        if file[-3:] == '.py':
            new_path = os.path.relpath(currentdir, res_path)

            if new_path not in res_list:
                res_list.append(os.path.relpath(currentdir, res_path))

res_list.sort()

with open(os.path.join(res_path, 'ans.txt'), 'w') as f:
    for path in res_list:
        f.write(path+'\n')