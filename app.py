 from flask import Flask, render_template
 from flask_socketio import SocketIO, emit
 import paho.mqtt.client as mqtt
 import json
 import threading
 import time

 app = Flask(__name__)
 app.config['SECRET_KEY'] = 'secret!'  # Change this!
 socketio = SocketIO(app)

 # MQTT Broker settings
 mqtt_broker = "your_broker_ip"  # Replace with your Mosquitto broker's IP
 mqtt_port = 1883
 mqtt_topics = ["home/+/smoke", "home/+/temperature", "home/+/flame", "home/+/alarm"]
 sensor_data = {}  # Store the latest sensor readings

 # MQTT Callbacks
 def on_connect(client, userdata, flags, rc):
     print("Connected to MQTT Broker with result code " + str(rc))
     for topic in mqtt_topics:
         client.subscribe(topic)

 def on_message(client, userdata, msg):
     # print(msg.topic + " " + str(msg.payload.decode()))
     topic_parts = msg.topic.split('/')
     location = topic_parts[1]
     sensor_type = topic_parts[2]
     value = msg.payload.decode()

     if location not in sensor_data:
         sensor_data[location] = {}
     sensor_data[location][sensor_type] = value

     # Emit data to the frontend via WebSockets
     socketio.emit('sensor_update', {'location': location, 'sensor': sensor_type, 'value': value})

     # Example: Check for alarm and emit
     if sensor_type == "alarm" and value != "":
         socketio.emit('alarm', {'location': location, 'message': value})

 # MQTT Client setup
 mqtt_client = mqtt.Client()
 mqtt_client.on_connect = on_connect
 mqtt_client.on_message = on_message

 def mqtt_thread():
   mqtt_client.connect(mqtt_broker, mqtt_port, 60)
   mqtt_client.loop_forever()
   
 mqtt_thread_instance = threading.Thread(target=mqtt_thread)
 mqtt_thread_instance.daemon = True  # Allow the thread to exit when the main program exits
 mqtt_thread_instance.start()
 

 @app.route('/')
 def index():
     return render_template('index.html')

 if __name__ == '__main__':
     socketio.run(app, debug=True, host='0.0.0.0') # Allow external connections


 
