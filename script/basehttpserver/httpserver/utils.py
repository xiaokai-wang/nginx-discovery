#!/bin/env python
import inspect
import time
from time import localtime, strftime
import socket
import struct
import sys
import traceback

def currtime(sec = 0):
	if sec > 0: 
		return strftime("%Y%m%d %H:%M:%S", localtime(sec))
	return  strftime("%Y%m%d %H:%M:%S", localtime())

def timestamp():
	return int(time.time())

def settimeout(sock, timeout):
    tv = struct.pack('ii', int(timeout), int((timeout-int(timeout))*1e6))
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDTIMEO, tv)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, tv)

def setlinger(sock, l_onoff, l_linger):
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,
                      struct.pack('ii', l_onoff, l_linger))

def getlinger(sock):
    """Returns SO_LINGER value for a socket as (l_onoff, l_linger)."""
    return struct.unpack('ii',
        sock.getsockopt(socket.SOL_SOCKET, socket.SO_LINGER,
                        struct.calcsize('ii')))

def bind_listen(host, port, backlog):
    s = None
    for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            print "socket error:",msg
            s = None
            continue
        except Exception as e:
            traceback.print_exc()

        try:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(sa)
            s.listen(backlog)
        except socket.error as msg:
            print "socket error:",msg
            s.close()
            s = None
            continue
        except Exception as e:
            traceback.print_exc()
        
        break

    if s is None:
        print 'could not open socket'
        sys.exit(1)
    return s

def connecthost(host, port, timeout):
    s = None
    for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            print "Exception: socket ", msg, inspect.currentframe().f_code.co_filename, inspect.currentframe().f_lineno
            s = None
            continue
        try:
            s.settimeout(timeout)
            s.connect(sa)
        except socket.error as msg:
            print "Exception: connecthost ", msg, inspect.currentframe().f_code.co_filename, inspect.currentframe().f_lineno
            s.close()
            s = None
            continue
        break
    if s is None:
        print 'Exception: could not open socket'
    return s

if __name__ == '__main__':
	print currtime()
	print timestamp()
	print currtime(timestamp()+1)
