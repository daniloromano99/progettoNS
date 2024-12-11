# Base image for Elasticsearch
FROM docker.elastic.co/elasticsearch/elasticsearch:8.10.2 AS elasticsearch

# Set environment variables for Elasticsearch
ENV discovery.type=single-node

# Copy custom configuration for Elasticsearch
COPY elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml

# Expose ports for Elasticsearch
EXPOSE 9200 9300

# Base image for Kibana
FROM docker.elastic.co/kibana/kibana:8.10.2 AS kibana

# Copy custom configuration for Kibana
COPY kibana.yml /usr/share/kibana/config/kibana.yml

# Expose port for Kibana
EXPOSE 5601

# Start Elasticsearch and Kibana
CMD ["bash", "-c", "service elasticsearch start && kibana"]
