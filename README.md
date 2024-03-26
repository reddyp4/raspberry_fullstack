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

# Headless vs GUI
 - Less space vs Larger OS space (graphics)
 - Best for server/remote vs. desktop
 - More reliable (less to break) vs. acceptable
 - Memory bound vs. RAM share with video
 - command line vs. point and click
 - no monitor/mouse/keyboard vs. added hardware components

 #Steps
 1) Copy Raspbian onto SD Card
 2) Copy ssh and wifi configuration to sd card
 3) Boot Raspberry from the SD card
 4) InET finds raspberry connected to PC
 5) ssh pi$ip (182.168.x.x from iNet)
 6) Configure "sudo raspi-config"
    6.1) Passwd, network options, network names, wifi
    6.2) Rename raspberry Pi
    6.3) Choose overclock preset
    6.4) Expand file system (reconfigure SD card )
    6.5) Memory split (decrease memory to GPU - no monitor)
    6.6) Reboot
 7) Root user
    7.1) Enable "root" as user - by default root is blocked via ssh
        7.1.1) nano /etc/ssh/sshd_config for configuration changes
        7.1.2) "PermitRootLogin" to yes
        7.1.3) /etc/init.d/ssh restart
        7.1.4) set passwd for root <passwd root>
        7.1.5) Test, exit pi, and do ssh root@ip, with new passwd
    7.2) Make a new user
 8) Setup backup
    8.1) Logon as a user
    8.2) reboot: sudo shutdown -h now (green LED off)
    8.3) Pop sd card, and connect to pc. 
    8.4) Copy backup: sudo dd if=/dev/disk3 of=~/rpi_backup/RaspbianStretchLite_fresh_install_25Mar24.dmg 
    8.5) Can take time - may 30+minutes
 9) 