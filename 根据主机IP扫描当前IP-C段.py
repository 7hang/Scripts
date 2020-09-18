# -*- coding:UTF-8 -*-

import platform
import socket
import os
import threading
import time
import sys

def my_os():
 return platform.system()
 
def my_ip():                                             
    return socket.gethostbyname(socket.gethostname())
 
def ping_ip(ip):                                        
    if my_os() == 'Windows':
        p_w = 'n'
    elif my_os() == 'Linux':
        p_w = 'c'
    else:
        print('not support')
        sys.exit()
    output = os.popen('ping -%s 1 %s'%(p_w,ip)).readlines()
    for w in output:
        if str(w).upper().find('TTL')>=0:
            print(ip,'ok')        
 
def ping_all(ip):                                      
    pre_ip = (ip.split('.')[:-1])
    for i in range(1,256):
        add = ('.'.join(pre_ip)+'.'+str(i))
        #ping_ip(add)
        threading._start_new_thread(ping_ip,(add,))
        time.sleep(0.1)
 
 
if __name__ == '__main__':
    ping_all(my_ip())
