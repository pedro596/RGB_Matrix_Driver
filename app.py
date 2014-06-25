from matrix import *
import email
'''
	object 'matrix' defined by default because the SIGINT handling

'''

while True:

	time.sleep(2)
	if email.unread_email()>0:
		matrix.Symbol('email')
		time.sleep(2)
		if email.unread_email()>1:
			message = 'TEM ' +str(email.unread_email())+ ' EMAILS POR LER'
		else:
			message = 'TEM ' +str(email.unread_email())+ ' EMAIL POR LER'

		matrix.matrix_print(message,0)
		matrix.Symbol('email')
		print 'Ola'

matrix.t.join()