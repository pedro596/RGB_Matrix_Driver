import imaplib

obj = imaplib.IMAP4_SSL('imap.gmail.com','993')
obj.login('labsis2014@gmail.com','labsisebonito')
obj.select()
obj.search(None,'UnSeen')
print len(obj.search(None, 'UnSeen')[1][0].split())

print obj.search(None, 'UnSeen')[1][0]#.split()

# data = obj.fetch(message, '(BODY[HEADER.FIELDS (SUBJECT FROM)])')
# header_data = data[1][0][1]
# parser = HeaderParser()
# msg = parser.parsestr(header_data)
# print msg
