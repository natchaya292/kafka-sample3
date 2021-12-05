from kafka import KafkaConsumer
consumer = KafkaConsumer(bootstrap_servers='54.235.235.33:9093')
consumer.subscribe(['btc'])
for msg in consumer:
    #assert isinstance(msg.value, dict)
    print(msg.value)