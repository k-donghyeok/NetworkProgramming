import sys
from scapy.all import *

while True:
    sniff(prn = lambda X:X.show())