import scapy
from scapy.all import *
from scapy.layers.http import HTTPRequest,HTTP
import time

start = time.time() 

#pkt = rdpcap("alexa_evil_twin_http_credential.pcap")
pkt = rdpcap("check_legitimate.pcapng")
for packet in pkt:
	if(packet.haslayer("TCP")):
		try:
			info = packet["TCP"].load
			if "getDeviceDetails" in info:
				print(info)
		except:
			continue
	if(packet.haslayer("UDP")):
		try:
			info = packet["UDP"].load
			print(info)
		except:
			continue
end = time.time()
print("Execution time of the program is- ", end-start)	
