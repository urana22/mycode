import ipaddress

#ipchk='192.168.0.1'
ipchk = input('Apply an IP address: ')

try:

    ipaddress.ip_address(ipchk)


    if ipchk == '192.168.70.1':
        print('Looks like the gateway IP address was set: ' + ipchk + ' This is not recommended.')

    elif ipchk:
        print("looks like the IP addess was set: " + ipchk)

    else:
        print("Not correct")

except:
    print('Enter a valid IP address ')
