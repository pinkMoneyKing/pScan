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


def ip_range():
    network = 'wlp4s0'
    # gateway_ip = netifaces.gateways()[network]
    print(netifaces.gateways())
    # print(f'{gateway_ip}')
    # data = netifaces.ifaddresses(network)[2]
    # for info in data:
    #     ip = info.get("addr", "Ip Not Found")



def scan_network():
    # network = network_choice()
    network = 'wlp4s0'
    ip_range()

def main():

    print('/n/tType "quit" to quit')
    scan_network()




main()
