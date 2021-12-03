import requests
import json
import argparse


parser = argparse.ArgumentParser(description="""
   This script is going to scan all subdomain from SecurityTrails. 
   """)
	
parser.add_argument("domain", help="Please enter your domain for scan")

args = parser.parse_args()

domain = args.domain

url = "https://api.securitytrails.com/v1/domain/{0}/subdomains?children_only=false&include_inactive=true".format(domain)

headers = {

   "Accept": "application/json",

   "APIKEY": "<Enter Your SecurityTrails API Key>"
}


response = requests.get(url,headers=headers)

sub = response.json()

for subdomain in sub['subdomains']:
	print(subdomain+"."+domain)