import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='background_tasks', durable=True) #make queue durable
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body=message,
    properties=pika.BasicProperties(delivery_mode=2) #make message persistent
)
print(" [x] Sent f{message}")
connection.close()