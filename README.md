1) Pull the docker image Elasticsearch:\
<code>docker pull docker.elastic.co/elasticsearch/elasticsearch:7.16.3</code>

2) Run Elasticsearch in docker:\
<code>docker run -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.16.3</code>

3) Run app:\
<code>uvicorn main:app</code>



