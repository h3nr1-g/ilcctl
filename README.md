ilcctl
======

Python package for iLC Bluetooth light bulbs

This project provides a Python3 package for controlling iLC Bluetooth light bulbs such as https://ilctech.myshopify.com/collections/lighting-1/products/ilc-bluetooth-bulbs-9w-e27 .

The code is tested on Python 3.5.


Installation
------------

To install the current released version, on most Debian-based systems:

    $ sudo apt-get install python3-pip libglib2.0-dev
    $ sudo pip3 install ilcctl

On Fedora do:

    $ sudo dnf install python3-pip glib2-devel

*If this fails* you should install from source.

    $ sudo apt-get install git build-essential libglib2.0-dev
    $ git clone https://github.com/h3nr1-g/ilcctl
    $ cd ilcctl
    $ python3 setup.py build
    $ sudo python3 setup.py install
 
    
Commandline Interface
---------------------

This package provides also a small commandline interface for shell based interactions with the light bulbs

    $ ilcctl --help                                                                                                                                                                                                                             ⏎
    Usage: ilcctl [OPTIONS] COMMAND [ARGS]...
    
    Options:
      --help  Show this message and exit.
    
    Commands:
      powerstate  Command for turning light bulb on and off
      sendcmd     Command for sending a raw byte sequence to the light bulb
      setcolor    Command for changing the color
      whitelight  Command for turn on warm white led with certain intensity

    $ ilcctl powerstate <MAC_ADDR> <0|1>
    $ ilcctl setcolor <MAC_ADDR> <HEX_COLOR>
    $ ilcctl sendcmd <MAC_ADDR> <CMD>
    $ ilcctl whitelight [--brightness <LEVEL>] <MAC_ADDR> 


License
-------

This project uses code from the bluez project, which is available under the Version 2
of the GNU Public License.

The Python files are released into the public domain by their author, Henry Glueck.



