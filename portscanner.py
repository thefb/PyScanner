import socket

## target = input("Provide the IP of the Host you wish to scan: ")
target = 'localhost'

def portscan(port):
    try:
        plug = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        plug.connect((target, port))
        return True
    except:
        return False


for p in range(65536):
    result = portscan(p)
    if result:
        print('Port {} is open'.format(p))
    else:
        print('Port {} is closed'.format(p))