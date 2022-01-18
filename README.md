1) Pull the docker image Elasticsearch:
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.16.3

2) Run Elasticsearch in docker:
docker run -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.16.3

3) Run app:
uvicorn main:app 



