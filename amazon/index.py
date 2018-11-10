#!/usr/bin/python

from config.ServerConfig import ServerConfig as conf
from server import HttpServer as server
from BaseHTTPServer import HTTPServer


PORT_NUMBER=conf.PORT_NUMBER

if __name__ == '__main__' :

	try:
		#Create a web server and define the handler to manage the incoming request
		server = HTTPServer(('', PORT_NUMBER), server.httpHandler)
		print 'Started listening on port ' , PORT_NUMBER
		
		#Wait forever for incoming htto requests
		server.serve_forever()

	except KeyboardInterrupt:
		print 'KeyboardInterrupt received, shutting down the web server'
		server.socket.close()
	except Exception,e: 
		print "an exception occurred" , e