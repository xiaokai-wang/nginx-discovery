#!/usr/bin/python
import BaseHTTPServer
import SimpleHTTPServer
import urlparse
import threading
import random
import getopt
import SocketServer
import socket
import time
import sys

class ThreadingSimpleServer(SocketServer.ThreadingMixIn,BaseHTTPServer.HTTPServer):
        pass

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        #protocol_version = "HTTP/1.1"

        def do_HEAD(s):
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.end_headers()
        def do_POST(self):
                self.do_GET()
        def do_GET(self):
                """Respond to a GET request."""
                parsed_path = urlparse.urlparse(self.path)
                message = '{\"upstream\":[{\"host\":\"oauthweibo\",\"server\":[\"10.77.108.241:8086\",\"10.77.108.241:8087\",\"10.77.108.241:8088\",\"10.77.108.241:8089\"]},{\"host\":\"test\",\"server\":[\"10.77.108.242:8086\",\"10.77.108.242:8087\",\"10.77.108.242:8088\",\"10.77.108.242:8089\"]}],\"method\":\"add\"}'
#                message = '{"retcode":20000000,"msg":"","data":{"meta":{"etag":"4cb5a3cd5141158defe3827d7a74479e","expire":1800,"ctime":1416897731},"data":{"code":304,"msg":"304 Not Modified"}}}'
                self.send_response(200)
                self.end_headers()
                try:
                        self.wfile.write(message)
                except Exception,e:
                        print "========wfile.write excepting======", str(e)
                interval=random.choice([0.1, 0.2, 0.0])
                aa=str(interval)
                inter=float(aa)
                time.sleep(inter)
                return


if __name__=='__main__':
	ip = "10.209.75.180"
	port = 10004
	httpd = ThreadingSimpleServer((ip, port), MyHandler)
        print time.asctime(), "Server Starts - %s:%s" % (ip, port)
        try:
                httpd.serve_forever()
        except KeyboardInterrupt:
                print "Bye,bye"
        except Exception, e:
                print "=====connection exception===",str(e), "~~~~~connection exception"
        print time.asctime(), "Server Stops - %s:%s" % (ip, port)


