# Homebridge에 Homebridge MQTT-Thing 설치

https://github.com/arachnetech/homebridge-mqttthing#readme


# mqtt 설정을 위한 mosquitto 설치

`sudo apt install mosquitto mosquitto-clients`

```shell
pi@raspberrypi:~ $ sudo apt install mosquitto mosquitto-clients
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following package was automatically installed and is no longer required:
  libfuse2
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  libcjson1 libdlt2 libev4 libmosquitto1 libwebsockets16
The following NEW packages will be installed:
  libcjson1 libdlt2 libev4 libmosquitto1 libwebsockets16 mosquitto
  mosquitto-clients
0 upgraded, 7 newly installed, 0 to remove and 97 not upgraded.
Need to get 701 kB of archives.
After this operation, 1,725 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://ftp.kaist.ac.kr/raspbian/raspbian bullseye/main armhf libcjson1 armhf 1.7.14-1 [20.8 kB]
Get:2 http://raspbian.raspberrypi.org/raspbian bullseye/main armhf libdlt2 armhf 2.18.6-1+deb11u1 [45.7 kB]
Get:3 http://ftp.kaist.ac.kr/raspbian/raspbian bullseye/main armhf libev4 armhf 1:4.33-1 [38.2 kB]
Get:4 http://ftp.kaist.ac.kr/raspbian/raspbian bullseye/main armhf libmosquitto1 armhf 2.0.11-1 [83.4 kB]
Get:5 http://ftp.kaist.ac.kr/raspbian/raspbian bullseye/main armhf libwebsockets16 armhf 4.0.20-2 [161 kB]
Get:6 http://ftp.kaist.ac.kr/raspbian/raspbian bullseye/main armhf mosquitto armhf 2.0.11-1 [243 kB]
Get:7 http://ftp.kaist.ac.kr/raspbian/raspbian bullseye/main armhf mosquitto-clients armhf 2.0.11-1 [110 kB]
Fetched 701 kB in 5s (138 kB/s)
Selecting previously unselected package libcjson1:armhf.
(Reading database ... 207423 files and directories currently installed.)
Preparing to unpack .../0-libcjson1_1.7.14-1_armhf.deb ...
Unpacking libcjson1:armhf (1.7.14-1) ...
Selecting previously unselected package libdlt2:armhf.
Preparing to unpack .../1-libdlt2_2.18.6-1+deb11u1_armhf.deb ...
Unpacking libdlt2:armhf (2.18.6-1+deb11u1) ...
Selecting previously unselected package libev4:armhf.
Preparing to unpack .../2-libev4_1%3a4.33-1_armhf.deb ...
Unpacking libev4:armhf (1:4.33-1) ...
Selecting previously unselected package libmosquitto1:armhf.
Preparing to unpack .../3-libmosquitto1_2.0.11-1_armhf.deb ...
Unpacking libmosquitto1:armhf (2.0.11-1) ...
Selecting previously unselected package libwebsockets16:armhf.
Preparing to unpack .../4-libwebsockets16_4.0.20-2_armhf.deb ...
Unpacking libwebsockets16:armhf (4.0.20-2) ...
Selecting previously unselected package mosquitto.
Preparing to unpack .../5-mosquitto_2.0.11-1_armhf.deb ...
Unpacking mosquitto (2.0.11-1) ...
Selecting previously unselected package mosquitto-clients.
Preparing to unpack .../6-mosquitto-clients_2.0.11-1_armhf.deb ...
Unpacking mosquitto-clients (2.0.11-1) ...
Setting up libmosquitto1:armhf (2.0.11-1) ...
Setting up libev4:armhf (1:4.33-1) ...
Setting up libcjson1:armhf (1.7.14-1) ...
Setting up mosquitto-clients (2.0.11-1) ...
Setting up libdlt2:armhf (2.18.6-1+deb11u1) ...
Setting up libwebsockets16:armhf (4.0.20-2) ...
Setting up mosquitto (2.0.11-1) ...
Created symlink /etc/systemd/system/multi-user.target.wants/mosquitto.service → /lib/systemd/system/mosquitto.service.
Processing triggers for man-db (2.9.4-2) ...
Processing triggers for libc-bin (2.31-13+rpt2+rpi1+deb11u4) ...
```


# 재부팅시 자동시작 설정

` sudo systemctl enable mosquitto`

```shell
pi@raspberrypi:~ $ sudo systemctl enable mosquitto
Synchronizing state of mosquitto.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable mosquitto
```


# status 확인

`sudo systemctl status mosquitto`

```shell
pi@raspberrypi:~ $ sudo systemctl status mosquitto
● mosquitto.service - Mosquitto MQTT Broker
     Loaded: loaded (/lib/systemd/system/mosquitto.service; enabled; vendor pre>
     Active: active (running) since Ooo 2022-00-00 00:00:00 BST; -min -s ago
       Docs: man:mosquitto.conf(5)
             man:mosquitto(8)
   Main PID: 20715 (mosquitto)
      Tasks: 1 (limit: 4915)
        CPU: 118ms
     CGroup: /system.slice/mosquitto.service
             └─20715 /usr/sbin/mosquitto -c /etc/mosquitto/mosquitto.conf

Ooo 00 00:00:00 raspberrypi systemd[1]: Starting Mosquitto MQTT Broker...
Ooo 00 00:00:00 raspberrypi systemd[1]: Started Mosquitto MQTT Broker.
```


# id, password 설정

https://chichi-story.tistory.com/34

# mosquitto.conf에 ip, port 설정

```conf
# ip설정
bind_address 192.168.0.15

#mosquitto 접속할 port
port 1883
```

# 기본 시작/재시작 명령어

https://blog.naver.com/kangyunmoon/221500634094

# ew11에 mqtt 세팅

https://m.blog.naver.com/ycj0324/221981721184

# mqtt 수신 확인

`mosquitto_sub -h {ip} -p {port} -t {topic} -u {user} -P {password}`

# 파이썬으로 mqtt 수신하기

```python

# 출처 : https://mishuni.tistory.com/57, https://i5i5.tistory.com/90

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


# 새로운 클라이언트 생성
client = mqtt.Client()

# 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_subscribe(topic 구독),
# on_message(발행된 메세지가 들어왔을 때)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message

# 브로커 연결 설정
url = "{ip}"
port = 1883
username = "{user}"
password = "{password}"

topic = "ew11/recv"
 
# 클라이언트 설정 후 연결 시도
client.username_pw_set(username, password)
client.connect(host=url, port=port)
 
# QoS level 0으로 구독 설정, 정상적으로 subscribe 되면 on_subscribe 호출됨
client.subscribe(topic, 0)

# 루프
client.loop_forever()
```

# 테스트 송신

```python
# 출처 : https://mishuni.tistory.com/57, https://i5i5.tistory.com/90

import paho.mqtt.client as mqtt
import json


def on_connect(client, userdata, flags, rc):
    # 연결이 성공적으로 된다면 완료 메세지 출력
    if rc == 0:
        print("completely connected")
    else:
        print("Bad connection Returned code=", rc)

# 연결이 끊기면 출력
def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)


# 새로운 클라이언트 생성
client = mqtt.Client()

# 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_subscribe(topic 구독),
# on_message(발행된 메세지가 들어왔을 때)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

# 브로커 연결 설정
url = "{ip}"
port = 1883
username = "{user}"
password = "{password}"

topic = "ew11/recv"
 
# 클라이언트 설정 후 연결 시도
client.username_pw_set(username, password)
client.connect(host=url, port=port)
 
 # 메세지 입력
client.loop_start()
client.publish(topic, bytearray.fromhex('aa5530bc00360001000011001a00000000004e0d0d'), 0)   # 보일러 전원 ON 패킷
client.loop_stop()

# 연결 종료
client.disconnect()
```

# if문으로 제어해보기


# 텔레그램 보내기


