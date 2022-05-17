################################################################################
#####                          readLocalization.py                         #####
#####                              Raul Tapia                              #####
#####                Redes de Sensores y Sistemas Autonomos                #####
#####                        Universidad de Sevilla                        #####
################################################################################

### Script para leer del puerto serie mensajes de tipo localizacion:
### - 8 bits para ID del emisor
### - 8 bits para posición en el eje x
### - 8 bits para posición en el eje y
### - 8 bits para posición en el eje z

import serial
import sys
from datetime import datetime

if len(sys.argv) > 2: exit()
s = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)

while True:
	while True:
		if not ord(s.read()) == 0x22: continue
		if not ord(s.read()) == 0x01: continue
		break

	r = s.read(4)
	if len(sys.argv) == 1 or int(sys.argv[1]) == ord(r[0]):
		if(ord(r[1]) < 200 and ord(r[2]) < 200 and ord(r[3]) < 200):
			print datetime.now().strftime('%H:%M:%S')
			print 'Sender: ' + str(ord(r[0]))
			print 'x = '     + str(ord(r[1]))
			print 'y = '     + str(ord(r[2]))
			print 'z = '     + str(ord(r[3]))

			print '-----'

s.close()
