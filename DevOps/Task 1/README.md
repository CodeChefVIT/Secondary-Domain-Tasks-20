# Run Elastticsearch and Kibana using Docker Compose

## Instructions
- Just run **docker-compose up -d** to run Elasticsearch and Kibana in detached mode
- Elasticsearch will be available in http://localhost:9200 and Kibana UI in http://localhost:5601
- You may need to wait a bit till Elasticsearch status becomes ready (Green), and the Kibana server initiates. You can view this by insepecting the logs. To do that run **docker-compose logs -f**
- To stop the Elasticsearch and Kibana containers, run - **docker-compose stop**
- To stop and completly remove all the containers, networks, volumes created by Elasticsearch and Kibana, run - **docker-compose down**
- This is only suitable for learning purposes. Do not use in production.
