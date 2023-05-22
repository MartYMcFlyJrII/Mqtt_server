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
    nvl_agua_cruda  = None
    nvl_agua_purificada = None
    pm  = None
    cloro = None
    while True:
        time.sleep(5)
        #msg = f"messages: {msg_count}"
        nvl_agua_cruda  = generate_nvl_agua_cruda(nvl_agua_cruda)
        nvl_agua_purificada = generate_nvl_agua_purificada(nvl_agua_purificada)
        pm  =  generate_pm(pm) #pm +1 if pm <202 else 198
        cloro = random.randint(0,20)
        
        msg = '{"Sensor":"nvl_agua_cruda","Valor":'+str(nvl_agua_cruda)+'}'
        result = client.publish(topic, msg)

        msg = '{"Sensor":"nvl_agua_purificada","Valor":'+str(nvl_agua_purificada)+'}'
        result = client.publish(topic, msg)

        msg = '{"Sensor":"pm","Valor":'+str(pm)+'}'
        result = client.publish(topic, msg)

        msg = '{"Sensor":"cloro","Valor":'+str(cloro)+'}'
        result = client.publish(topic, msg)

        
        



        
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1

def generate_nvl_agua_cruda(nvl_agua_cruda):
    if nvl_agua_cruda is None or nvl_agua_cruda < 200:
        return random.randint(200,2500)
    else:
        return nvl_agua_cruda - random.randint(50,200)
    
def generate_nvl_agua_purificada(nvl_agua_purificada):
    if nvl_agua_purificada is None or nvl_agua_purificada < 200:
        return random.randint(200,2500)
    else:
        return nvl_agua_purificada - random.randint(50,200)

def generate_pm(pm):
    if pm is None or pm > 200 :
        return random.randint(0,10)
    else:
        return pm + random.randint(0,20) 


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()

