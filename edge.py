import paho.mqtt.client as mqtt
import ssl

# ===== CONFIG =====
BROKER = "localhost"
PORT = 8883
TOPIC = "iot/temperature"

USERNAME = "edge"
PASSWORD = "edge123"

CA_CERT = "C:/Program Files/mosquitto/mosquitto.crt"

# ===== MQTT CLIENT =====
client = mqtt.Client(
    client_id="edge_01",
    clean_session=False,
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

# ===== CALLBACKS =====
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(" Edge connecté au broker MQTT sécurisé")
        client.subscribe(TOPIC)
    else:
        print(f" Connexion refusée (edge), code : {rc}")

def on_message(client, userdata, msg):
    temperature = float(msg.payload.decode())
    print(f"[EDGE] Température reçue : {temperature}°C")

    if temperature >= 30:
        print(" [EDGE] ALERTE reçue : Température critique !")

client.on_connect = on_connect
client.on_message = on_message

# Connexion
client.connect(BROKER, PORT)
client.loop_forever()
