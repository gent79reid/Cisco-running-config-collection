#!/usr/bin/evn 

from netmiko import ConnectHandler

username = "admin"
password = "P@ssword"

n7k_1_vdc1 = {
    'device_type':'cisco_nxos',
    'ip':'172.29.3.151',
    'username': username,
    'password': password,
}

n7k_1_vdc2 = {
    'device_type':'cisco_nxos',
    'ip':'172.29.3.152',
    'username': username,
    'password': password,
}

n7k_1_vdc3 = {
    'device_type':'cisco_nxos',
    'ip':'172.29.3.153',
    'username': username,
    'password': password,
}

n7k_1_vdc4 = {
    'device_type':'cisco_nxos',
    'ip':'172.29.3.154',
    'username': username,
    'password': password,
}

n7k_1_vdc5 = {
    'device_type':'cisco_nxos',
    'ip':'172.29.3.155',
    'username': username,
    'password': password,
}

n7k_1_vdc6 = {
    'device_type':'cisco_nxos',
    'ip':'172.29.3.156',
    'username': username,
    'password': password,
}

n7k_1_vdc7 = {
    'device_type':'cisco_nxos',
    'ip':'172.29.3.157',
    'username': username,
    'password': password,
}

n7k_2_vdc1 = {
    'device_type':'cisco_nxos',
    'ip':'172.29.3.161',
    'username': username,
    'password': password,
}

n7k_2_vdc2 = {
    'device_type':'cisco_nxos',
    'ip':'172.29.3.162',
    'username': username,
    'password': password,
}

n7k_2_vdc3 = {
    'device_type':'cisco_nxos',
    'ip':'172.29.3.163',
    'username': username,
    'password': password,
}

n7k_2_vdc4 = {
    'device_type':'cisco_nxos',
    'ip':'172.29.3.164',
    'username': username,
    'password': password,
}

n7k_2_vdc5 = {
    'device_type':'cisco_nxos',
    'ip':'172.29.3.165',
    'username': username,
    'password': password,
}

n7k_2_vdc6 = {
    'device_type':'cisco_nxos',
    'ip':'172.29.3.166',
    'username': username,
    'password': password,
}

n7k_2_vdc7 = {
    'device_type':'cisco_nxos',
    'ip':'172.29.3.167',
    'username': username,
    'password': password,
}

all_devices = [ n7k_1_vdc1, n7k_1_vdc2, n7k_1_vdc3,n7k_1_vdc4,n7k_1_vdc5,n7k_1_vdc6,n7k_1_vdc7,
                n7k_2_vdc1, n7k_2_vdc2, n7k_2_vdc3,n7k_2_vdc4,n7k_2_vdc5,n7k_2_vdc6,n7k_2_vdc7]

for device in all_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show run")
    target_file = open(device['ip']+".txt", "w")
    target_file.write(output)
    target_file.close()