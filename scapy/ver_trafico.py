from scapy.all import *

def ver_trafico(pkt):
    if pkt.haslayer(TCP) and pkt[TCP].dport == 21:
        print(">>> Paquete al puerto 21 (FTP control)")
        if Raw in pkt:
            print(pkt[Raw].load)

sniff(filter="tcp port 21", prn=ver_trafico, store=0)