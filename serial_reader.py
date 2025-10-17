# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# Y ou should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import serial

parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", help="show program version", action="store_true")
parser.add_argument("-p", "--port", required=True, help="Specify which port to read from. Example /dev/ttyUSB0")
parser.add_argument("-n", "--number",  default=0, type=int, help="Specify the number of records to read. Default is 0, infinite.")
parser.add_argument("-b", "--baud", default="9600", help="Specify the baud rate. Default is 9600")
parser.add_argument("-f", "--file", help="Specify a filename to output to")

args = parser.parse_args()

running = True
current_it = 0

if args.version:
    print("Serial Reader v 0.1")


while running == True:
	with serial.Serial(args.port, args.baud, timeout=10) as ser:
		line=ser.readline()
		print (line.rstrip())
		if args.file != None:
			fh = open(args.file, "a")
			fh.write(str(line.rstrip())+"\n")
			fh.close()

		current_it = current_it + 1
		if (current_it >= args.number) and (args.number > 0):
			running=False

	
