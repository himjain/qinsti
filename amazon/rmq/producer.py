#!/usr/bin/env python
import pika
from config.rmqConfig import RmqConfig as rmq_conf

class RMQProducer: 
	
	def __init__(self, queue):
		self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=rmq_conf.host))
		self.channel = self.connection.channel()
		self.channel.queue_declare(queue)

	def publish(self, message) :
		self.channel.basic_publish(exchange='',routing_key=rmq_conf.routing_key,body=message)
		print(" [x] Sent " + message)	

