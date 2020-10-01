# Run Elastticsearch and Kibana using Docker Compose

## Instructions
- Just run **docker-compose up -d** to run Elasticsearch and Kibana in detached mode
- Elasticsearch will be available in http://localhost:9200 and Kibana UI in http://localhost:5601
- You may need to wait a bit till Elasticsearch status becomes ready (Green), to insepect the logs run **docker-compose logs -f**
- This is only suitable for learning purposes. Do not use in production.


