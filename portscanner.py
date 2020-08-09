import socket
import threading
from queue import Queue


# Defines the target to be scanned
## target = input("Provide the IP of the Host you wish to scan: ")
target = 'localhost'

#function that scans the port
def portscan(port):
    try:
        plug = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        plug.connect((target, port))
        return True
    except:
        return False


# for p in range(65536):
#     result = portscan(p)
#     if result:
#         print('Port {} is open'.format(p))
#     else:
#         print('Port {} is closed'.format(p))

#creates a queue of ports to be scanned
queue = Queue()
open_ports = []


#function to fill the queue with the ports
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

# Worker is the function each thread will call to execute the scan
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print('Port {} is open'.format(port))
            open_ports.append(port)

# defines the range to be scanned
port_list = range(0, 65536)

# Calls the fucntion to fill the ports in  the queue
fill_queue(port_list)

thread_list = []

# defines how many threads to be executed
for t in range(50):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

# initiate the thread
for thread in thread_list:
    thread.start()
# wait for the thread to finnish
for thread in thread_list:
    thread.join()

#prints the final result
print("Open ports are: ", open_ports)