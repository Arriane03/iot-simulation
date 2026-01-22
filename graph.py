import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# CONFIG BROKER 
BROKER = "localhost"
PORT = 8883          
TOPIC = "iot/temperature"
USERNAME = "edge"    
PASSWORD = "edge123"  

CERT_PATH = "C:/Program Files/mosquitto/mosquitto.crt"

# DONNÉES 
x_data = []
y_data = []
start_time = time.time()

#  CALLBACK 
def on_message(client, userdata, msg):
    try:
        temp = float(msg.payload.decode())
        t = time.time() - start_time
        x_data.append(t)
        y_data.append(temp)
        print(f"[GRAPH] Température reçue : {temp}°C")
    except Exception as e:
        print(f"Erreur lecture message : {e}")

# CLIENT MQTT 
client = mqtt.Client(client_id="graph_client")
client.tls_set(CERT_PATH)            # TLS activé
client.username_pw_set(USERNAME, PASSWORD)
client.on_message = on_message

client.connect(BROKER, PORT)
client.subscribe(TOPIC)
client.loop_start()  # démarrage de la boucle MQTT en arrière-plan

#  CONFIG GRAPHE 
fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    ax.plot(x_data, y_data, marker='o', color='blue')
    ax.set_title("Température reçue")
    ax.set_xlabel("Temps (s)")
    ax.set_ylabel("Température (°C)")
    ax.grid(True)
    if y_data:
        ax.set_ylim(min(y_data) - 1, max(y_data) + 1)

ani = FuncAnimation(fig, update, interval=1000, cache_frame_data=False)  # mise à jour toutes les 1s
plt.show()