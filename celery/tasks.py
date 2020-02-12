from celery import Celery
import time
from kombu import Queue, Exchange

result_backend = 'db+postgresql://postgres:postgres@localhost/postgres'
app = Celery('tasks', broker='amqp://localhost//', backend=result_backend)

app.conf.task_queues = (
    Queue('add',    routing_key='tasks.add', exchange=Exchange('celery', type="direct")),
    Queue('substract', routing_key='tasks.substract', exchange=Exchange('celery', type="direct")),
    Queue('multiply',   routing_key='tasks.multiply', exchange=Exchange('celery', type="direct")),
)

@app.task
def add(x, y):
    time.sleep(10)
    return x + y

@app.task
def substract(x, y):
    time.sleep(20)
    return x - y

@app.task
def multiply(x, y):
    time.sleep(10)
    return x * y