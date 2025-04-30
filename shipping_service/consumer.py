import json
import uuid
from datetime import datetime
from kafka import KafkaConsumer
from pymongo import MongoClient

# 1) Kafka consumer
consumer = KafkaConsumer(
    'order-confirmed',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# 2) MongoDB connection
client = MongoClient("mongodb://localhost:27018/")
db = client.shipping_db
collection = db.shippings

# 3) Listen and save
for msg in consumer:
    order = msg.value
    record = {
        "itemId":    order["itemId"],
        "itemName":  order["itemName"],
        "quantity":  order["quantity"],
        "trackingId": f"SHIP-{uuid.uuid4().hex[:6].upper()}",
        "status":    "pending",
        "createdAt": datetime.utcnow()
    }
    collection.insert_one(record)
    print("Saved shipping record:", record)
