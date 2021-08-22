import subprocess

hosts = ["192.168.0.1","192.168.0.18","127.0.0.1"]

for host in hosts:
    res = subprocess.run(["ping",host,"-n","1"],stdout=subprocess.PIPE)

    print(res.stdout.decode("cp932"))
    
    if res.returncode == 0 :
        print("成功\n\n")
    else:
        print("失敗\n\n")
    print("-----------------------------")