import socket
import termcolor

def scan(target, ports):
	print(termcolor.colored(f'[+] {target}\'s ports are: ', 'green'))
	for port in range(1,ports):
		port_scan(target, port)

def port_scan(ipaddress,port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress,port))
		print(termcolor.colored(f'[+] Port Opened: {port}', 'green'))
		sock.close()
	except:
		pass

targets = input(termcolor.colored('[*] Enter targets ip addresses (split them by ,): ', 'green'))
ports = int(input(termcolor.colored('[*] How many ports you wanna scan: ', 'blue')))
if ',' in targets:
	print("[+] Scanning Multiple targets...")
	for target in targets.split(','):
		scan(target.strip(' '),ports)
else:
	print(termcolor.colored("[+] Scanning...",'green'))
	scan(targets,ports)
