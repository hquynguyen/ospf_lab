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
        router2 = self.addHost( 'R2', cls = LinuxRouter, ip = '192.168.4.2/24' )
        router4 = self.addHost( 'R4', cls = LinuxRouter, ip = '192.168.4.4/24' )
        router5 = self.addHost( 'R5', cls = LinuxRouter, ip = '192.168.4.5/24' )
        router6 = self.addHost( 'R6', cls = LinuxRouter, ip = '192.168.4.6/24' )

        # Create a switch with name
        s1 = self.addSwitch('s1')

        # Create links between devices according to the topology with name of interface
        self.addLink( s1, router2 ,intfName2='r2-eth4')
        self.addLink( s1, router4 ,intfName2='r4-eth1')
        self.addLink( s1, router5 ,intfName2='r5-eth1')
        self.addLink( s1, router6 ,intfName2='r6-eth1')
