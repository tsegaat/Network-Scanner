"""
Creator is Tsega Amanuel
Be sure to have scapy installed
"""
from scapy.all import *
from time import sleep

def mac_finder(ip):
    """
    Sends an ARP packet broadcasting who has
    the given ip and returns the Mac adress of
    the given ip
    """
    packet = ARP(pdst=ip)
    broadcast = Ether(src="1c:7f:2c:15:68:27")
    broadcast_packet = broadcast / packet 
    answered = send(broadcast_packet, verbose = False, return_packets= True)[0]
    return answered.dst

def scan_everything():
    """
    Sends the whole network an ARP packet
    requesting the Mac adress of all the devices 
    in the entire subnet

    NOTE if the ip does not appear it means it is
    note being used
    """
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
