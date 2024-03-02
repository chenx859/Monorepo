
# kafka-ml

This project intends to dissect the intricacies connecting the realm of streaming with the domain of data science. 


## Installation

1. Create a virtual environment using conda :
```bash
python3 -m venv myenv
```
2. Activate your virtual environment : 

```bash
source myenv/bin/activate
```
3. Start zookeeper, kafka and kafdrop service :

```bash
docker compose up -d
```

4. Create the topic cpu_data : 
```bash
bin/kafka-topics.sh --create --topic cpu_data --bootstrap-server localhost:9092 --create partitions 3 --replication-factor 1
```

5. Run the script to start producing to the topic ( producer.py ) :

```bash
python src/data_streaming/producer.py
```

6. Check if the 'cpu_data' topic is receiving data :

```bash
bin/kafka-console-consumer.sh  --topic cpu_data --bootstrap-server localhost:9092
```
7. Create the topic 'anomalies' :
```bash
bin/kafka-topics.sh --create --topic anomalies --bootstrap-server localhost:9092 --create partitions 3 --replication-factor 1
```

8. Run the script that will allow our model to detect the anomalies and publish them to the 'anomalies' topic :
```bash
python3 src/data_streaming/detector.py
```

9. list the anomalies from the 'anomalies' topic :
```bash
bin/kafka-console-consumer.sh  --topic anomalies --bootstrap-server localhost:9092
```
