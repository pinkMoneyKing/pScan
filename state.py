#!/usr/bin/python3
# state.py

import netifaces
from pprint import pprint

class InputState(object):
    """
    Return Input functionality
    """

    def __init__(self):
        # self.command = ['start']
        self.command = ''

    def input(self):
        print('\n')
        user_command = input("$ ")
        print('\n')
        self.command = self.parse_command(user_command)
        return self.command

    def parse_command(self, command):
        command_array = command.split(" ")
        return command_array


class CommandState(object):

    def __init__(self):
        self.command_options = ['help', 'list', 'set', 'run', 'info', 'options', 'exit']
        self.state = InputState()
        self.command_options = {}

    def command_switch(self):
        command_array = self.state.command
        command = command_array[0]

        if command == 'help':
            self.help()
        elif command == 'list':
            self.list(command_array)
        elif command == 'set':
            self.set(command_array)
        elif command == 'exit':
            return command
        elif command == 'pink':
            print(f'{command} : {command_array}')
        else:
            print('command unknow')

    def help(self):
        # print('\thelp <command> for more information\n')
        for command in self.command_options:
            print(f'\t{command}')

    def list(self, command_array):
        if len(command_array) <= 1:
            print('Usage : list <option> ')
            print('Options : network, ip, gateways')
            return

        option = command_array[1]
        if option == 'network':
            networks = netifaces.interfaces()
            for network in networks:
                print(f'\t{network}')
        if option == 'gateways':
            gateways = netifaces.gateways()
            pprint(gateways)

    def set(self, command_array):
        if len(command_array) <= 1:
            print('Usage : set <option> <value>')
            print('Options : network, ip')
            print('Example : set network wlp4so')
            return

        key = command_array[1]
        value = command_array[2]
        self.command_options[key] = value
        print(f'set {key} {value}')
        return self.command_options


    def run(self):
        command = ['run']
        while command[0] != "exit":
            command = self.state.input()
            # self.command_switch(self.command)
            self.command_switch()


class ScanOptions(object):

    def __init__(self):
        self.target = '192.168.0.1'
        self.scan_type = 'network'

    def set_target(self, target):
        self.target = target

    def set_type(self, scan_type):
        self.scan_type = scan_type


class Scan(ScanOptions):

    def scan_network(self):
        print(f'Traget : {self.target}')
        print(f'Type : {self.scan_type}')

pink_scanner = CommandState()
pink_scanner.run()

# pink_scanner = Scan()
# pink_scanner.scan_network()
