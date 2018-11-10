from BaseHTTPServer import BaseHTTPRequestHandler
from utils.requestUtils import RequestUtils
from rmq.producer import RMQProducer
from config.rmqConfig import RmqConfig as rmq_conf

utils = RequestUtils ()
RMQProducer = RMQProducer(rmq_conf.queue)

#This class will handles any incoming request

class httpHandler(BaseHTTPRequestHandler):

	#Handler for the GET requests
	def do_GET ( self ):
		try:
			uri_list = filter ( None, self.path.split('/') )
			print uri_list
			if ( uri_list and uri_list[0] == "request-data" ):
				print uri_list[1]
				output = "{sold : true}" if ( int(uri_list[1])%2 == 0 ) else "{sold:false}"
				self.send_response(200)
				self.send_header('Content-type','application/json')
				self.end_headers()
				self.wfile.write(output)
				return
			else: 
				self.send_response(404)
				return
		except Exception,e:
			#log the error rather than printing here
			print e 
			self.send_response(401)
			return

	#Handler for the POST requests
	def do_POST(self):
		try:
			#send the price setting request to a queue 
			#acknowledge by sending a unique id
			if self.path=="/register-request":
				content_len = int(self.headers.getheader('content-length', 0))
				post_body = self.rfile.read(content_len)
				RMQProducer.publish(post_body)
				self.send_response(200)
				self.end_headers()
				self.wfile.write(utils.generate_unique_id())
				return
			else:
				self.send_response(404)
				return
		except Exception,e:
			#log the error
			print e 
			self.send_response(401)
			return
'''
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), httpHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
'''