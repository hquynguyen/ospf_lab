py import time
py "Start zebra and ospf in router 1"
R1 /usr/lib/quagga/zebra -f conf1/zebra-R1.conf -d -i /tmp/zebra-R1.pid > logs/R1-zebra-stdout 2>&1
R1 /usr/lib/quagga/ospfd -f conf1/ospfd-R1.conf -d -i /tmp/ospf-R1.pid > logs/R1-ospfd-stdout 2>&1
py time.sleep(3)
py "Start zebra and ospf in router 2"
R2 /usr/lib/quagga/zebra -f conf1/zebra-R2.conf -d -i /tmp/zebra-R2.pid > logs/R2-zebra-stdout 2>&1
R2 /usr/lib/quagga/ospfd -f conf1/ospfd-R2.conf -d -i /tmp/ospf-R2.pid > logs/R2-ospfd-stdout 2>&1
py time.sleep(3)
py "Start zebra and ospf in router 3"
R3 /usr/lib/quagga/zebra -f conf1/zebra-R3.conf -d -i /tmp/zebra-R3.pid > logs/R3-zebra-stdout 2>&1
R3 /usr/lib/quagga/ospfd -f conf1/ospfd-R3.conf -d -i /tmp/ospf-R3.pid > logs/R3-ospfd-stdout 2>&1
py time.sleep(3)
py "Finish"
