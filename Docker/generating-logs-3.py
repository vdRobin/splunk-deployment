import requests
import time
import random
import os
import json

# Paramètres de destination basés sur une variable d'environnement
def str_to_bool(value):
    """Convertit une chaîne en booléen, accepte plusieurs formats."""
    return value.lower() in ("true", "1", "yes", "on") if value else False

IS_LOCAL = str_to_bool(os.getenv("IS_LOCAL", "false"))  # Par défaut, False si non défini
SPLUNK_HOST = "host.docker.internal" if IS_LOCAL else "splunk-idxc-test-indexer-headless.siem.svc.cluster.local"
SPLUNK_PORT = 8088  # Le port HEC
SPLUNK_TOKEN = "<ton_token_hec>"  # Remplace par ton token HEC

LOG_TEMPLATES = [
    "<134>1 {timestamp} FortiGate-100 srcip={src_ip} dstip={dst_ip} action=deny msg=\"Failed login attempt\"",
    "<134>1 {timestamp} CheckPoint srcip={src_ip} dstip={dst_ip} action=drop msg=\"DDoS detected\" packets={packets}",
    "<134>1 {timestamp} FortiGate-100 srcip={src_ip} dstip={dst_ip} action=accept msg=\"HTTP request to suspicious URL\"",
]

def generate_log():
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    src_ip = f"192.168.{random.randint(1, 254)}.{random.randint(1, 254)}"
    dst_ip = f"10.0.{random.randint(1, 254)}.{random.randint(1, 254)}"
    packets = random.randint(100, 10000) if "DDoS" in LOG_TEMPLATES[1] else 1
    log = random.choice(LOG_TEMPLATES).format(timestamp=timestamp, src_ip=src_ip, dst_ip=dst_ip, packets=packets)
    return log

def send_logs():
    url = f"http://{SPLUNK_HOST}:{SPLUNK_PORT}/services/collector/event"
    headers = {
        'Authorization': f'Splunk {SPLUNK_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    while True:
        start_time = time.time()
        
        # Envoi des logs pendant 5 secondes
        while time.time() - start_time < 5:
            log = generate_log()
            data = {
                "event": log,
                "sourcetype": "_json",  # Spécifie le type de source si nécessaire
                "index": "main"  # Remplace par ton index
            }
            try:
                response = requests.post(url, headers=headers, data=json.dumps(data))
                if response.status_code == 200:
                    print(f"Sent: {log}")
                else:
                    print(f"Error sending log: {response.status_code} - {response.text}")
            except Exception as e:
                print(f"Error: {e}")
            time.sleep(random.uniform(0.1, 1))  # Pause aléatoire entre les logs
        
        print("Pausing for 10 seconds...")
        time.sleep(10)  # Pause de 10 secondes avant le prochain envoi de logs

if __name__ == "__main__":
    send_logs()
