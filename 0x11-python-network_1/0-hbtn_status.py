#!/usr/bin/python3
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read().decode('utf-8')

print("\t- Body response:")
print("\t\t- type:", type(body))
print("\t\t- content:", body)

