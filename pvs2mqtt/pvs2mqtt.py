import urllib.request, json
import paho.mqtt.publish as mqtt

# mqtt config
mqtt_host = 'localhost'
mqtt_port = 1883
mqtt_topic = 'pvs2mqtt'

# pvs config
method = 'http'
host = 'sunpowerconsole.com'
comm_status_command = 'Get_Comm'
device_command = 'DeviceList'

device_url = method + '://' + host + '/cgi-bin/dl_cgi?Command=' + device_command

def get_device_info():
    with urllib.request.urlopen(device_url) as response:
        return json.loads(response.read())
 
def export_pvs_device_status():
    info = get_device_info()
    messages = []
    for device in info['devices']:      # categorize devices by type / serial number
        device_type = device['DEVICE_TYPE']
        serial = device['SERIAL']
        for key in device.keys():       # update topic for each field in device status
            messages.append({'topic': mqtt_topic+'/'+device_type+'/'+serial+'/'+key,
                             'payload': device[key],
                             'qos': 0,
                             'retain': True})
    # publish messages
    mqtt.multiple(messages, hostname=mqtt_host, port=mqtt_port)


if __name__ == "__main__":              # update mqtt with pvs values
    export_pvs_device_status()
