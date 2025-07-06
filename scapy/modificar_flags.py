from scapy.all import *

ip_dst = "190.45.22.104" 
puerto = 21  

pkt = IP(dst=ip_dst)/TCP(sport=RandShort(), dport=puerto, flags="P")/Raw(load="PWD\r\n")

send(pkt)

print("Paquete con flags modificadas enviado (solo PSH, sin ACK)")