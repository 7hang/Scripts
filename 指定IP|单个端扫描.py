#PYthon2.7
//ip.txt

#port_scanner_start.py

#!/usr/bin/python2
# -*- coding:utf-8 -*-
import threading,Queue
import argparse
import time

from port_scanner import portscanner

class AllScanner(threading.Thread):
    def __init__(self,queue,queue1):
        threading.Thread.__init__(self)
        self.queue = queue
        self.queue1 = queue1
    def run(self):
        while True:
            if self.queue.empty():
                break
            else:
                try:
                    ip = self.queue.get(timeout=0.5)
                    port = self.queue1.get(timeout=0.5)
                    portscanner(ip,port)

                except Exception:
                    continue

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',dest='ipsFile',default='ipsFile',help='put local ips filename')
    parser.add_argument('-t',dest='thread_number',type=int,default=50,help='Setting the number of threads')
    parser.add_argument('-u',dest='single_ip',default='single_ip',help='put a single ip')
    parser.add_argument('-p',dest='port',type=int,default='6379',help='Setting the number of port')
    args = parser.parse_args()
    ip_single = str(args.single_ip)
    ips = str(args.ipsFile)
    thread_number = args.thread_number
    port = args.port
    try:
        threads = []
        queue = Queue.Queue()
        queue1 = Queue.Queue()
        if ip_single == 'single_ip':
            ips = open(ips,'r')
            for ip in ips.readlines():
                ip = ip.strip()
                queue.put(str(ip))
                queue1.put(port)
        else:
                ip = ip_single
                queue.put(str(ip))
                queue1.put(port)
        for i in xrange(thread_number):
            threads.append(AllScanner(queue,queue1))
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    except Exception as e:
        parser.print_help()

if __name__ == '__main__':
    time_start = time.time()
    main()
    time_all = time.time()-time_start
    print 'All Finish. Use %ss' % time_all
    
   
#port_scanner.py

from socket import *
import sys

def portscanner(ip,port):
    s = socket(AF_INET,SOCK_STREAM)
    try:
        s.settimeout(8)
        result = s.connect_ex((ip,port))
        if result == 0:
            sys.stdout.write("%s:%d \n" % (ip, port))
    except:
        add_file.close()
        s.close()
    s.close()
 
