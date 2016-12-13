#!/usr/bin/python

from Adafruit_Thermal import *
from time import sleep, gmtime, strftime

def print_text(p, msg, chars_per_line=None):
	""" Print some text defined by msg. If chars_per_line is defined, inserts newlines after the given amount. Use normal '\n' line breaks for empty lines. """
	if not chars_per_line:
	    p.write(msg)
	    sleep(0.2)
	else:
	    l = list(msg)
	    le = len(msg)
	    for i in xrange(chars_per_line + 1, le, chars_per_line + 1):
		l.insert(i, '\n')
	    p.write("".join(l))
	    sleep(0.2)

def main(sender, message):
	print("sender %s message %s" % (sender, message))
	printer = Adafruit_Thermal("/dev/serial0", 9600, timeout=5)

	printer.wake()       # Call wake() before printing again, even if reset
	printer.setDefault() # Restore printer to defaults

	# Set justification (right, center, left) -- accepts 'L', 'C', 'R'
	# Set type size, accepts 'S', 'M', 'L'
	printer.setSize('L')	# Lagre
	printer.justify('C')	# Center
	print_text(printer, "%s\n" % sender, 15)

	printer.setSize('S')	# Small
	#print_text(printer, "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...\n", 15)
	#print_text(printer, str(message).join("\n"), 15)
	print_text(printer, "%s\n" % message, 15)


	printer.setLineHeight(50)
	#printer.println("<time>")
	print_text(printer, strftime("%Y-%m-%d\n%H:%M:%S", gmtime()))
	printer.setLineHeight() # Reset to default

	printer.feed(4)

	printer.sleep()      # Tell  printer to sleep

if __name__ == '__main__':
	import sys

	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Argument List:', str(sys.argv)
	if len(sys.argv) != 3:
		sys.exit("ERROR: Sender and message required!")

	print("sender %s message %s" % (sys.argv[1], sys.argv[2]))
	
	main(sys.argv[1], sys.argv[2])
