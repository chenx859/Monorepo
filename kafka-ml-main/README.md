
# kafka-ml

This project intends to dissect the intricacies connecting the realm of streaming with the domain of data science. 




## Installation

1. Create a virtual environment :
```bash
python3 -m venv myenv
```
2. Activate your virtual environment : 

```bash
source myenv/bin/activate
```
3. Start zookeeper service :

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```
4. Start kafka broker :
```bash
bin/kafka-server-start.sh config/server.properties
```

5. Create the topic cpu_data : 
```bash
bin/kafka-topics.sh --create --topic cpu_data --bootstrap-server localhost:9092 --create partitions 3 --replication-factor 1
```

6. Run the script to start producing to the topic ( producer.py ) :

```bash
python src/data_streaming/producer.py
```

7. Check if the 'cpu_data' topic is receiving data :

```bash
bin/kafka-console-consumer.sh  --topic cpu_data --bootstrap-server localhost:9092
```
8. Create the topic 'anomalies' :
```bash
bin/kafka-topics.sh --create --topic anomalies --bootstrap-server localhost:9092 --create partitions 3 --replication-factor 1
```

9. Run the script that will allow our model to detect the anomalies and publish them to the 'anomalies' topic :
```bash
python3 src/data_streaming/detector.py
```

10. list the anomalies from the 'anomalies' topic :
```bash
bin/kafka-console-consumer.sh  --topic anomalies --bootstrap-server localhost:9092
```

10. Start Kafdrop UI using docker combose:
```bash
docker compose up -d
```
