# Usa l'immagine ufficiale di Filebeat
FROM docker.elastic.co/beats/filebeat:8.10.2

# Copia il file di configurazione di Filebeat nella giusta posizione
COPY ./filebeat.yml /usr/share/filebeat/filebeat.yml

# Modifica i permessi del file appena copiato
RUN chmod 644 /usr/share/filebeat/filebeat.yml

# Definisci la directory dei log di Suricata, dove Filebeat leggerà i log
VOLUME ["/var/log/suricata"]

# Configura l'utente per l'esecuzione di Filebeat
USER root

# Avvia Filebeat
CMD ["filebeat", "-e", "-d", "*"]
