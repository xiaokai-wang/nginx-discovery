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
		etime=str(int(time.time())+50000)
		ctime=str(int(time.time()))
		message = '{"retcode":20000000,"msg":"","data":{"session":{"uid":"2458219537","rand":"wx","domain":".weibo.com","ctime":'+ctime+',"idc":"xd","status":0,"ip":null,"ua":null,"etime":'+etime+',"mid":null,"appid":null,"flag":4,"username":null,"from":null,"logintype":1,"savestate":1,"clienttype":1,"verify_flag":null,"entry":null,"ac":null,"tid":null,"appkey":null}}}'
#                message = '{"retcode":50111309,"msg":"","data":{"session":{"uid":"1000000009","rand":"w4","domain":".sina.com.cn","ctime":1399516123,"idc":"sb","status":0,"ip":"10.10.10.123","ua":"10","etime":1399602523,"mid":"01a00002000a03216012","appid":54321,"flag":4,"username":null,"from":null,"logintype":null,"savestate":null}}}'
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
	ip = "10.13.1.134"
	port = 10003
	httpd = ThreadingSimpleServer((ip, port), MyHandler)
        print time.asctime(), "Server Starts - %s:%s" % (ip, port)
        try:
                httpd.serve_forever()
        except KeyboardInterrupt:
                print "Bye,bye"
        except Exception, e:
                print "=====connection exception===",str(e), "~~~~~connection exception"
        print time.asctime(), "Server Stops - %s:%s" % (ip, port)


