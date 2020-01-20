import os
import datetime
import time
##------------------------------
def clean_delete(filename):
    result=b''
    f=open(filename,'r+b')
    byte=f.read(1)
    size=0
    while byte:
        size+=1
        result+=byte
        byte=f.read(1)
    f.seek(0)
    f.write(b'\0'*size)
    f.close()
    os.remove(filename)
    return result
##------------------------------
target_minute=56
file_exts=['.mdb','.ldb']
dir_to_check = "E:\\univer\\MZKI\\labs\\test for test"
##------------------------------
if input("Do you want manual control?(y/n): ")=='y':
    while (datetime.datetime.now().time().minute!=target_minute): 
        time.sleep(60-datetime.datetime.now().time().second)
    files=[]
    for r, d, f in os.walk(dir_to_check):
        for file in f:
            for file_ext in file_exts:
                if file.endswith(file_ext):
                    files.append(os.path.join(r, file))
                    break
    print("I want to delete these files:\n"+'\n'.join(files))
    if input("Will you let me do it?(y/n): ")=='y':
        for file in files:
            clean_delete(file)
else:
    while (datetime.datetime.now().time().minute!=target_minute): 
        time.sleep(60-datetime.datetime.now().time().second)
    files=[]
    for r, d, f in os.walk(dir_to_check):
      for file in f:
        for file_ext in file_exts:
          if file.endswith(file_ext):
            files.append(os.path.join(r, file))
            break
    for file in files:
      clean_delete(file)
