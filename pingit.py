#!/usr/bin/python

from signal import signal, SIGINT
import sys, getopt
from pythonping import ping

def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    sys.exit(0)

def main(argv):
    host = ''
    output = ''
    count = 4
    size = 32
    timeout = 2

    try:
        opts, args = getopt.getopt(argv,"h:c:s:", ["help"])
    except getopt.GetoptError:
        print('pingit.py -h <host/FQDN or IP>')
        sys.exit(2)
    if len(argv) == 0:
        print('pingit.py -h <host/FQDN or IP>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            host = arg
        elif opt == '-c':
            count = int(arg)
        elif opt == '-s':
            size = int(arg)

        elif opt == '--help':
            print('pingit.py -h <host/FQDN or IP>')
            sys.exit()
        else:
            print('pingit.py -h <host/FQDN or IP>')
            sys.exit(2)

    # Do the actual ping
    response_list = ping(host, timeout, count, size)

    for item in response_list:
        if item.error_message:
            print(item.error_message)
        else:
            print(item.time_elapsed_ms)
    print("Avg time:" + str(response_list.rtt_avg_ms))




if __name__ == "__main__":
    signal(SIGINT, handler)

    main(sys.argv[1:])

