#!/usr/bin/env python

#link -> https://www.rabbitmq.com/tutorials/tutorial-two-python.html

#Módulos
import pika
import sys

#Ligação
credentials = pika.PlainCredentials('', '')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='', port=5672, credentials=credentials,heartbeat=480))
channel = connection.channel()
#Indicação da queue
channel.queue_declare(queue='task_queue', durable=True)

#Permite que mensagens arbitárias sejam enviadas da linha de comando
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent %r" % message)
connection.close()