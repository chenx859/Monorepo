
# kafka-ml

This project I will demonstrate the change data capture approach to data ingestion.

## Installation

1. Start zookeeper, debezium, kafka and postgres service :

```bash
cd debezium_kafka_CDC/postgres-docker
docker compose up -d
```

2. Go to postgres container and login: 
```bash
docker ps
docker exec -it d18401215fff bash
psql -U postgresuser -d shipment_db -W
select * from shipments;
```

3. Log in to the Debezium container and execute this in a terminal to create debezium connecter:
```bash
curl -H 'Content-Type: application/json' debezium:8083/connectors --data '
{
  "name": "shipments-connector",  
  "config": {
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector", 
    "plugin.name": "pgoutput",
    "database.hostname": "postgres", 
    "database.port": "5432", 
    "database.user": "postgresuser", 
    "database.password": "postgrespw", 
    "database.dbname" : "shipment_db", 
    "database.server.name": "postgres", 
    "table.include.list": "public.shipments" 
  }
}'
```

4. Log in to the Postgres container and execute the following query:
```bash
update shipments set status='COMPLETED' where order_id = 12500;
```

5. To see the content, execute the following:
```bash
docker run --tty \
--network postgres-docker_default \
confluentinc/cp-kafkacat \
kafkacat -b kafka:9092 -C \
-s key=s -s value=avro \
-r http://schema-registry:8081 \
-t postgres.public.shipments
```


## Useful commands
Inside kafka container:
- `kafka-topics --bootstrap-server kafka:9092 --list`: List all Kafka topics 
- `kafka-console-producer --bootstrap-server kafka:9092 --topic postgres.public.shipments`: Consult messages from a topic
- `kafka-console-consumer --bootstrap-server kafka:9092 --topic postgres.public.shipments --from-beginning`: Consume message from a topic
