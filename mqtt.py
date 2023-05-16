from paho.mqtt import client as mqtt_client
import random
import time
broker = 'localhost'
port = 1883
topic = "Prueba1"
client_id = f'python-mqtt-{random.randint(0, 1000)}'

print(client_id)

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    msg_count = 0
    while True:
        time.sleep(5)
        #msg = f"messages: {msg_count}"
        gas  = random.randint(0,10)
        humo = random.randint(0,10)
        luz  = random.randint(0,100)
        
        msg = '{"Sensor":"Gas","Valor":'+str(gas)+'}'
        result = client.publish(topic, msg)

        msg = '{"Sensor":"Humo","Valor":'+str(gas)+'}'

        msg = '{"Sensor":"Humedad","Valor":'+str(gas)+'}'
        result = client.publish(topic, msg)

        msg = '{"Sensor":"CO2","Valor":'+str(gas)+'}'
        result = client.publish(topic, msg)

        msg = '{"Sensor":"Luz","Valor":'+str(luz)+'}'
        result = client.publish(topic, msg)
        



        
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()

