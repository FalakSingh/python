#!/usr/bin/env python

import re
import subprocess
import optparse


#function to change mac address
def change_mac(interface, new_mac):
    print("[+]Changing MAC Address of " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac ])
    subprocess.call(["ifconfig", interface, "up"])

#function to get arguments by the user
def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Name of Interface to change its MAC")
    parser.add_option("-m", "--new_mac", dest="new_mac", help="New Mac Address")
    (options, arguments) =  parser.parse_args()
    if not options.interface:
        parser.error("[-] Please Specify an Interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please provide a New MAC, use --help for more info.")
    return options


#function to search MAC address
def search_mac_add(interface):
    ifconfig_output = subprocess.check_output(["ifconfig", interface])
    mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_output)
    if mac_search_result:
        return mac_search_result.group(0)
    else:
        print("[-] Could not find MAC Address")

#function to check the completion if MAC is changed or not
def check_completion():
    if options.new_mac == changed_mac:
        print("[+]New MAC: " + changed_mac)
    else:
        print("[-]Could not change MAC")

#getting input from user
options = get_args()

#searching the current MAC Address
current_mac = search_mac_add(options.interface)
print("[+]Current MAC is: " + str(current_mac))

#changing MAC
change_mac(options.interface, options.new_mac)
changed_mac = search_mac_add(options.interface)

#to check completion of script/program
check_completion()

