#tesr.py 局域网发包

from scapy.all import *
data = 'Packet content'
pkt = IP(src='127.0.0.1', dst='10.xx.xx.xx')/TCP(sport=xx,dport=xx)/data
#每间隔1s发送5次
send(pkt,inter=1,count=5)
