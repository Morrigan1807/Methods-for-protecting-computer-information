import os

def check_sign(filename,sign,buffer_size):
  f=open(filename,'rb')
  buffer=f.read(buffer_size)
  sign_positions=[]
  position=buffer_size-1
  while True:
    if sign.startswith(buffer):
      sign_iter=0
      sign_positions.append({'pos':position+1-buffer_size,'part_len':buffer_size})
      while (sign_iter+sign_positions[-1]['part_len'])!=len(sign):
        byte=f.read(1)
        if not byte:
          f.close()
          return []	
        position+=1
        flag_new_part=False
        if byte==sign[sign_iter+sign_positions[-1]['part_len']:sign_iter+sign_positions[-1]['part_len']+1]:
          if (flag_new_part==False):
            sign_positions[-1]['part_len']+=1
          else:
            sign_positions.append({'pos':position,'part_len':1})
        else:
          flag_new_part=True
      f.close()
      return sign_positions
    byte=f.read(1)
    if not byte:
      f.close()
      return []	
    position+=1
    buffer=buffer[1:]+byte
	  
	  
def erase_sign(filename,sign_positions):
  f=open(filename,'rb')
  position=-1
  new_filename=os.path.dirname(filename)+'temp' 
  g=open(new_filename,'wb')
  while True:
    byte=f.read(1)
    if not byte:
      f.close()
      g.close()
      os.remove(filename)
      os.rename(new_filename,filename)
      return True
    position+=1
    position_jumped=False
    for sign_part_pos_len in sign_positions:
      if position==sign_part_pos_len['pos']:
        position+=sign_part_pos_len['part_len']-1
        f.read(sign_part_pos_len['part_len']-1)
        position_jumped=True
        break
    if position_jumped==False:
      g.write(byte)
	  
	  
signs_file='E:\\univer\\MZKI\\labs\\sign.txt'
dir_to_check= "E:\\univer\\MZKI\\labs\\test"
files=[]
for r, d, f in os.walk(dir_to_check):
  for file in f:
    files.append(os.path.join(r, file))
signs_f=open(signs_file,'rb')
signs=signs_f.readlines()
signs_f.close()
for file in files:
  for sign in signs:
    print(sign)
    check_res = check_sign(file,sign,3) 
    if len(check_res) != 0:
      print("This file infected: ", file)
print("Do you want to delete virus signatures?(y/n)")
if input() == 'y':
  for file in files:
    for sign in signs:
      check_res = check_sign(file,sign,3)
      erase_sign(file, check_res)
