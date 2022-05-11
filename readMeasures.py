################################################################################
#####                           readMeasures.py                            #####
#####                              Raul Tapia                              #####
#####                Redes de Sensores y Sistemas Autonomos                #####
#####                        Universidad de Sevilla                        #####
################################################################################

### Script para leer del puerto serie mensajes de tipo medida:
### - 8 bits para ID del emisor
### - 8 bits para ID del receptor
### - 16 bits para medida de RSSI
### - 8 bits para tipo de medida (temperatura, humedad o iluminancia)
### - 16 bits para medida de temperatura, humedad o iluminancia

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

	r = s.read(7)
	if len(sys.argv) == 1 or int(sys.argv[1]) == ord(r[0]):
		print datetime.now().strftime('%H:%M:%S')
		print 'Sender:      ' + str(ord(r[0]))
		print 'Receiver:    ' + str(ord(r[1]))

		rssi = ord(r[2])<<8 | ord(r[3])
		if rssi > 127: rssi = rssi - 65536
		print 'RSSI:        ' + str(rssi)

		measure_type = ord(r[4])
		measure_value = ord(r[5])<<8 | ord(r[6])
		if measure_type in [ord('t'), ord('T'), 1, 2**0]:
			print 'Temperatura: ' + str(measure_value)
		if measure_type in [ord('h'), ord('H'), 2, 2**1]:
			print 'Humedad:     ' + str(measure_value)
		if measure_type in [ord('l'), ord('L'), 3, 2**2]:
			print 'Iluminancia: ' + str(measure_value)

		print '-----'

s.close()
