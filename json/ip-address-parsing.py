### IP Addresses: dict and list
single_address = {'ip': '192.168.56.101', 'netmask': '255.255.255.0'}
multiple_addresses = [{'ip': '192.168.56.101', 'netmask': '255.255.255.0'},
                      {'ip': '192.0.2.1', 'netmask': '255.255.255.252'} ]
ietf_ipv4 = {'address': [{'ip': '192.168.56.101', 'netmask': '255.255.255.0'}]}

print(type(single_address))
print(type(multiple_addresses))
print(type(ietf_ipv4))
print(ietf_ipv4['address'][0]['ip'])