# MMP8266

MMP8266 is an ESP8266 based small weather station node.
Desiged for hustoj group.

MMP8266是基于ESP8266的小型气象站节点。
为HUSTOJ群友们设计。

## 概述
MMP8266使用ESP-12E模块来处理传感器信息及通信。
使用AM2302、AM2301、DHT11等单总线兼容的设备作为温湿度传感器。

## 主要技术&器件
+ ESP-12E模块，集成业界领先的 Tensilica L106 超低功耗 32 位微型 MCU，带有 16 位精简模式，主频支持 80 MHz 和 160 MHz，支持 RTOS，集成 Wi-Fi MAC/ BB/RF/PA/LNA，板载天线。 该模块支持标准的 IEEE802.11 b/g/n 协议，完整的 TCP/IP 协议栈
+ IP5109 3A充电2.4A放电高集成度移动电源SOC
+ AM2301 高精度单总线数字温湿度传感器
+ MicroPython for esp8266
+ WS2812 RGBLED用于指示设备运行状态
+ 有源蜂鸣器用于指示设备运行状态