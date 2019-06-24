from machine import Pin
from machine import Timer
from dht import DHT22
from simple import MQTTClient
import time

# 初始化外设
# 用户LED灯
led = Pin(16,Pin.OUT)

# AM2302
dht = DHT22(Pin(12))

# 定时器
tim = Timer(-1)

# 定义MQTT服务器
SERVER = 'your mqtt broker address'
PORT = 1883
CLIENTID = 'node1781923'
TOPIC_DOWNLINK = 'node_downlink'
TOPIC_UPLINK_T = 'node_uplink_t'
TOPIC_UPLINK_H = 'node_uplink_h'

# 全局变量
USERNAME = 'your mqtt user'
PSW = 'your mqtt user password'
NEW_DATA_FLAG = False

# 温度测量函数
def temprature_measure(t):
	global NEW_DATA_FLAG
	dht.measure()
	NEW_DATA_FLAG = True
	

def subscribe_callback(topic,msg):
	print("Get MSG <- TOPIC:%s MSG:%s" % (topic,msg))
	if msg == b"on":
		led.off()
	else:
		led.on()
	
def main():
	global NEW_DATA_FLAG
	
	# 初始化定时器
	tim.init(period = 10000, mode = Timer.PERIODIC, callback = temprature_measure)
	# 初始化MQTT客户端
	client = MQTTClient(CLIENTID,SERVER,PORT,USERNAME,PSW)
	client.set_callback(subscribe_callback)
	client.connect()
	client.subscribe(TOPIC_DOWNLINK)
	print("Connected to MQTT server: %s, topic:%s" % (SERVER,TOPIC_DOWNLINK))
	try:
		while True:
			# 主循环
			client.check_msg()
			if NEW_DATA_FLAG:
				led.off()
				msg = "T:%s,H:%s" % (dht.temperature(),dht.humidity())
				tem = "%s"%(dht.temperature())
				humi = "%s"%(dht.humidity())
				client.publish(TOPIC_UPLINK_T,tem)
				client.publish(TOPIC_UPLINK_H,humi)
				print("Send MSG: -> TOPIC:%s MSG:%s"%("REMIX_TOPIC",msg))
				NEW_DATA_FLAG = False
				led.on()
			time.sleep_ms(100)
	finally:
		client.disconnect()
