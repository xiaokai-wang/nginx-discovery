#!/bin/env python
import socket
import sys
import utils
import time

HOST = None
PORT = 8080
BACKLOG = 128
MAX_REQUEST_SIZE = 4096

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

def main():
    port = PORT
    backlog = BACKLOG
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    if len(sys.argv) > 2:
        backlog = int(sys.argv[2])
    s = bind_listen(HOST,port,backlog)
    print 'Listen on %s %d, than go sleep' % (socket.gethostbyname(socket.gethostname()), port)
    try:
        time.sleep(3600*24*300)
    except KeyboardInterrupt:
        s.close()
        print "Bye,bye"

if __name__ == '__main__':
    main()
