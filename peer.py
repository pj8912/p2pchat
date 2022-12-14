import sys
from p2p.client import *
from p2p.server import *
import time
import sqlite3

class p2p:
    peers = ['127.0.0.1']


def main():
    
    msg = "test message".encode('utf-8')
    while True:
        try:
            print("-" * 21 + "Trying to connect" + "-" * 21)
            time.sleep(2)
            for peer in p2p.peers:
                try:
                    client = ClientConnection(peer)
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass


                # become the server
                try:
                    server = ServerConnection(msg)
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    pass

        except KeyboardInterrupt as e:
            sys.exit(0)

