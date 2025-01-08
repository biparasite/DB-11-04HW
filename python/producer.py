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
channel.basic_publish(exchange='hw-netology', routing_key='hello', body='Hello Netology!')
connection.close()
