medium article: https://medium.com/@stefentaime_10958/free-real-time-flight-status-pipeline-with-kafka-schemas-registry-avro-graphql-postgres-and-7ac59b63ea99

Get access_key for Aviation Stack API https://aviationstack.com/


1. Create a virtual environment using conda :
```bash
python3 -m venv myenv
```
2. Activate your virtual environment : 

```bash
source myenv/bin/activate
```
3. intall all the dependecies
```bash
pip install -r requirements.txt
```
4. Start the docker compose
```bash
docker compose up -d
docker ps
docker exec -it 9784e603fb2d bash
psql -U postgres -d postgres -W
select * from flights;
```
5. Run the producer
```bash
cd Free-Real-time-Flight-Status-Pipeline-main/python_scripts
export access_key= value
python3 ingest.py
```
5. Run the Consumer
```bash
cd python_scripts
python3 consumer.py
```

To remove the persisted volumes, run
```bash
docker volume rm free-real-time-flight-status-pipeline-main_postgres_data
docker volume rm free-real-time-flight-status-pipeline-main_pgadmin_data
```