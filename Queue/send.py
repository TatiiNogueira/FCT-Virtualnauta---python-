#!/usr/bin/env python

#Link -> https://www.rabbitmq.com/tutorials/tutorial-one-python.html

#Enviar para a queue

#Módulos
import pika

#Ligação
credentials = pika.PlainCredentials('', '')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='', port=5672, credentials=credentials,heartbeat=480))
channel = connection.channel()
#Criar a queue - hello será o nome da mesma
#Verificar se a queue existe se não existir cria uma nova
#Posso correr o programa quantas vezes quiser a queue só irá ser criada uma vez
channel.queue_declare(queue='hello')

#Expecificação de qual é a queue e o text (body)
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

#Fechar a conecção
connection.close()