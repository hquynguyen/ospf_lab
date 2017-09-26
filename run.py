import sys
import os
from time import sleep
from multiprocessing import Process
import termcolor as T

def log(s, col="green"):
    print T.colored(s, col)

tp = __import__(sys.argv[1])
conf = str(sys.argv[1]).strip()[-1]

def run():

    os.system("sudo rm -f /tmp/R*.log /tmp/R*.pid logs/* /tmp/zebra*.pid /tmp/ospf*.pid ")
    os.system("sudo mn -c >/dev/null 2>&1")
    os.system("sudo killall -9 zebra ospfd > /dev/null 2>&1")

    topo = tp.NetworkTopo()
    net = tp.Mininet( topo=topo, autoSetMacs=True )
    net.start()

    # The code below is for openning all host terminals, pause applying routing protocol to routers,
    # so that we can open wireshark to track all packets in the beginning
    #net.startTerms()
    user_input = raw_input("click enter to start network")

    #Installing zebra and ospf daemon in routers
    #for router in net.hosts:
    #    if router.name.startswith('R'):
    #        router.cmd("/usr/lib/quagga/zebra -f conf%s/zebra-%s.conf -d -i /tmp/zebra-%s.pid > logs/%s-zebra-stdout 2>&1" % (conf, router.name, router.name, router.name))
    #        router.waitOutput()
    #        router.cmd("/usr/lib/quagga/ospfd -f conf%s/ospfd-%s.conf -d -i /tmp/ospf-%s.pid > logs/%s-ospfd-stdout 2>&1" % (conf, router.name, router.name, router.name))
    #        router.waitOutput()
    #        log ("Starting zebra and ospf on %s" % router.name)
    #        sleep(3)

    tp.CLI( net )
    net.stop()
    os.system("sudo killall -9 zebra ospfd")
    os.system("sudo rm -f /tmp/bgp*.pid /tmp/zebra*.pid /tmp/ospf*.pid ")

if __name__ == '__main__':
    tp.setLogLevel( 'info' )
    run()
