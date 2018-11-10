# qinsti
# Amazon server :

	1. An HTTP Server, listening on a port 8081.
	2. Has following end-points:
		a. POST /register-request
			Returns a unique ID, to be passed on to next request
		b. GET /request-data/:id
			If <id> is even, returns { sold: true }
			If <id> is odd, returns { sold: false }

# To run the amazon server: python index.py