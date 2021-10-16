import paho.mqtt.client as mqtt    #import client library

broker_address = "192.168.137.21" # ip adress given by mobile hotspot
qos = 2
MQTT_PATH = "test"
MQTT_PATH_2 = "test/test2"
FAILING_PATH = "failing"

LIST_PATH = [MQTT_PATH,MQTT_PATH_2,FAILING_PATH]
failing_message = "server failed"

username = "CW2B2"
password = "KULeuven"
MQTT_SUCCES = 0

connection_params = {
    0 : "Connection successful",
    1: "Connection refused - incorrect protocol version",
    2: "Connection refused - invalid client identifie",
    3: "Connection refused - server unavailable",
    4: "Connection refused - bad username or password" ,
    5: "Connection refused - not authorised 6-255: Currently unused.",
    'Min_delay': 5,
    'Max_delay': 80
}


def evaluate_connection(rc,connection_params):

    if rc == 0:
        print(connection_params[rc])
    else:
        print("system error confirmed, given by library mqtt server:")
        print(connection_params[rc])
        assert False

    pass
def on_subscribe(client,userdata,mid,granted_qos):
    if len(granted_qos) == len(LIST_PATH):
        print("all subscription confirmed")
    else:
        number_missing_subscription = str(len(LIST_PATH) - len(granted_qos))
        print("missing" + number_missing_subscription + "subscriptions")

        main()
def on_disconnect(client,userdata,msg):
    if msg == MQTT_SUCCES:
        print("Shutting down confirmed")
    else:
        print("starting reconnecting protocol")
        print("Min_delay:" + str(userdata['Min_delay']) + " seconds")
        print("Max_delay:" + str(userdata['Max_delay']) + " seconds")
        print("Delay is doubled between subsequent reconnections ")
def on_connect(client, userdata, flags, rc):

    evaluate_connection(rc,userdata)

    client.subscribe([(MQTT_PATH,qos),(MQTT_PATH_2,qos),(FAILING_PATH,0)])

def on_message_PATH_2(client,userdata,msg):

    print(msg.topic + " " + str(msg.payload))

def on_message_PATH(client,userdata,msg):

    print(msg.topic + " " + str(msg.payload))

def main():

    client = mqtt.Client("recieving_data")             #create new instance
    client.on_connect=on_connect  #bind call back function
    client.on_disconnect = on_disconnect
    client.on_subscribe=on_subscribe
    client.username_pw_set(username,password=password)
    client.will_set(FAILING_PATH,payload = failing_message)
    client.reconnect_delay_set(min_delay=connection_params['Min_delay'],max_delay=connection_params['Max_delay'])
    client.user_data_set(connection_params)

    client.connect(broker_address)               #connect to broker

    client.message_callback_add(MQTT_PATH,on_message_PATH)
    client.message_callback_add(MQTT_PATH_2,on_message_PATH_2)

    client.loop_forever()

if __name__ == '__main__':

    main()
# use this line if you don't want to write any further code. It blocks the code forever to check for data
# client.loop_start()
# #use this line if you want to write any more code here


"""
def on_message(client, userdata, msg):
    if msg.topic == "test":
        print("test:")
        print(msg.topic+" "+str(msg.payload))
    if msg.topic == "test2":
        print("test2:")
        print(msg.topic + " " + str(msg.payload))
    # more callbacks, etc
"""