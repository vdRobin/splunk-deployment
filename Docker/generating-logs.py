import socket
import time
import random

# Paramètres de destination (Splunk indexer)
SPLUNK_HOST = "splunk-idxc-test-indexer-headless.siem.svc.cluster.local"  # Nom du service Splunk dans Kubernetes
SPLUNK_PORT = 9997  # Port d'entrée Splunk par défaut

# Exemples de logs firewall simulés
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

# Envoi des logs à Splunk via TCP
def send_logs():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((SPLUNK_HOST, SPLUNK_PORT))
        while True:
            log = generate_log()
            sock.sendall((log + "\n").encode('utf-8'))
            print(f"Sent: {log}")
            time.sleep(random.uniform(0.1, 1))  # Simule un flux de logs variable
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    send_logs()