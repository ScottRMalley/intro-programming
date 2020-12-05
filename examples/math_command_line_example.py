
import sys

arguments = sys.argv

if len(arguments) > 3:
	if arguments[1] == 'add':
		print(int(arguments[2]) + int(arguments[3]))
	if arguments[1] == 'multiply':
		print(int(arguments[2]) * int(arguments[3]))
else:
	print("List not long enough")

