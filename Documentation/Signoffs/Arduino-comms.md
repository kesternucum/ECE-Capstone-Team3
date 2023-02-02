# ESP8266 Arduino Shield for WiFi Communication

## Big Picture

The Arduino devices controlling the signs and pressure tube sensors need to be able to connect to WiFi to interact with the server. Arduino devices do not natively have WiFi capabilities and so an outside device needs to be selected in order to allow this communication.

## Requirements
The requirements for this device are:
1. The shield must be able to communicate between the Arduinos and the WiFi network.
2. The shield must be able to establish a reliable and stable wireless connection to the university's WiFi network.
3. The shield must support the proper level of communication for each device, meaning that low levels of data need to be transmitted over the course of a minute. The network consumption of both the pressure tubes and the sign will need no more than 1 kps. Each device will only be receiving a few simple instruction packets (up to about 50 bytes a piece) and the pressure sensors will be sending out a few packets for an integer count.
4. The shield must have low power consumption to efficiently use energy obtained from the batteries charged by the solar panels.
5. The shield must be easily compatible with the Arduino.

## Specifications

1. Shield Type
    * ESP8266 Arduino Shield[1]
2. Network Capabilities
    * Supports 802.11 b/g/n
    * 2.4GHz
    * 9600 bps transmission rate due to the Arduino’s default baud rate. The ESP8266 itself is capable of transmission rates of 115200bps.
3. Security Protocols
    * Supports WEP, WPA/WPA2 PSK/Enterprise
4. Power
    * 3.0-3.6V DC
    * Consumes about 0.3W on average
5. Inputs
    * Supports UART, GPIO, ADC, PWM, I2C, SPI
6. Range
    *100m indoor, 150m outdoor

## Analysis

1. The ESP8266 Arduino shield provides the necessary interface for connecting an Arduino board to the university's WiFi network. The device’s main functionality is WiFi connectivity.
2. The range of the device was determined to be sufficient for the intended use. In typical indoor conditions, the range is estimated to be 100m and in outdoor conditions, it can reach 150m. The necessary range is estimated to be no more than 91 meters.

 ![The distance measurement between the corner of the parking lot and the building.](../Images/distanceparkinglot.png)

3.The shield supports multiple security protocols to ensure a secure connection to the university's WiFi network.
4. The shield’s 9600bps transmission rate allows it to fulfill the 1000 bps transmission rate requirement easily.
5.The shield consumes low power, making it an efficient solution for powering the communication interface.
6. The shield provides multiple inputs, including UART, GPIO, ADC, PWM, I2C, and SPI, which can be used to connect various peripherals to the Arduino board.
7. The device was chosen because it fulfills all of the aforementioned requirements as well as being very cheap ($7.50 a piece on sparkfun.)

## Cited Sources

[1] “ESP8266 WiFi Module ,” sparkfun.com, 2023.
[https://cdn.sparkfun.com/assets/f/e/5/6/f/ESP8266ModuleV2.pdf](https://cdn.sparkfun.com/assets/f/e/5/6/f/ESP8266ModuleV2.pdf)

