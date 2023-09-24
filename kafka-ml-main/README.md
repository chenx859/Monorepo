
# kafka-ml

This project intends to dissect the intricacies connecting the realm of streaming with the domain of data science. 




## Installation

1. Create a virtual environment using conda :
```bash
conda create -n rt-ml
```
you can display the virtual environments that you have in your machine using this command :  

```bash
conda info --envs
```
2. Activate your virtual environment : 

```bash
conda activate rt-ml
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
python src/data_streaming/detector.py
```

10. list the anomalies from the 'anomalies' topic :
```bash
bin/kafka-console-consumer.sh  --topic anomalies --bootstrap-server localhost:9092
```

## 🚀 About Me
My name is Chiheb Mhamdi , I'm an IT-Engineer who is seeking for improving his skills , expanding his knowledge . I'm open to exchange experiences and projects 

## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mhamdi-chiheb//)


[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/__chiheb_mh/)


