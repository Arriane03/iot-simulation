# Projet IoT – Simulation MQTT sécurisée avec TLS



## Objectif du projet
Ce projet a pour objectif de simuler une architecture IoT sécurisée en utilisant le protocole MQTT.  
Un capteur IoT envoie périodiquement des données (température simulée) vers le edge, qui les reçoit via un broker Mosquitto sécurisé, puis les données sont visualisées sous forme de graphe en temps réel.

Ce projet met en œuvre :
- la communication MQTT
- la sécurisation par certificats TLS
- l’authentification par identifiant/mot de passe
- la visualisation de données IoT



### Rôle des composants
- capteur.py : simule un capteur IoT qui publie des données
- edge.py : agit comme un nœud edge qui reçoit et traite les données
- graph.py : souscrit au topic MQTT et affiche les données sous forme de graphe
- Mosquitto : broker MQTT sécurisé avec TLS


## Sécurité mise en place
- MQTT sécurisé via TLS
- Authentification par username / password
- Certificats SSL :
  - `mosquitto.crt`
  - `mosquitto.key`
- Les fichiers sensibles sont exclus du dépôt via `.gitignore`

##  Prérequis

- Windows 
- Python 
- Git
- Mosquitto MQTT Broker

## Installation

## Cloner le projet
git clone https://github.com/Arriane03/iot-simulation.git
cd iot-simulation

## Créer un environnement virtuel Python
python -m venv .venv
.venv\Scripts\Activate.ps1


## Installer les dépendances Python
pip install paho-mqtt matplotlib numpy


## Télécharger Mosquitto depuis le site officiel 

## Configuration MQTT (local) 
Les fichiers de sécurité (passwd, .key, .crt) ne sont pas présents sur GitHub pour des raisons de sécurité.

## Créer le fichier d’authentification
(Utilisateur et mdp)

## Modifier le fichier d’authentification (mosquitto.conf)

### exemple
 

listener 8883
protocol mqtt

(TLS)
cafile C:\Program Files\mosquitto\mosquitto.crt
certfile C:\Program Files\mosquitto\mosquitto.crt
keyfile C:\Program Files\mosquitto\mosquitto.key
require_certificate false

(Authentification)
allow_anonymous false
password_file C:\Program Files\mosquitto\passwd

(Logs)
log_type all

## Lancer le broker MQTT sécurisé
mosquitto -c mosquitto.conf -v

## Enfin, exécuter le projet
- python edge.py 
- python capteur.py (Simulation de capteur IOT)
- python graph.py (Visualisation en temps réel)





###  Auteur
Teufack Arriane