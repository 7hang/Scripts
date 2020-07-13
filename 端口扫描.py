#TCP connect Port Scanner Threads
from socket import *
import threading

lock = threading.Lock()
openNum = 0
threads = []

def portScanner(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        openNum+=1
        print('[+] %d open' % port)
        lock.release()
        s.close()
    except:
        pass

def main():
    setdefaulttimeout(1)
    for p in range(1,30000):
        t = threading.Thread(target=portScanner, args=('localhost',p))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('[*] The scan is complete!')
    print('[*] A total of %d open port' % (openNum))

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    #TCP connect Port Scanner Threads 3389
#tesr.py
from socket import *
import threading
from gla import getipdict

lock = threading.Lock()
openNum = 0
threads = []

def portScanner(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        openNum+=1
        print('[+] %d open' % port)
        lock.release()
        s.close()
    except:
        pass

def main():
    setdefaulttimeout(1)
    IPss = getipdict()
    IP = IPss.get_ip_dict()

    for host in IP:
        t = threading.Thread(target=portScanner, args=(host,3389))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('[*] The scan is complete!')
    print('[*] A total of %d open port' % (openNum))

if __name__ == '__main__':
    main()


#IP.txt
localhost
10.137.21.23
10.137.154.219
10.137.154.123


#gla.py
class getipdict():
    def __init__(self):
        pass

    def get_ip_dict(self):
        ip_dict = []
        with open('IP.txt','r') as f:
            for line in f.readlines():
                line = line.strip('\n')
                ip_dict.append(line)
            f.close()
        return ip_dict
        
        
        
        #Port Scanner bundle

from socket import *
import threading

lock = threading.Lock()
openNum = 0
threads = []

def portScanner(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        openNum+=1
        print (ip)
        print('[+] %d open' % port)
        lock.release()
        s.close()
    except:
        pass

def verify(ip):
    setdefaulttimeout(1)
    for p in range(1,30000):
        t = threading.Thread(target=portScanner, args=(ip,p))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('[*] The scan is complete!')
    print('[*] A total of %d open port' % (openNum))

if __name__ == '__main__':
    def get_pass_dict():
        pass_dict = []
        with open('./ZoneIP.txt', 'r') as f:
            for line in f.readlines():
                 line = line.strip('\n')
                 pass_dict.append(line)
            f.close()
        return pass_dict

    IP = get_pass_dict()
    for ip in IP:

        res = verify(ip)
        print(res)
