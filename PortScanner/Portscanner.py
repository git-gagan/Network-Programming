#Use Sockets
import socket
import threading
from queue import Queue

target = "x.x.x.x"    #Your personal network as port scanning is illegal too!
queue = Queue()
open = []

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        return True
    except:
        return False
    
def fill(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open".format(port))
            open.append(port)

if __name__ == "__main__":
    name = input("Plz enter your name : ")
    print(f"Welcome to the port scanner {name}")

    thread_list = []
    port_list = range(1,1024)
    fill(port_list)
    #Creating threads
    for t in range(100): 
        thread = threading.Thread(target = worker)
        thread_list.append(thread)
    #Starting Threads
    for t in thread_list:
        t.start()
    #After starting all threads, we are gonna wait for them all to finish before we proceed to the end!
    for t in thread_list:
        t.join()
        
    #After every thread finishes
    print("Open ports are : ",open)