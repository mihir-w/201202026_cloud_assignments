#!/usr/bin/python

import sys
from mininet.net import Mininet
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def runTopology():
    args = (sys.argv)
    numSwitch = int(args[1])
    hostSwitch = int(args[2])
    totalHost = numSwitch * hostSwitch
    oddIP = '10.0.0.'
    evenIP = '10.0.1.'
    enum = 1
    onum = 1

    net = Mininet(controller=OVSController,link=TCLink)
    info( 'Adding controller\n' )
    net.addController('c0')

    hosts=[]
    for i in range(1,totalHost+1):
        if i%2 == 1:
            hosts.append(net.addHost('h'+str(i), ip=oddIP+str(onum)+'/24'))
            onum+=1
        else:
            hosts.append(net.addHost('h'+str(i), ip=evenIP+str(enum)+'/24'))
            enum+=1
    info( 'Hosts Added\n' )

    switches=[]
    for i in range(1,numSwitch+1):
        switches.append(net.addSwitch('s'+str(i)))
    info( 'Switches Added\n' )

    info( 'Creating Links\n' )
    # Linking Hosts and Switches
    host_no=0
    for i in range(numSwitch):
        for j in range(hostSwitch):
            bandwidth=(host_no%2)+1
            net.addLink(switches[i], hosts[i*hostSwitch + j], bw=bandwidth) # Odd Host = 1 mbps, Even Host = 2 mbps
            print "h" + str(i*hostSwitch + j + 1) + "--- s" + str(i+1)
            host_no+=1

    # Linking between switches
    for i in range(numSwitch-1):
        net.addLink(switches[i], switches[i+1], bw=2)
        print "s" + str(i+1) + "--- s" + str(i+2)
    #net.addLink(switches[numSwitch-1], switches[0], bw=2)

    info( 'Starting tNetwork and CLI\n' )
    net.start()
    CLI(net)

    info( 'Adding controller\n' )
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    runTopology()
