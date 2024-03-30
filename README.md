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
 9) Restore a backup
    9.1) Check location of sdcard (mac): diskutil list
    9.2) Format SD Card: sudo newfs_msdos -F 16 /dev/disk3
    9.3) Restoration: sudo dd if=***filename**.dmg of=/dev/disk3 (10k seconds)
    9.4) Confirm config.txt settings using raspberry config
    9.5) Eject and reinsert to raspberry Pi
    9.6) Connect as root: ssh root@ip 
    9.7) If you can boot, restoration of back-up image worked
 10) Raspberry GPIO, Python using CLI
    10.1) Plug sd card into raspberry pi
    10.2) Using Python v3: python --version, python3 --version
    10.3) CLI: python3 -> can execute commands
    10.4) function: def str_operation(strn): -> remember for three spaces indent
    10.5) install vim: 'Esc', : -> sudo apt-get install vim
    10.6) create py: vim example.py -> sys.argv[1], int(sys.argv[2]) 
    10.7) Wire the circuit: LED, Switch to GPIOs
    10.8) Install pip: sudo apt-get install python3-pip
    10.9) Install rpi.gpio: pip3 install rpi_gpio
    10.11) Set GPIO
            import RPi.GPIO as GPIO
            pin = 7
            GPIO.setmode(GPIO.BOARD) # GPIO.BCM
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH) ->HIGH
    10.12) Read a button, similiar to GPIO, except it is an input
            GPIO.cleanup() to clean up
            polling -> while(True) with some delay time.sleep(0.1)
            import time, RPi.GPIO as GPIO
    10.13) Control LED with the button
   11) Install git
      11.1) Install git: sudo apt-get install git-core
      11.2) config: git config --global user.email reddyp4@gmail.com
      11.3) config: git config --global user.name reddyp4
      11.4) clone: ADAfruit_Python from adafruit
      11.5) setup packages: sudo python3 setup.py install 
   12) Install DHT22 sensor
      12.1) Sensor: python3 AdafruitDHT.py 2303 17 -> #sensorDHT22-2302 gpio#15
      12.2) SEE: cat adafruit.py 
            import sys modules
            read: Adafruit_DHT.read_retry(sensor,pin)
            calibration table 
   13) Web Application Stack 
      13.0) app -> framework -> appl server -> web server -> webbrowser -> user
            framework: debian, stretch lite
            framework: flask
            app server: uWSGI
            web server: nginx 
            web browser: url
            order of installation doesnt matter
      13.1) Python virtual environment needed for individual modules
            System python: modules/packages
            App1->mod/pkg1, app2->mod/pkg2
            Individual modules can have individual modules/packages
      13.1) Essential packages: sudo apt-get install build-essential
      13.2) sudo apt-get install libncurses5-dev libncursesw5-dev libreadline6-dev
      13.3) sudo apt-get install libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libsqlite3-dev libgdbm-dev tk8.5-dev
      13.4) if didnt get, sudo-apt-get update
      13.5) python dev tools: sudo apt-get install python-dev 
      13.6) pip for flask: sudo apt-get install libssl-dev openssl
      13.7) download, compile: 
         1_ mkdir python-source
         2_ in this folder-> wget https://... .tgz
         3_ python3 --version -> update
         4_ tar zxvf Python***.tgz
         5_ cd Python***
         6_ ./configure --prefix=/usr/local/opt/python-3.6.4
         7_ make -> compilation
            Look for "Python build finished successfully"
         8_ Install new version: sudo make install 
         9_ check new version .../usr/local.opt/../python3.6 --version
         10_ use full path
         11_ Take a backup of setup
   14) Setup Infra for Web Application 
      14.1) Python VM: sudo su
      14.2) cd _var -> mkdir www (for web applications)
      14.3) inside www -> mkdir lab_app
      14.4) inside lap_app -> /usr/local/opt/python-3.6.4/bin/python3.6 -m venv .
            venv module -> virtual environment 
      14.5) activate python -> . bin/activate -> new python virtual env
   15) Install NGINX
      15.1) Go to lap_app -> .bin/activate
      15.2) apt-get install nginx -> may be apt-get update
      15.3) Check -> https://192.168.111.36 -> Welcome to nginx
   16) Install Flask ->
      16.1) pip install flask
      16.2) Create tiny appl using vim 
         from flask import Flask
         app = Flask(__name__)
         @app.route("/")
         -> add function hell()
         -> initializer: if __name__ == "__main__"
         -> send data to port 8080: app.run(host='0.0.0.0',port=8080)
         why 0.0.0.0? 
      16.3) Exeute hello.py
      16.4) go to https://ip:8080-> app info sent to web-browser
      16.5) Now to Flask application
            vim hello.py
            flask notes: flask.pocoo.org
            default: flask run -> default=5000
            apply host 0.0.0.0 -> flask run --host=0.0.0.0 --port=1234
   17) uWSGI application - between flask and nginx (to web)
      17.1) to .bin/activate
      17.2) pip install uwsgi 
      17.3) Config: cat /..nginx../default 
      17.4) rm /etc/nginx/sites-enabled/default
      17.5) vim lab_app_nginx.conf  ->
            server {
               listen 80;
               server_name localhost;
               charset utf-8;
               client_max_body_size 75M;

               #static files
               location /static {
                  root /var/www/lab_app/;
               }
               #
               location / {try_these $uri @labapp;} 
               location @labapp {
                  include uwsgi_params;
                  uwsgi_pass unix:/var/www/lab_app.lab_app_uwsgi.sock;
               }
            }
      17.6) symbolic link: ln -s /var/www.,,, nginx.conf /etc/nginx/conf.d/
      17.7) restart nginx /etc/init.d/nginx restart
      17.8) config: bim lab_app_swsgi.ini
            [uwsgi]
            #application 's base folder
            base = /var/www/lab_app

            #python's module to import
            app = hello 
            module = %(app)

            home= %(base)
            pythonpath = %(base)

            #socket files location
            socket = /var/www/lab_app/%n.sock   #need to match nginx socket file

            #permissions for the socket file
            ch-socket = 666

            #variable that folds a floask application inside the module imported # at line #6
            callable = app 

            #location of log files
            logto = /var/log/uwsgi/%n.log #log file for debugging
      17.9) folder for logs: mkdir /var/log/uwsgi
      17.10) Testing: start manually
            /bin/uwsgi --ini /var/www/lab_app/lab_app_uwsgi.ini
            go to webrower: no need of port
            Now UWSGI Flask application comes into nginx
      17.11) Take a back-up
      17.12) auto-start uwsgi for restarting:
            systemd -> system process manager in Linux
            1_ vim /etc/systemd/system/emperor.uwsgi.service
            [unit]
            [Service]   #ini file to start
            [Install]
            freedesktop.org
            2_ start emperor.uwsgi.service
            3_ status emperor.uwsgi.service
            4_ restart not starting systemd doesnt know yet
            5_ systemctl enable emperor.uwsgi.service
            6_ Reboot Raspberry PI -> check 192.168.11.36
            reboot -> sudo reboot
   18) Install SQLite3
      18.1) root: sudo su
      18.2) run: sqlite3 sample.sql
            1_ begin;
            2_ create table temperatures (rDatetime datetime, sensorID text, temp numeric);
            3_ insert into temperatures values (datetime(' now'),"1",25.10);
            4_ commit;
            5_ select * from temperatures; -> should see the record
            6_ .exit
      18.3) Documentation: sqlite.org
   19) CSS for Styling, static assets (non-executable code)
      19.1) Static -> skeleton.css
      Next Boilerplate cascading sheet: 
      19.2) in lab_app: mkdir css, mkdir images
      19.3) vim a_static_file.html -> get the html
      <html>, <head>, <title>, <body>
      19.4) Access: http://192.168.11.36/static/a_static_file.html
      19.5) Boiler plate css -> getskeleton.com -> copy css files
      19.6) sftp to copy (or filezilla): copy from host to Raspberry PI
            SFTP = ssh file transfer protocol 
      19.7) Update the new file -> insert links to css files
            1_ <!--> ...
      19.8) Now to flask templates: mkdir templates
      19.9) vim hello.py -> modify to add templates
      19.10) restart uwsgi service -> systemctl restart emperor.uwsgi.service
            Check the webpage
      19.11) Debugging the flask application -> debugging is on -> log file?
            venv -> .bin/activate
            -> run application -> get error on console if ssh or webbrowser
            -> not defined
            -> vim check to line -> :9 -> navigate to line
            -> restart systemctl restart emperor.uwsgi.service
      19.12) Debugging info at uwsgi.log
            tail -n 100 /var/log/uwsgi/lab_app_uwsgi.log -> last 100 lines
   20) DHT Library -> access data from flask app -> show in browser
      20.1) 