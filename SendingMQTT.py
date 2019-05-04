import paho.mqtt.client as mqtt #import the client1
import time

info = "hello world"

def message_creator(client,topic_name,info):
    message = info
    #print("Subscribing to topic", topic_name)
    client.subscribe(topic_name)
    #print("Publishing message to topic",topic_name)
    client.publish(topic_name,message)

def main(info):
    broker_address="192.168.2.3"
    instance = "Driving"
    topic_name = "Rover"
    #print("creating new instance")
    client = mqtt.Client(instance)  #create new instance
    #print("connecting to broker")
    client.connect(broker_address)  #connect to broker
    client.loop_start()             #start the loop
    message_creator(client, topic_name, info)
    client.loop_stop()              #stop the loop

if __name__ == "__main__":
    main(info)