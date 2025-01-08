#!/usr/bin/env python
# coding=utf-8
import pika

credentials = pika.PlainCredentials(username='rabbitmq', password='rabbitmq')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        'localhost', credentials=credentials
        )
    )
channel = connection.channel()
channel.queue_declare(queue='hw-netology-q')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume('hw-netology-q', callback, auto_ack=True)
channel.start_consuming()
