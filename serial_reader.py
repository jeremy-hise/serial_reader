import argparse
import serial


# initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", help="show program version", action="store_true")
parser.add_argument("-p", "--port", required=True, help="Specify which port to read from. Example /dev/ttyUSB0")
parser.add_argument("-n", "--number",  default=0, type=int, help="Specify the number of records to read. Default is 0, infinite.")
parser.add_argument("-b", "--baud", default="9600", help="Specify the baud rate. Default is 9600")
parser.add_argument("-f", "--file", help="Specify a filename to output to")

# read arguments from the command line
args = parser.parse_args()

running = True
current_it = 0

# check for --version or -V
if args.version:
    print("Serial Reader v 0.1")


while running == True:
	with serial.Serial(args.port, args.baud, timeout=10) as ser:
		line=ser.readline()
		print (line.rstrip())
		if args.file != None:
			fh = open(args.file, "a")
			fh.write(line.rstrip()+"\n")
			fh.close()

		current_it = current_it + 1
		if (current_it >= args.number) and (args.number > 0):
			running=False

	
