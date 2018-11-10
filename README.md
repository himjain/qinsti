# qinsti - on Python 2.7.10
# Amazon server :

	1. An HTTP Server, listening on a port 8081.
	2. Has following end-points:
		a. POST /register-request
			Returns a unique ID
			Writes the message to a queue due to overloaded amazon server to be consumed by another process
		b. GET /request-data/:id
			If <id> is even, returns { sold: true }
			If <id> is odd, returns { sold: false }

#To run rmq:
  pip install pika

# To run the amazon server: python amazon/index.py 
