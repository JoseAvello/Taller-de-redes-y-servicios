from scapy.all import *

ip_server = "190.45.22.104"

pkt = IP(dst=ip_server)/TCP(dport=21, sport=RandShort(), flags="S")

syn_ack = sr1(pkt, timeout=2)

if syn_ack is None:
    print("Servidor no respondiÃ³ al SYN")
    exit()

ack = IP(dst=ip_server)/TCP(dport=21, sport=pkt[TCP].sport,
                            seq=syn_ack.ack, ack=syn_ack.seq + 1, flags="A")
send(ack)


payload = b"USEA ftpuser\r\n"
psh = IP(dst=ip_server)/TCP(dport=21, sport=pkt[TCP].sport,
                            seq=syn_ack.ack, ack=syn_ack.seq + 1, flags="PA")/Raw(load=payload)
send(psh)

print("Comando 'USEA ftpuser' enviado")