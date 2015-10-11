#!/bin/env python
import socket
import sys
import utils
import time

HOST = None
PORT = 8080
BACKLOG = 128
MAX_REQUEST_SIZE = 4096

def main():
    port = PORT
    backlog = BACKLOG
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    if len(sys.argv) > 2:
        backlog = int(sys.argv[2])
    s = utils.bind_listen(HOST,port,backlog)
    print 'Listen on %s %d, than go sleep' % (socket.gethostbyname(socket.gethostname()), port)
    try:
        time.sleep(3600*24*300)
    except KeyboardInterrupt:
        s.close()
        print "Bye,bye"

if __name__ == '__main__':
    main()
