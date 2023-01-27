import socket
import re
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('0.0.0.0', 0000))
while True:
    receivedata = s.recv(1024).decode('utf-8')
    print("[+]receivedata=",receivedata)
    splitreceivedata = receivedata.split("\n")
    formula = splitreceivedata[len(splitreceivedata)-1]
    pattern = '(.*) ='
    m = re.search(pattern, formula)
    if m:
        formula = m.group(1)
        print("[+]formula=",formula)
    senddata = str(eval(formula))
    print("[+]senddata=",senddata)
    s.sendall((senddata+"\n").encode("utf-8"))