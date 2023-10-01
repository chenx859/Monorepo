
# kafka-ml

This project I will demonstrate the change data capture approach to data ingestion.

## Installation

1. Start zookeeper, debezium, kafka and postgres service :

```bash
docker compose up -d
```

2. Go to postgres container and login: 
```bash
docker ps
docker exec -it 4446bcaed1b4 bash
psql -U docker -d exampledb -W
```

3. create a table :

```bash
create table student (id integer primary key, name varchar)
select * from student
alter table public.student replica identity full
```

4. Register a Debezium connector to stream changes from exampledb :

```bash
curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" 127.0.0.1:8083/connectors/ --data "@debezium.json"
```

5. To see the content, execute the following :
```bash
docker run --tty \
--network postgres_debezium_cdc_default \
confluentinc/cp-kafkacat \
kafkacat -b kafka:9092 - C \
-s key=s -s value=avro \
-r http://schema-registry:8081 \
-t postgres.public.student
```