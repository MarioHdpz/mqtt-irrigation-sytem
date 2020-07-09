"""Module to store settings"""
import os

HOST = os.environ.get("MQTT_HOST") 
PORT = int(os.environ.get("MQTT_PORT"))
USER = os.environ.get("MQTT_USER")
PASSWORD = os.environ.get("MQTT_PASSWORD") 