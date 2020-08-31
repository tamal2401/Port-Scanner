import socket
import threading
from queue import Queue

open_ports = []
ipAddr = '127.0.0.1'
queue = Queue()

def populateQueue(portLists):
    for p in portLists:
        queue.put(p)

def scan(port):
    try:
        sock = socket.socket(socket.AF_TNET, socket.SOCK_STREAM)
        sock.connect((ipAddr, port))
        print("true")
        return True
    except:
        print("false")
        return False

list_of_ports = range(1,1024)
populateQueue(list_of_ports)

def worker():
    while not queue.empty():
        current_port = queue.get()
        status = scan(current_port)
        if status:
            open_ports.append(current_port)

list_of_threads = []

for i in range(8):
    thread = threading.Thread(target=worker)
    list_of_threads.append(thread)

for thread in list_of_threads:
    thread.start()

for thread in list_of_threads:
    thread.join()

print('Open ports are : {}'.format(open_ports))