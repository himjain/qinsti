import time

class RequestUtils: 

	def generate_unique_id (self):
		return int(round(time.time() * 1000))