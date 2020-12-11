import sys
from Publisher import Publisher
from Subscriber import Subscriber
from Server import Server

def main():
    args = sys.argv[1:]

    # if len(args) != 3:
    #     print('python init.py [publisher|subscriber|server] <host> <port>')

    #     return

    host = 'localhost'
    port = 8000

    if args[0] == 'publisher':
        client = Publisher(host, port)

        try:
            client.menu_loop()
        except KeyboardInterrupt:
            print('\nBye')

        return

    if args[0] == 'subscriber':
        client = Subscriber(host, port)

        try:
            client.menu_loop()
        except KeyboardInterrupt:
            print('\nBye')

        return

    if args[0] == 'server':
        server = Server('server/newsletter.db')

        print('Serving...')

        try:
            server.serve(host, port)
        except KeyboardInterrupt:
            print('\nBye')

        return

    print('Bad argument')

if __name__ == '__main__':
    main()
