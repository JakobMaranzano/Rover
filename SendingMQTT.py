import paho.mqtt.client as mqtt #import the client1
import time

#def on_message(client, userdata, message):
    #print("message received " ,str(message.payload.decode("utf-8")))
    #print("message topic=",message.topic)
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)
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
    #client.on_message=on_message   #attach function to callback
    #print("connecting to broker")
    client.connect(broker_address)  #connect to broker
    client.loop_start()             #start the loop
    message_creator(client, topic_name, info)
    #time.sleep(4)                   #wait
    client.loop_stop()              #stop the loop

if __name__ == "__main__":
    main(info)