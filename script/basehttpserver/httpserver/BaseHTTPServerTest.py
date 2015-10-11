from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
import getopt
import SocketServer
import socket
import time
import sys

class myRequestHandler(BaseHTTPRequestHandler):
	
	def do_GET(self):
		print self.headers
#		self.process("get")
#		self.do_POST()

	def do_POST(self):
		print self.headers
		len = int(self.headers.getheader('content-length'))
		if len:
			len = int(len)
		else:
			self.send_response(404)
			self.send_error(404,"check your arguments for post")
            		return
		input_body = self.rfile.read(len)
		print input_body		
		self.send_response(200)
#		self.process("post")

	def process(self, type):
		
		if type == "get":
			#print self.client_address
			#print self.command
			#print self.path
			#print self.request_version
			print self.headers
'''		if type == "post":
			print self.headers
			len = int(self.headers.getheader('content-length'))
			input_body = self.rfile.read
'''
