//ip.txt IP文本
//Pwd.txt  密码文本

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import sys

def check(ip, port, timeout):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        s.send("INFO\r\n")
        result = s.recv(1024)
        if "redis_version" in result:
            return u"IP:{0}存在未授权访问".format(ip)
        elif "Authentication" in result:
            with open('Pwd.txt','r') as f:
                passwds = f.readlines()
            for pwd in passwds:
                passwd = pwd.strip("\n")
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, int(port)))
                s.send("AUTH %s\r\n" %(passwd))
                result = s.recv(1024)
                if 'OK' in result:
                    return u"IP:{0} 存在弱口令，密码：{1}".format(ip,passwd)
                else:pass
        else:pass
        s.close()
    except Exception, e:
        pass

if __name__ == '__main__':
    # default Port
    port="6379"
    with open('ip.txt','r') as  f:
        ips = f.readlines()
        for i in ips:
            ip = i.strip("\n")
            result = check(ip,port,timeout=10)
            print(result)
