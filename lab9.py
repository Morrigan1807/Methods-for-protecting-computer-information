import time
alphabet='0123456789qwertyuiopasdfghjklzxcvbnm'
def rec_password(target_password,built_prefix,remaining_symbols):
    if remaining_symbols==0:
        if built_prefix==target_password:
            return built_prefix
        else:
            return ''
    else:
        for sym in alphabet:
            temp_res=rec_password(target_password,built_prefix+sym,remaining_symbols-1)
            if temp_res!='':
                return temp_res
        return ''


    
def bust_password(target_password):
    buster_size=1
    buster=''
    time_start=time.time()
    while rec_password(target_password,'',buster_size)!=target_password:
        buster_size+=1
    time_end=time.time()
    return {"spent_time":time_end-time_start,"pass_length":buster_size}

print("Enter password: ")
print(bust_password(input()))
        
