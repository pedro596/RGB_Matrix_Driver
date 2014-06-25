import serial
import time
import  timeit
from threading import Thread
import Queue
import signal
import sys


def SIGINT_handler(signal, frame):
	matrix.matriz[3]=0
	sys.exit(0)

class Serial_Matrix():
	"""docstring for Serial_Matrix"""


		
	def __init__(self):


		

		self.r = {0:1,1:1,2:1,3:1,4:1,5:1,6:1,7:1}
		self.g = {0:1,1:1,2:1,3:1,4:1,5:1,6:1,7:1}
		self.b = {0:1,1:1,2:1,3:1,4:1,5:1,6:1,7:1}

		self.matriz = {0:self.r, 1:self.g, 2:self.b,3:1}
		
		#letters definition


		self.letter = {
		' ':{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0},
		'A':{0:0x7F,1:0x88,2:0x88,3:0x88,4:0x7F,5:0,6:0,7:0},
		'B':{0:0xFF,1:0x91,2:0x91,3:0x91,4:0x6E,5:0,6:0,7:0},
		'C':{0:0x7E,1:0x81,2:0x81,3:0x81,4:0x42,5:0,6:0,7:0},
		'D':{0:0xFF,1:0x81,2:0x81,3:0x42,4:0x3C,5:0,6:0,7:0},
		'E':{0:0xFF,1:0x91,2:0x91,3:0x91,4:0x81,5:0,6:0,7:0},
		'F':{0:0xFF,1:0x90,2:0x90,3:0x90,4:0x80,5:0,6:0,7:0},
		'G':{0:0x7E,1:0x81,2:0x89,3:0x89,4:0x4E,5:0,6:0,7:0},
		'H':{0:0xFF,1:0x10,2:0x10,3:0x10,4:0xFF,5:0,6:0,7:0},
		'I':{0:0x81,1:0x81,2:0xFF,3:0x81,4:0x81,5:0,6:0,7:0},
		'J':{0:0x06,1:0x01,2:0x01,3:0x01,4:0xFE,5:0,6:0,7:0},
		'K':{0:0xFF,1:0x18,2:0x24,3:0x42,4:0x81,5:0,6:0,7:0},
		'L':{0:0xFF,1:0x01,2:0x01,3:0x01,4:0x01,5:0,6:0,7:0},
		'M':{0:0xFF,1:0x40,2:0x30,3:0x40,4:0xFF,5:0,6:0,7:0},
		'N':{0:0xFF,1:0x40,2:0x30,3:0x08,4:0xFF,5:0,6:0,7:0},
		'O':{0:0x7E,1:0x81,2:0x81,3:0x81,4:0x7E,5:0,6:0,7:0},
		'P':{0:0xFF,1:0x88,2:0x88,3:0x88,4:0x70,5:0,6:0,7:0},
		'Q':{0:0x7E,1:0x81,2:0x85,3:0x82,4:0x7D,5:0,6:0,7:0},
		'R':{0:0xFF,1:0x88,2:0x8C,3:0x8A,4:0x71,5:0,6:0,7:0},
		'S':{0:0x61,1:0x91,2:0x91,3:0x91,4:0x8E,5:0,6:0,7:0},
		'T':{0:0x80,1:0x80,2:0xFF,3:0x80,4:0x80,5:0,6:0,7:0},
		'U':{0:0xFE,1:0x01,2:0x01,3:0x01,4:0xFE,5:0,6:0,7:0},
		'V':{0:0xF0,1:0x0C,2:0x03,3:0x0C,4:0xF0,5:0,6:0,7:0},
		'W':{0:0xFF,1:0x02,2:0x0C,3:0x02,4:0xFF,5:0,6:0,7:0},
		'X':{0:0xC3,1:0x24,2:0x18,3:0x24,4:0xC3,5:0,6:0,7:0},
		'Y':{0:0xE0,1:0x10,2:0x0F,3:0x10,4:0xE0,5:0,6:0,7:0},
		'Z':{0:0x83,1:0x85,2:0x99,3:0xA1,4:0xC1,5:0,6:0,7:0},
		'1':{0:0x00,1:0x41,2:0xFF,3:0x01,4:0x00,5:0,6:0,7:0},
		'2':{0:0x43,1:0x85,2:0x89,3:0x91,4:0x61,5:0,6:0,7:0},
		'3':{0:0x42,1:0x81,2:0x91,3:0x91,4:0x6E,5:0,6:0,7:0},
		'4':{0:0x18,1:0x28,2:0x48,3:0xFF,4:0x08,5:0,6:0,7:0},
		'5':{0:0xF2,1:0x91,2:0x91,3:0x91,4:0x8E,5:0,6:0,7:0},
		'6':{0:0x1E,1:0x29,2:0x49,3:0x89,4:0x86,5:0,6:0,7:0},
		'7':{0:0x80,1:0x8F,2:0x90,3:0xA0,4:0xC0,5:0,6:0,7:0},
		'8':{0:0x6E,1:0x91,2:0x91,3:0x91,4:0x6E,5:0,6:0,7:0},
		'9':{0:0x70,1:0x89,2:0x89,3:0x8A,4:0x7C,5:0,6:0,7:0}

		}

		self.symbol={
		'email':{0:{0:0b00000000 ,1:0 ,2:0 ,3:0 ,4:0 ,5:0 ,6:0 ,7:0},
				 1:{0:0xFF ,1:0b01000001 ,2:0b00100001 ,3:0b00010001 ,4:0b00010001 ,5:0b00100001 ,6:0b01000001 ,7:0xFF},
				 2:{0:0xFF,1:0b01000001 ,2:0b00100001 ,3:0b00010001 ,4:0b00010001 ,5:0b00100001 ,6:0b01000001 ,7:0xFF},
				 3:1
				 }

		}


		self.string = "1234567 "
		self.stringpointer = 0
		self.string_write = True
		self.string_end = False

		#self.letter =  {'A':{0:0x7F,1:0x0,2:0x0,3:0,4:0x0,5:0,6:0,7:0}}

		self.shift=13
		self.anti_shift=3
		#time control vars
		self.tempo=0
		self.elapsedtime= timeit.default_timer()


		self.ser = serial.Serial()
		self.ser.baudrate = 115200	
		self.ser.bytesize = serial.EIGHTBITS #number of bits per bytes
		self.ser.parity   = serial.PARITY_NONE #set parity check: no parity
		self.ser.stopbits = serial.STOPBITS_ONE #number of stop bits		
		self.ser.timeout  = 0.5

		self.ser.port = "/dev/ttyUSB0"

		self.ser.open()
		self.data_send = Queue.Queue()
		self.TurnAllOff(0)
		self.TurnAllOff(1)
		self.TurnAllOff(2)
		self.SerialThread_call()

	def Symbol(self, symbol):
		self.matriz = self.symbol[symbol]

		self.data_send.put(self.matriz)

	def matrix_print(self, string, cor):
		self.TurnAllOff(0)
		self.TurnAllOff(1)
		self.TurnAllOff(2)
		

		self.string = string
		self.TurnAllOff(cor)
		if self.string[len(self.string)-1] != ' ':
			self.string = self.string + ' '

		self.stringpointer = 0
		self.string_write = True
		while self.string_write == True:
			self.ProcessData(cor)
			time.sleep(0.01)


	def TurnAllOff(self, var):
		self.matriz[var] = dict(map(lambda (k,v): (k, 255), self.matriz[var].iteritems()))

	def TurnAllOn(self, var):
		self.matriz [var] = dict(map(lambda (k,v): (k,0), self.matriz[var].iteritems()))

	# def turn90(self):
	# 	aux_matrix = self.matriz
	# 	for n in range (0,3):
	# 		for j in range (8,0):
	# 			for i in range (0,8):
	# 				deleter = 0
	# 				deleter = (1<<i)
	# 				xpto = (self.matriz[n][j] & deleter) 
	# 				if xpto>0:
	# 					aux_matrix[n][j] = ((aux_matrix[n][j]<<1)+1)
	# 				else:
	# 					aux_matrix[n][j] = (aux_matrix[n][j]<<1) 



		#for k in range(0,3):
		#	for h in range (0,8):
		#		aux_matrix[k][h] = aux_matrix[k][h] & 0xff 
		# self.matriz[1][1] = 10
		
		# self.matriz = aux_matrix





	def ProcessData(self, cor):
		self.elapsedtime = timeit.default_timer()-self.tempo
		if self.elapsedtime > 0.10:
			self.tempo = timeit.default_timer()
			self.TurnAllOff(1)
			self.TurnAllOff(0)
			self.TurnAllOff(2)
			#self.matriz[1] = self.letter['A']
			if self.shift == -6:
				self.shift = 13
			else:
				self.shift = self.shift -1

			#print self.shift


			if self.shift == 0:
				self.shift= 6
				if self.stringpointer<(len(self.string)-2):
					self.stringpointer = self.stringpointer+1
				elif self.string_end == False:
					self.string_write = False

			#print self.string_write
			if self.string_write == True:
				self.letterwrite(cor,self.string[self.stringpointer],self.string[self.stringpointer+1],self.shift)
			else:
				self.stringpointer = 0
				

			#self.letterwrite(1,'A','A',self.shift)


	def letterwrite(self, cor, letter1,letter2, shift):

		aux_final = self.letter[letter1]
		#aux_final1 = self.letter['B']


		if shift>=0 and shift<=5:
			first_shift = 5-shift
			primeiro = True
			write_first = True
		elif shift<13:
			first_shift = shift -5
			primeiro = False
			write_first = True
		else:
		 	write_first = False

		if write_first:
			if primeiro:
				for key in range(0,8-first_shift):
					self.matriz[cor][key] = aux_final[key+first_shift]^255
			else:
				for key in range(0,8):
					self.matriz[cor][key+first_shift] = aux_final[key]^255	


		aux_final = self.letter[letter2]

		shift = shift + 6
		write_second = False
		if shift>=0 and shift<=5:
			first_shift = 5-shift
			primeiro = True
			write_second = True
		elif shift<13:
			first_shift = shift-5
			primeiro = False
			write_second = True
		else:
			write_second = False

		if write_second:
			if primeiro:
				for key in range(0,8-first_shift):
					self.matriz[cor][key] = aux_final[key+first_shift]^255
			else:
				for key in range(0,8):
					self.matriz[cor][key+first_shift] = aux_final[key]^255		

		#self.TurnAllOn(0)
		#self.turn90()
		self.data_send.put(self.matriz)

	
	def SerialThread_call(self):

		self.t = Thread(target=self.SerialThread)
		self.t.start()		
	

	def SerialThread(self):
		self.ser.write(chr(2))
		
		while self.matriz[3]==1:
			try:
				self.matriz = self.data_send.get_nowait()	
			except Queue.Empty:

				pedido = self.ser.readline()
				#print pedido
				#if(pedido[2:3]=='d'):
				#	self.ser.write(chr(1))

				#find my control char
				try:
					request_start = pedido.index('-')
					request_start = request_start + 1 		#offset for remove the control char
					request_end = request_start +2			#offset for remove the second (in the end) control char
				except ValueError:							#just in case the control char cannot be found
											#in this case just send a '1' to unlock matrix soft. and try read again
					continue

				#print pedido	#so, if everything goes ok lets print it just for debug 
				resposta = chr(self.matriz[int(pedido[request_start:(request_end-1)])][int(pedido[request_start+1:request_end])])
				#time.sleep(0.000001)
				#resposta = chr(0)
				self.ser.write(resposta)
				
				#print self.matriz[int(pedido[request_start:(request_end-1)])][int(pedido[request_start+1:request_end])]
				#time.sleep(0.0002)
				#print ord(resposta)
matrix = Serial_Matrix()
signal.signal(signal.SIGINT, SIGINT_handler)
