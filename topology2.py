from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node, Switch, OVSKernelSwitch
from mininet.log import setLogLevel, info, lg
from mininet.cli import CLI
from mininet.util import dumpNodeConnections, quietRun, moveIntf


class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl -w net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl -w net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()


class NetworkTopo( Topo ):

    def build( self, **_opts ):
        # Create routers by using LinuxRouter class defined, with name and default IP address
        router1 = self.addHost( 'R1', cls = LinuxRouter, ip = '192.168.1.1/24' )
        router2 = self.addHost( 'R2', cls = LinuxRouter, ip = '192.168.2.1/24' )
        router3 = self.addHost( 'R3', cls = LinuxRouter, ip = '192.168.3.1/24' )
        router4 = self.addHost( 'R4', cls = LinuxRouter, ip = '192.168.4.4/24' )
        router5 = self.addHost( 'R5', cls = LinuxRouter, ip = '192.168.4.5/24' )
        router6 = self.addHost( 'R6', cls = LinuxRouter, ip = '192.168.4.6/24' )
        router7 = self.addHost( 'R7', cls = LinuxRouter, ip = '192.168.103.2/30' )
        router8 = self.addHost( 'R8', cls = LinuxRouter, ip = '192.168.104.2/30' )

        # Create hosts with name, IP address and default route or gateway IP which is IP address of router's interface
        h1 = self.addHost( 'h1', ip='192.168.1.2/24', defaultRoute='via 192.168.1.1' )
        h2 = self.addHost( 'h2', ip='192.168.2.2/24', defaultRoute='via 192.168.2.1' )
        h3 = self.addHost( 'h3', ip='192.168.3.2/24', defaultRoute='via 192.168.3.1' )

        # Create a switch with name
        s1 = self.addSwitch('s1')

        # Area 0: Create links between devices according to the topology with name of interface
        self.addLink( h1, router1, intfName2='r1-eth1' )
        self.addLink( h2, router2, intfName2='r2-eth1' )
        self.addLink( h3, router3, intfName2='r3-eth1' )
        self.addLink( router1, router2, intfName1 = 'r1-eth2', intfName2='r2-eth2')
        self.addLink( router2, router3, intfName1 = 'r2-eth3', intfName2='r3-eth2')
        self.addLink( router1, router3, intfName1 = 'r1-eth3', intfName2='r3-eth3')

        # Area 1: Create links between devices according to the topology with name of interface
        self.addLink( s1, router2 ,intfName2='r2-eth4')
        self.addLink( s1, router4 ,intfName2='r4-eth1')
        self.addLink( s1, router5 ,intfName2='r5-eth1')
        self.addLink( s1, router6 ,intfName2='r6-eth1')

        # Area 2: Create links between devices according to the topology with name of interface
        self.addLink( router3, router7, intfName1 = 'r3-eth4', intfName2='r7-eth1')
        self.addLink( router3, router8, intfName1 = 'r3-eth5', intfName2='r8-eth1')
