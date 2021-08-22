# -*- coding: utf-8 -*-
import subprocess
import csv
import codecs
import datetime

class Ping(object):
    def test(self, hosts):
        result = []
        for host in hosts:
            # pingコマンド
            ping = subprocess.Popen(["ping", host],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            # ping試験
            out, error = ping.communicate()
            print("■" + host)
            print("----------------------")
            print(out.decode('Shift-JIS'))
            print("----------------------")
            result.append(out.decode('Shift-JIS'))

        hosts = [hosts]
        hosts.append(result)
        hosts = list(map(list, zip(*hosts)))  
        return hosts

    def load_csv(self, filepath):
        f = codecs.open(filepath, "r")
        csv_data = csv.reader(f)
        data = [ e[0] for e in csv_data]
        f.close()
        return data
        
    def save_csv(self, filepath, data):
        with open(filepath, 'w', newline='') as f:    #newline=''を追加した
            writer = csv.writer(f)
            writer.writerows(data)   
            

ping = Ping()

# ipアドレスのリストをロード
hosts = ping.load_csv("iplist.csv")   

# ping試験
data = ping.test(hosts)

# 結果を保存
date = datetime.datetime.now()
ping.save_csv("iptest-{0:%Y%m%d_%H%M%S}.txt".format(date), data)