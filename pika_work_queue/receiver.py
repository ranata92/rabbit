import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='background_tasks', durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag) # acknowledge the processing of a message

channel.basic_qos(prefetch_count=1) # make sure that consumer doesn't get the messa if it didn't process previous one
channel.basic_consume(
    queue='hello',
    on_message_callback=callback
)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()