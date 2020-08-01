"""
Creator is Tsega Amanuel
"""
from scapy.all import *
from time import sleep

def mac_finder(ip):
    packet = ARP(pdst=ip)
    broadcast = Ether(src="1c:7f:2c:15:68:27")
    broadcast_packet = broadcast / packet 
    answered = send(broadcast_packet, verbose = False, return_packets= True)[0]
    return answered.dst

def scan_everything():
    x = 0
    while x <= 255:
        packet = ARP(pdst="192.168.1." + str(x))
        broadcast = Ether(src="1c:7f:2c:15:68:27")
        broadcast_packet = broadcast / packet 
        answered = send(broadcast_packet, verbose = False, return_packets= True)[0]
        if answered.dst != "ff:ff:ff:ff:ff:ff":
            print("\nIP:\n" + str(answered.pdst) + "\n\nMAC:\n" + str(answered.dst) + "\n--------------------")
            sleep(1)
        x += 1

scan_everything()
