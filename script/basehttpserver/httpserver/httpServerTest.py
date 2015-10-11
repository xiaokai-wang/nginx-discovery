#!/usr/bin/python
from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
from BaseHTTPServerTest import myRequestHandler
import getopt
import SocketServer
import socket
import time
import sys

starttime = time.time()

def helpinfo():
	print " usage: python <script>.py [options]"
	print " options:"
	print " -h --help        show the help message and exit"
	print " -i --ip   use the host you specified and localhost is default"
	print " -p --port        use the port you specified and 8888 is default"

def argsparse():
	try:
		argsdict = {}
		options,args = getopt.getopt(sys.argv[1:],"hi:p:",["help","ip=","port="])
		if not options:
			print "localhost is default ip and 8888 is default port"
			sys.exit()
		for name,value in options:
			if name in ("-h", "--help"):
				helpinfo()
				sys.exit()
			if name in ("-i", "--ip"):
				argsdict["ip"] = value
			if name in ("-p", "--port"):
				argsdict["port"] = value
		return argsdict
	except getopt.GetoptError:
		sys.exit()

def network(ip, port):
	try:
		server = HTTPServer((ip, port),myRequestHandler)
		print "server start at {STARTTIME}".format(STARTTIME=starttime)	
		server.serve_forever()
	except KeyboardInterrupt:
        	print "Bye,bye"
if __name__=='__main__':
#	argdict = argsparse()	
#	print argdict
	ip = socket.gethostbyname(socket.gethostname())
	network(ip, 9999)



