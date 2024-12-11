#!/bin/bash

# Esegui lo script Python per SQL Injection
echo "Esecuzione di SQL Injection..."
python3 sql_injection.py

# Esegui lo script Python per Traffic Generator
echo "Esecuzione di Traffic Generator..."
python3 traffic_generator.py

# Esegui lo script bash per Port Scan
echo "Esecuzione di Port Scan..."
./port_scan.sh

echo "Tutti gli script sono stati eseguiti."
