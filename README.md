# raspberry_fullstack
Full stack embedded on Raspberry PI: Headless, Embedded Linux, Python, Web Development, Cloud etc.

# Aspects of development
 - Raspberry Pi
 - Operating System (Ubuntu, Headless vs GUI Raspian), installation
 - Back-up and recovery (SD card)
 - Python for GPIOs (Hardware pinouts etc., dht22 sensor)
 - Web Application Stack (raspian, virtual env, nginx, flask, uwsgi, systemd) 
 - Styling (CSS, SQLite3, file management)
 - Core application (functionality, persist measurements, automation)
 - Databases (retruive, querystrings, jquery-presets)
 - Charts and Widgets (google charts, datetime)
 - Timezones (conversions, jquery, arrow)
 - Plotly (debugging)
 - Internet (ip address, web app to internet)

 # Hardware
 - Raspberry PI (3 or 2 or w0 (w0-wifi only))
 - SD card (atleast 8GB)
 - Power adapter (5V, 1.8A)
 - mini-USB cable
 - bread-board
 - dht-22 sensor 
 - push-button, 10k pull-down, LED, current limiting resistor, jumpers etc. 

Useful commands:
1) Copy files from raspberry pi to mac
   scp user@raspberrypi.local:filename.xx .
2) Copy file from mac to raspberry
   scp button.py user@raspberrypi.local:button.py
3) 

Bugs:
1) Unable to ssh: 
   Why? New versions do not have ssh/default user/pwd
  a) Remove known_hosts file 
  b) Flash using Raspberry PI Imager, and custom settings for ssh, user, passwd
  c) ssh using raspberyypi.local
2) 