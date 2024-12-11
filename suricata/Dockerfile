FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y     suricata     net-tools     iputils-ping     && apt-get clean

COPY suricata.yaml /etc/suricata/suricata.yaml
COPY rules/ /etc/suricata/rules/

RUN mkdir -p /var/log/suricata

CMD ["suricata", "-c", "/etc/suricata/suricata.yaml", "-i", "eth0"]