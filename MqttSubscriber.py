import paho.mqtt.client as mqtt
import serial

MQTT_SERVER = "192.168.2.3"
MQTT_PATH = "Rover"
serialPort = serial.Serial('/dev/ttyACM0')

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected to", MQTT_PATH)

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    m_decoded = str(msg.payload.decode("utf-8", "ignore").strip())
    print("Direction recived:" , m_decoded)
    serialPort.write(m_decoded.encode("utf-8"))
    print("Direction sent")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)
client.loop_forever()