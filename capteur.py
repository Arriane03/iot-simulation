import paho.mqtt.client as mqtt
import ssl
import time
import random

# ===== CONFIG =====
BROKER = "localhost"
PORT = 8883
TOPIC = "iot/temperature"

USERNAME = "capteur"
PASSWORD = "capteur123"

CA_CERT = "C:/Program Files/mosquitto/mosquitto.crt"

# ===== MQTT CLIENT =====
client = mqtt.Client(
    client_id="capteur_01",
    protocol=mqtt.MQTTv311
)

# Authentification
client.username_pw_set(USERNAME, PASSWORD)

# TLS
client.tls_set(
    ca_certs=CA_CERT,
    tls_version=ssl.PROTOCOL_TLSv1_2
)
client.tls_insecure_set(True)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(" Capteur connecté au broker MQTT sécurisé")
    else:
        print(f" Connexion refusée (capteur), code : {rc}")

client.on_connect = on_connect

# Connexion
client.connect(BROKER, PORT)
client.loop_start()

# ===== SIMULATION CAPTEUR =====
try:
    while True:
        temperature = round(random.uniform(25, 35), 2)
        print(f"[Capteur] Température mesurée: {temperature}°C")

        client.publish(TOPIC, temperature)

        if temperature >= 30:
            print(" [ALERTE] Température critique détectée !")

        time.sleep(5)

except KeyboardInterrupt:
    print("\n Capteur arrêté")
    client.loop_stop()
    client.disconnect()
