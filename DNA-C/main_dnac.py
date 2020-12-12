'''
Author: Sheetanshu Shekhar
Purpose: Main Python program to import modules and interact with
Cisco DevNet Sandbox
'''
from get_token import get_token
from get_devices_list import get_devices_list, get_devices_mgmt_ip
import json

username = input(" Username : ")
password = input(" Password : ")
#Use the Password and Username to get token
token = get_token(username,password)
#Use the generated token to print the devices_list
get_devices_mgmt_ip(get_devices_list(token))