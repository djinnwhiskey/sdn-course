
import os
from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import AuthenticationException, SSHException, NetMikoTimeoutException

admin_username = input("Enter admin username: ")
admin_pass = getpass("Enter admin password: ")

cisco_rtr = {
        'ip': '192.168.72.100',
        'username': admin_username,
        'password': admin_pass,
        'device_type': 'cisco_ios'
 }



try:
    connect = ConnectHandler(**cisco_rtr)
    connect_output = connect.send_command('show run')
    b = open('Router1.conf', 'x')
    b.write(connect_output)
    b.close()
except(AuthenticationException):
    print("Invalid login for " + cisco_rtr['ip'])
except(SSHException):
    print("A secure connection to " + cisco_rtr['ip'] + " can not be established")
except(NetMikoTimeoutException):
    print(cisco_rtr['ip'] + " has timed out. Please attempt the connection again")
