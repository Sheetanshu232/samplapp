'''
Author: Sheetanshu Shekhar
Purpose: Add a new device in Cisco DNA Center
Sandbox using REST API
'''
import requests
from get_token import get_token
import json

#Generate a payload to be sent as boady
payload = '''
{
	"cliTransport": "ssh",
	"enablePassword": "Cisco123!",
	"ipAddress": ["192.168.1.1"],
	"password": "Cisco123!",
	"snmpAuthPassphrase": "Cisco123!",
	"snmpAuthProtocol": "MD5",
	"snmpMode": "v3",
	"snmpPrivPassphrase": "Cisco123!",
	"snmpPrivProtocol": "AES128",
	"snmpROCommunity": "public",
	"snmpRWCommunity": "Cisco123!",
	"snmpRetry": "3",
	"snmpTimeout": "10",
	"snmpUserName": "devnetuser",
	"username": "cisco"
}
'''
payload_json = json.loads(payload)
def add_device(token, ipaddress):
	'''
	This is the function that will add device on DNAC
	'''
	base_url = "https://sandboxdnac.cisco.com/dna/"
	headers = {
	   "Content": "application/json",
	   "X-Auth-Token": token
	}
	payload_json["ipAddress"] = ipaddress
	add_device = requests.post(f"{base_url}/intent/api/v1/network-device", headers=headers, data=None, json=payload_json)
	#Check for the error code of the 
	return add_device.status_code

def main():
	'''
	Execution is done here
	'''
	ipaddress = input(" Print the IP Address of the Device :")
	username = input(" Username of the DNA Center :")
	password = input(" Password of the DNA Center :")
	token = get_token(username,password)
	print(add_device(token, ipaddress))

if __name__ == "__main__":
	main()