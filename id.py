import random
import datetime
import string

def generate_order_id():
    prefix = random.choice(["ORN"])
    date_part = datetime.datetime.now().strftime("%Y%m%d")
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return f"{prefix}-{random_part}"

# Example: generate 10
for _ in range(10):
    print(generate_order_id())
