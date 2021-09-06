import hashlib,glob,codecs
for file in glob.glob("./pass*.txt"):
   file_data = open(file, "r+",encoding="utf-8")
   data = file_data.read()
   file_data.close()
   xint = hashlib.sha256(data.encode()).hexdigest()
   with open('hashfile.txt', 'a') as f:
      f.write(str(data) +'::: '+str(xint) +'\n')
