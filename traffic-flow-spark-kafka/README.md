# traffic-flow-spark-kafka
Testing Spark Structured Streaming and Kafka with real data from traffic sensors 

1. To start the environment, just run:
```bash
docker-compose up -d
```

2. Access the Kafka container terminal and create a Kafka topic from where our spark job will consume the messages.
```bash
kafka-topics.sh --create --bootstrap-server localhost:9092 --topic test_topic
```

3. To simulate a producer writing messages on this topic, let’s use the kafka-console-producer. Also inside the container:
```bash
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test_topic --property "parse.key=true" --property "key.separator=:"
```

4. From now, every line typed in the terminal will be sent as a message to the test topic. The character “:” is used to separate the message’s key and value (key:value).
```bash
joao:21
```

5. Access the Spark container and run the job.
```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 /src/streaming/read_test_stream.py
```

6. After testing, download the zip file from AUGUST 2022 and extract it into the /data volume and execute the following:
```bash
spark-submit /src/transform_json_to_parquet.py
spark-submit /src/join_parquet_files.py
```

7. Create the Kafka topic to receive our messages
```bash
kafka-topics.sh --create --replication-factor 1 --bootstrap-server localhost:9092 --topic traffic_sensor
```
Optionally, if you want to display the arriving messages, it’s possible to set up a console consumer.
```bash
kafka-console-consumer.sh --topic traffic_sensor --bootstrap-server localhost:9092
```

8. Read the parquet file write it to the topic by executing the job:
```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 /src/streaming/insert_traffic_topic.py
```

9.  Executing the following to count the number of vehicels by type:
```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 /src/streaming/group_by_vehicle_type.py
```

Medium articale link: https://medium.com/towards-data-science/a-fast-look-at-spark-structured-streaming-kafka-f0ff64107325
