//python3 IPsort.py ip.txt

#!/usr/bin/python3
import sys
import os
import socket

iplist = []
def ipsort(iplist):
    with open('ip.txt', 'w') as file:
        for i in sorted(iplist, key=socket.inet_aton):
            print(i)
            file.writelines(i + "\n")
        # print(file)

def read_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            iplist.append(line.rstrip('\n').rstrip('\n'))  
    return iplist


def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: %s %s" % (sys.argv[0], sys.argv[1]))
        else:
           
            if os.path.exists(sys.argv[1]):
                filename = sys.argv[1]
            else:
                print("%s is not exists!" % (sys.argv[1]))
                sys.exit(1)
        iplist = read_file(filename)  
        # print(iplist)
        ipsort(iplist)  

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
