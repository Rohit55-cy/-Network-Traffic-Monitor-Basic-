# pip install scapy
from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer('IP'):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        proto = packet['IP'].proto
        print(f"IP Packet: {src_ip} -> {dst_ip} (Protocol: {proto})")

print("Starting network traffic monitor...")
sniff(prn=packet_callback, count=20)  # Captures 20 packets
