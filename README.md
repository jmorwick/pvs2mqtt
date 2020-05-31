# pvs2mqtt

A simple script to access power levels of sunpower inverters. I followed the advice in 
[these notes](https://github.com/deekue/sunpower-pvs-exporter/blob/master/sunpower_pvs_notes.md)
and added a second ethernet connection to a raspberry pi I have processing MQTT for home automation. 
This script simply populates the values accessible from the inverters in to MQTT. I have it running 
on cron in order to provide sensor data to [home assistant](https://www.home-assistant.io/). 
