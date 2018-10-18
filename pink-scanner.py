#! /usr/bin/python3
"""
    Network and IP scanner.
        * netiface
        * python-nmap

    by Pink Money King
"""


import sys
import netifaces
import nmap
import re


def network_interfaces():
   interfaces = netifaces.interfaces()
   return interfaces


def print_network_options():
    interfaces = network_interfaces()

    print(f'\n\tWhich network would you like to scan?')
    for index, interface in enumerate(interfaces):
        print(f"\t {interface}")
    print('\n')

def network_choice():
    """
    TODO:
        * user input error
    """
    print_network_options()
    network = input("> ")
    return network


def network_range(network="wlp4s0"):
    data = netifaces.ifaddresses(network)[2]
    for info in data:
        ip = info.get("addr", "Ip Not Found")

    print(f"\n\tNetwork :: {network}")
    print(f"\tIp :: {ip}\n")

    input_network_range = input("Enter the Ip range you wish to scan: ")
    return input_network_range


def scan_network():
    network = network_choice()
    range_to_scan = network_range()
    print(f"\n\tScanning range {range_to_scan} in {network}\n")
    hosts_list = nmap_host_discovery(range_to_scan)
    return hosts_list
    # nmap stuff

def nmap_host_discovery(range_to_scan):
    nm = nmap.PortScanner()
    nm.scan(hosts=range_to_scan, arguments='-sP')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    for host, status in hosts_list:
        print(f'\tHost :: {host} \t Status :: {status}')

    return hosts_list

def main():

    print('/n/tType "quit" to quit')
    scan_network()




main()
