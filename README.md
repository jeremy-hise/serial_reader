# serail_reader

Simple utility for reading from a serial port. 

```
usage: serial_reader.py [-h] [-V] -p PORT [-n NUMBER] [-b BAUD] [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program version
  -p PORT, --port PORT  Specify which port to read from. Example /dev/ttyUSB0
  -n NUMBER, --number NUMBER
                        Specify the number of records to read. Default is 0,
                        infinite.
  -b BAUD, --baud BAUD  Specify the baud rate. Default is 9600
  -f FILE, --file FILE  Specify a filename to output to
```

Pre-run requirements

```
$ sudo easy_install pip
$ sudo pip install pyserial
```
