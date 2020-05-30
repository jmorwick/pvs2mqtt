import urllib.request, json
import paho.mqtt.client as mqtt

polling_frequency = '1'         # in minutes
#mqqt_url = ''

method = 'http'
host = 'sunpowerconsole.com'
comm_status_command = 'Get_Comm'
device_command = 'DeviceList'

device_url = method + '://' + host + '/cgi-bin/dl_cgi?Command=' + device_command

def get_device_info():
    with urllib.request.urlopen(device_url) as response:
        return json.loads(response.read())
 



#print(get_device_info())
