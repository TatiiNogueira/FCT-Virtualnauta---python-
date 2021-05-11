#!/usr/bin/env python

#link -> https://www.rabbitmq.com/tutorials/tutorial-two-python.html

#Módulos
import pika
import time

#Ligação
credentials = pika.PlainCredentials('', '')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='', port=5672, credentials=credentials,heartbeat=480))
channel = connection.channel()
#Indicação da queue e declará-la como durável
channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()