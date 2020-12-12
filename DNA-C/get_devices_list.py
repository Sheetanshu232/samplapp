'''
Author: Sheetanshu Shekhar
Purpose: Get device list from DNA Center using
REST API
'''
import requests
from get_token import get_token
import pprint

def get_devices_list(token):
	'''
	Get a list of devices from
	Cisco DNA Center
	'''
	# Declare Useful Variables
	base_url = "https://sandboxdnac.cisco.com/dna"
	headers = {
	  "Content-type": "application/json",
	  "Accept": "application/json",
	  "X-Auth-Token": token
	}

	#Get devices list
	devices_list = requests.get(f"{base_url}/intent/api/v1/network-device", headers = headers)

	# Return Devices list if there are no errors
	devices_list.raise_for_status()
	return devices_list.json()

def get_devices_mgmt_ip (devices_list):
	#Extract Device ID
	for device in devices_list["response"]:
		print (f"Hostname: {device['hostname']}   ID: {device['id']}   IP: {device['managementIpAddress']}" )


def main():
	'''
	Main Execution begins here
	'''
	# Get user inputs for username and password
	username = input("Username: ")
	password = input("Password: ")
	token = get_token(username,password)
	devices_list = get_devices_list(token)
	pprint.pprint(devices_list)
	print("The management IP of all the Devices are ")
	get_devices_mgmt_ip(devices_list)

if __name__ == "__main__":
	main()

