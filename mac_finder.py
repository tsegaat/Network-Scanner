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
    broadcast = Ether()
    broadcast_packet = broadcast / packet 
    answered = send(broadcast_packet, verbose = False, return_packets= True)[0]
    return answered.dst

def scan_everything(router_ip):
    """
    Sends the whole network an ARP packet
    requesting the Mac adress of all the devices 
    in the entire subnet.



    NOTE:---    ENTER THE FIRST THREE LAYERS OF THE ROUTER'S IP ADDRESS

    """
    x = 0
    while x <= 255:
        packet = ARP(pdst = router_ip + "." + str(x))
        broadcast = Ether()
        broadcast_packet = broadcast / packet 
        answered = send(broadcast_packet, verbose = False, return_packets= True)[0]
        print("\nIP:\n" + str(answered.pdst) + "\n\nMAC:\n" + str(answered.dst) + "\n--------------------")
        sleep(1)
        x += 1

scan_everything("192.168.0")