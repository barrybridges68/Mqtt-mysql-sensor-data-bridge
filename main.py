import paho.mqtt.client as mqtt
import database

broker_url = "192.168.1.236"
broker_port = 1883

client = mqtt.Client()
client.connect(broker_url, broker_port)


ePacketTypeIdent = 0xAA,
ePacketTypeRegistration = 0xAE,
ePacketTypeTemperatureLegacy = 0x14,
ePacketTypeTemperature = 0x20,
ePacketTypeTemperatureHumidity = 0x21,
ePacketTypeTemperatureLight = 0x22,
ePacketTypeTemperatureHumidityLight = 0x23,
ePacketTypeTrigger = 0x24,
#ePacketTypeTriggerInactive = 0x25,
ePacketTypePir = 0x26,
ePacketTypeTemperatureHumidityHdc1080 = 0x26,

def on_connect(client, userdata, flags, rc):
   print("Connected With Result Code: {}".format(rc))

def on_disconnect(client, userdata, rc):
   print("Client Got Disconnected")

def on_message(client, userdata, message):
   print("Message Recieved: "+message.payload.decode())

def create_databases():
    pass

if __name__ == "__main__":
    client.on_connect = on_connect
    client.on_message = on_message
    client.subscribe("home/sensor/", qos=1)
    print("Main")
    client.loop_forever()