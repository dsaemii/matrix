# Matrix
![matrix](https://user-images.githubusercontent.com/46267818/177481366-83a75efc-1184-45a5-a867-d1c735c4d0b6.png)

## Goal
The visualization of the **PV production** (PV Produktion), the **grid** (Netzbezug) **and battery supply** (Batteriebezug), and the **battery status** (Batteriezustand). At the same time, we want to use these values to control power consumers such as the pool heating or the legionella program more intelligently.

## How it works
The data comes directly from the PV Power Converter through an [IP Symcon module](https://community.symcon.de/t/modul-jotkpp-solar-wechselrichter-kostal-plenticore-plus-piko-iq/50857). Using the MQTT protocol, we then provide this data from IP Symcon as an MQTT server to the MQTT client, our Raspberry Pi, which controls the RGB LED matrix. With IP Symcon we also control consume excess PV energy, like the Legionella Program Boiler or the pool heating.
