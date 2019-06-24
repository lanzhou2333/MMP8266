#boot文件，配置网络

def network_config():
	print("Init network...")
	import network
	SSID = 'your ssid'
	PSW = 'your wifi password'
	sta = network.WLAN(network.STA_IF)
	ap = network.WLAN(network.AP_IF)
	if ap.active():
		#如果AP模式打开，则关闭AP模式
		ap.active(False)
	if sta.isconnected():
		print('Connecting...')
	sta.active(True)
	sta.connect(SSID,PSW) #连接到WIFI
	while not sta.isconnected():
		pass
	print('Connected!')
	print(sta.ifconfig())
	
network_config()
gc.collect()
	