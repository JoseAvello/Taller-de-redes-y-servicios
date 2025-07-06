from scapy.all import *
import random
import string

ip = "190.45.22.104"   
port = 21              

def comando_fuzz():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)).encode() + b"\r\n"

SYN = IP(dst=ip)/TCP(dport=port, flags='S')
SYNACK = sr1(SYN, timeout=2)

if SYNACK:
    ACK = IP(dst=ip)/TCP(dport=port, sport=SYN[TCP].sport, seq=100, ack=SYNACK.seq + 1, flags='A')
    send(ACK)
    
    for _ in range(2):
        fuzz_data = comando_fuzz()
        pkt = IP(dst=ip)/TCP(dport=port, sport=SYN[TCP].sport, seq=101, ack=SYNACK.seq + 1, flags='PA')/Raw(load=fuzz_data)
        send(pkt)
        print(f"Inyectado: {fuzz_data}")
else:
    print("No hubo respuesta al SYN")