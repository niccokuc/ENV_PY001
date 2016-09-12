
2
down vote
favorite
1
I installed the networking module Scapy. When I import scapy (import scapy) everything works fine. When I import all from scapy (from scapy.all import *), it brings up this error:

Traceback (most recent call last):
File "/Users/***/Downloads/test.py", line 5, in <module>
from scapy.all import *
File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/scapy/all.py", line 16, in <module>
from .arch import *
File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/scapy/arch/__init__.py", line 75, in <module>
from .bsd import *
File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/scapy/arch/bsd.py", line 12, in <module>
from .unix import *
File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/scapy/arch/unix.py", line 22, in <module>
from .pcapdnet import *
File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/scapy/arch/pcapdnet.py", line 22, in <module>
from .cdnet import *
File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/scapy/arch/cdnet.py", line 17, in <module>
raise OSError("Cannot find libdnet.so")
OSError: Cannot find libdnet.so
I found out on another post that we might have to download additionnal modules in order to make scapy fully work. What should be done exactly? I tried using (port ** install) which didn't work because port is not supported anymore? If you have any idea how to make it work in python3, I will be active. Here is more additionnal informations:

python 3.4.3
mac os 10.10.4
scapy-python3==0.14
EDIT: Another interesting thing is :

On all OS except Linux libpcap should be installed for sending and receiving packets (not python modules - just C libraries). libdnet is recommended for sending packets, without libdnet packets will be sent by libpcap, which is limited. Also, netifaces module can be used for alternative and possibly cleaner way to determine local addresses. Source: https://pypi.python.org/pypi/scapy-python3/0.11

Dnet seems to only work with version 2.7 : https://pypi.python.org/pypi/dnet/1.12

python-3.x importerror scapy
shareimprove this question
edited Aug 10 '15 at 2:29
asked Aug 10 '15 at 2:01

Bob Ebert
348315
add a comment
1 Answer
active oldest votes
up vote
1
down vote
accepted
You have to install libdnet. Not the python library (which does not work on python3 as you mentioned), but the library itself. There has to be library file libdnet.so somewhere in your system where python searches for libraries. Downloading the libdnet source and compiling should make it work:

wget http://libdnet.googlecode.com/files/libdnet-1.12.tgz
tar xfz libdnet-1.12.tgz
cd libdnet-1.12
./configure
make
Also, there is a possibility to use libpcap for sending packets and not to use libdnet, but I recommend trying to make libdnet work first.