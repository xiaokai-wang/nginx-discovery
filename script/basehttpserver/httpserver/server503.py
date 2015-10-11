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

        def do_GET(s):
		parsed_path = urlparse.urlparse(s.path)
                data = '{"error":"request failed for anyone reason","error_code":503, "request":"%s"}' % parsed_path.path
                s.send_response(503)
                s.send_header("Content-type", "text/html")
                s.end_headers()
		try:
                        s.wfile.write(data)
		except Exception,e:
                        print "========wfile.write excepting======", str(e)
		return

        def do_POST(self):
                self.do_GET()

        def do_HEAD(self):
                """Respond to a GET request."""
                parsed_path = urlparse.urlparse(self.path)
                message_parts = [
                        'CLIENT VALUES:',
                        'client_address=%s (%s)' % (self.client_address,
                                            self.address_string()),
                        'command=%s' % self.command,
                        'path=%s' % self.path,
                        'real path=%s' % parsed_path.path,
                        'query=%s' % parsed_path.query,
                        'request_version=%s' % self.request_version,
                        '',
                        'SERVER VALUES:',
                        'server_version=%s' % self.server_version,
                        'sys_version=%s' % self.sys_version,
                        'protocol_version=%s' % self.protocol_version,
                        '',
                        'HEADERS RECEIVED:',
                        ]
                for name, value in sorted(self.headers.items()):
                        message_parts.append('%s=%s' % (name, value.rstrip()))
                message_parts.append('')
                message = '\r\n'.join(message_parts)
                self.send_response(503)
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
	ip = socket.gethostbyname(socket.gethostname())
	port = 9999
	httpd = ThreadingSimpleServer((ip, port), MyHandler)
        print time.asctime(), "Server Starts - %s:%s" % (ip, port)
        try:
                httpd.serve_forever()
        except KeyboardInterrupt:
                print "Bye,bye"
        except Exception, e:
                print "=====connection exception===",str(e), "~~~~~connection exception"
        print time.asctime(), "Server Stops - %s:%s" % (ip, port)


