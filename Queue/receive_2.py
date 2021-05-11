#!/usr/bin/env python

#Link -> https://www.rabbitmq.com/tutorials/tutorial-one-python.html

#Receber mensagem da queue

#Módulos
import pika,sys,os

def main():
    #Ligação
    credentials = pika.PlainCredentials('', '')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='', port=5672, credentials=credentials,heartbeat=480))
    channel = connection.channel()
    #Verificar se a queue existe se não existir cria uma nova
    #Posso correr o programa quantas vezes quiser a queue só irá ser criada uma vez
    channel.queue_declare(queue='hello')

    #Função retorno de chamada
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    #Indicação de que queue queremos receber a mensagem
    channel.basic_consume(queue='hello',
                          on_message_callback=callback,
                          auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
