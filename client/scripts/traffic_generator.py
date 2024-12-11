import requests
import time

# Durata per cui inviare le richieste in secondi (90 secondi = 1 minuto e 30 secondi)
timeout = 90

# Iniziamo il timer
start_time = time.time()

while True:
    # Calcoliamo il tempo trascorso
    elapsed_time = time.time() - start_time
    
    # Se il tempo trascorso è maggiore del timeout, interrompiamo
    if elapsed_time > timeout:
        print("Tempo scaduto, interruzione delle richieste HTTP.")
        break
    
    try:
        # Invia una richiesta GET al server
        response = requests.get('http://webserver:80')
        print(f"Received: {response.status_code}")
        
        # Attendi 1 secondo prima di inviare una nuova richiesta
        time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
        break

print("Generazione di traffico HTTP completata.")
