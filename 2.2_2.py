import simplecrypt
import os
f_path = os.path.join(r'C:\Users\Gavr\Downloads', 'encrypted.bin')
pswrd_path = os.path.join(r'C:\Users\Gavr\Downloads', 'passwords.txt')
with open(f_path, "rb") as inp:
    encrypted = inp.read()
inp.close()

pswrd_list = []
with open(pswrd_path, "rb") as inp:
    for line in inp:
        pswrd_list += [line.strip()]
inp.close()

for pswrd in pswrd_list:
    try:
        res = simplecrypt.decrypt(pswrd, encrypted)
        print(pswrd, res.decode('utf8'))
    except Exception:
        print(pswrd, 'DecryptionException')