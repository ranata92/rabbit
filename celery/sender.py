from tasks import add, substract, multiply
import time


result = add.apply_async((4, 4), queue='add')
print(f"Job_ID{result}")
print(f"Result status {result.status}")
time.sleep(15)
print(f"Result status {result.status}")
result = substract.apply_async((10, 4), queue='substract')
print(f"Job_ID{result}")
print(f"Result status {result.status}")
time.sleep(15)
print(f"Result status {result.status}")
multiply.apply_async((20, 30), queue='multiply')
print(f"Job_ID{result}")
print(f"Result status {result.status}")
time.sleep(15)
print(f"Result status {result.status}")

