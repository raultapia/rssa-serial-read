################################################################################
#####                             readTDMA.py                              #####
#####                              Raul Tapia                              #####
#####                Redes de Sensores y Sistemas Autonomos                #####
#####                        Universidad de Sevilla                        #####
################################################################################

### Script para leer del puerto serie mensajes de tipo TDMA:
### - 8 bits para ID del emisor
### - 16 bits para duracion del slot
### - 8 bits para ID del receptor 1
### - 8 bits para ID del receptor 2
### - [...]
### - 8 bits para ID del receptor N

import serial
import sys
from datetime import datetime
NUM_SLOTS = 3

if len(sys.argv) > 2: exit()
s = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)

while True:
	while True:
		if not ord(s.read()) == 0x22: continue
		if not ord(s.read()) == 0x01: continue
		break

	r = s.read(3+NUM_SLOTS)
	if len(sys.argv) == 1 or int(sys.argv[1]) == ord(r[0]):
		print datetime.now().strftime('%H:%M:%S')
		print 'Sender:      ' + str(ord(r[0]))

		slot_time = ord(r[1])<<8 | ord(r[2])
		print 'Slot time:   ' + str(slot_time)

		for i in range(NUM_SLOTS):
			id = ord(r[i+3])
			print "Slave " + str(i) + ": " + str(id)

		print '-----'

s.close()
