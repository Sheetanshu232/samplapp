#! usr/bin/env python
'''
Author: Sheetanshu Shekhar
Purpose: Test Python "Requests" to get an access token from
Cisco DNA Center using the REST API
'''
import requests

def get_token(username, password):
	'''
	Gets an access token from Cisco DNA Center Sandbox.
	Returns the token string if successful. It fails otherwise
	'''

	# Declare the useful variables.
	base_url = "https://sandboxdnac.cisco.com/dna"
	auth = (username, password)
	headers = {
	   "Content-type": "application/json",
	   "Authorization": "string"
	}

	# Issue HTTP post request to get the token
	auth_resp = requests.post(f"{base_url}/system/api/v1/auth/token", auth=auth, headers=headers)

	# Return token if the event is successful. Else print the HTTP error.
	auth_resp.raise_for_status()
	token = auth_resp.json()["Token"]
	return token

def main():
	'''
	Execution Begins Here
	'''
	username = input("Print the username: ")
	password = input("Type the password: ")
	token = get_token(username, password)
	print(token)

if __name__ == "__main__":
	main()
