import random
random.seed()

def encryption (str_len, n_keys, in_cipher, keys):
    for i in range (0, str_len, 2): 
        for k in range (0, n_keys):
            save = in_cipher[i + 1]
            in_cipher[i] = (in_cipher[i] + keys[k] // 2) % 256
            in_cipher[i] ^= in_cipher[i+1]
            in_cipher[i+1] = in_cipher[i]
            in_cipher[i] = save
    return in_cipher

print("Enter your string: ")
input_str = input()

str_len = len(input_str)  ##create list of codes
flag = False
if len(input_str) % 2 != 0:
    flag = True
    str_len += 1
    in_cipher = [0 for i in range (0, str_len)]
    for i in range (0, str_len - 1):
        in_cipher[i] = ord(input_str[i])
    in_cipher[str_len-1] = random.randrange(0, 255)
else:
    in_cipher = [0 for i in range (0, str_len)]
    for i in range (0, str_len):
        in_cipher[i] = ord(input_str[i])

print(in_cipher)

print("Enter number of rounds: ") ##create list of keys
n_keys = int(input())
keys = [0 for i in range (0, n_keys)]
for i in range (0, n_keys):
    keys[i] = random.randrange(0, 100)

print (keys)

in_cipher = encryption (str_len, n_keys, in_cipher, keys)

print("Reult of encription: ")
for i in range (0, str_len):
    print(in_cipher[i], end = ' ')

##decription
##keys, im_cipher, n_keys

for i in range (0, str_len, 2):
    for k in range (n_keys - 1, -1, -1):
        save = in_cipher[i + 1]
        in_cipher[i+1] = in_cipher[i]
        in_cipher[i] = save
        in_cipher[i] ^= in_cipher[i+1]
        in_cipher[i] = (in_cipher[i] - keys[k] // 2) % 256
        
print("\nResult of decription: ")
if flag == True:
    str_len -= 1
for i in range (0, str_len):
    print(chr(in_cipher[i]), end = '')
