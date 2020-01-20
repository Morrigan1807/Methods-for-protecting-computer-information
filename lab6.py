import os
import hashlib
os.getcwd()

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(10240), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def check():
    files = []
    # r=root, d=directories, f = files
    path = "C:\\Users\\Nika\\Desktop\\univer\\MZKI\\labs\\test"
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
            
    cs = dict()
    for i in files:
        cs[i] = md5(i)
    return cs

file_save = "C:\\Users\\Nika\\Desktop\\univer\\MZKI\\labs\\check.txt"    
if os.path.isfile(file_save) == False:
    f =  open (file_save, 'w')
    files_and_cs = check()
    for file in files_and_cs.keys():
        f.write(file +' '+files_and_cs[file]+'\n')
    f.close()
else:
    f =  open (file_save, 'r')
    files_and_cs = check()

    files_and_cs_now = dict()
    for line in f:
        print (line)
        l = line.replace('\n','').split(' ')
        files_and_cs_now[l[0]] = l[1]
    f.close()
    flag = False
    for file in files_and_cs_now.keys():
        if file in files_and_cs.keys():
            if files_and_cs_now[file] != files_and_cs[file]:
                flag = True
                print("File " +  file + " has checksum changed!")
    if flag == False:
        print("All files successfully passed the checking!")
