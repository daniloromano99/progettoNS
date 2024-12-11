FROM ubuntu:20.04

# Installazione delle dipendenze di sistema necessarie (python, pip, nmap, curl)
RUN apt-get update && apt-get install -y python3 python3-pip nmap curl

# Installazione delle librerie Python necessarie (requests, ecc.)
RUN pip3 install requests

# Copia gli script nella directory /opt/scripts/
COPY scripts/ /opt/scripts/

# Imposta la directory di lavoro
WORKDIR /opt/scripts/

# Rendi eseguibili gli script
RUN chmod +x *.py
RUN chmod +x port_scan.sh
RUN chmod +x start.sh

# Esegui lo script start.sh che eseguirà gli altri 3 script
CMD ["./start.sh"]
