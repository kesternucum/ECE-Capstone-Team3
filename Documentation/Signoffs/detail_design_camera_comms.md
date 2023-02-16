# Camera Communications Detail Design

## Function of Subsystems

The camera communications subsystem allows each camera to connect to the university's Wi-Fi network so that the images collected from each camera can be transmitted wirelessly to the remote server for AI image processing.

## Constraints

1. The Avigilon cameras have only Ethernet (RJ45) inputs and therefore require an adapter to connect to the Wi-Fi network, so the chosen adapter must be able to communicate back and forth between Ethernet (RJ45) and Wi-Fi.

2. This device must have the ability to establish a reliable and stable wireless connection to the Wi-Fi network in Bell Hall from its camera position. This device should be able to connect to Wi-Fi at a range of 100 m, which is the distance from Bell Hall to the southeast corner of the parking lot.

 ![Figure 1. Distance Measurement between Cameras and Building](../Images/distanceparkinglot.png)

3. This device must be able to transmit frames at a resolution of 1080p (the resolution of the Avigilon cameras) at a frame rate of 30 fps (the rate of the Avigilon cameras). To stream a YouTube video at a 1080p resolution with a standard frame rate of 30 fps, a bitrate setting of 8 Mbps is recommended [1].

4. The device must have low power consumption capability as the system operates on a solar panel and battery power source. The device should be designed to efficiently use energy to ensure the longevity of the battery and minimize the strain on the solar panels.

# Buildable Schematic

![Wiring diagram for the networking device](../Images/Camera_Comm_wiring.png)

![Figure 2. Camera Communications 3D Schematic](../3D&#32;Models/CameraComm3D.PNG)
<div align="center"> Figure 2. Camera Communication Module 3D Placement Schematic 
<br />
<div align="left">

Note: The Module will be attached to the interior of the casing using a double sided adhesive tape. 

## Analysis

1. Chosen Device:
    * Vonets VAP11G-500[1]
2. Network Capabilities
    * 300Mbps transmission rate
3. Security Protocols
    * WEP(64,128), WPA, WPA-PSK, WPA2, and WPA2-PSK
4. Power
    * Consumes Less than 2W
    * 5V-15V DC
    * DC barrelled power hole or USB power input
5. Range
    * 500m unobstructed, 250m obstructed
6. Inputs
    * RJ45, DC 2.0, USB
7. Dimensions
    * 90mm x 45mm x 15mm

1. This device is an Ethernet to WiFi adapter. This allows for the device to communicate between the network and the cameras.
2. The chosen device is able to reach 250 meters in poor conditions.

3. Using an aggressive estimate to approximate the bandwidth required by the device, using 3 megapixels and 30 frames per second at the highest quality in the calculations, the camera would require only 76.8 Mbps[2], compared to the 300Mbps provided by the adapter, this is well within scope.
4. The setup of this device would be simple, consisting of connecting the ethernet cable to a POE injector that feeds into the camera’s CAT5 RJ45 port directly. To power it, the device can be fed 5V-15V DC to its DC 2.0 power hole. The power consumption of this device is considered “low” by most standards and will be able to be designed for in the power subsystem.
6. Thorough research showed this to be the only device currently on the market that provided the functionality necessary as well as fulfilling all of the requirements of the system.

## Bill of Materials

| Name of Item | Description | Used in which subsystem(s) | Part Number | Manufacturer | Quantity | Unit Price | Total |
| ------------ | ----------- | -------------------------- | ----------- | ------------ | -------- | ---------- | ----- |
| VONETS VAP11G-300 WiFi to Ethernet Converter | WiFi Bridge 2.4GHz WiFi Repeater/Point to Point with RJ45 Male DC/USB Powered for PLC IP Camera Printer Medical Devices Network Device | Primary Data Acquisition | VAP11G-300 | Vonets | 7 | $25.98 | $25.98 |
| | | | | | | | **$181.86** |

## Cited Sources

[1] [https://golightstream.com/what-is-video-bitrate/](https://golightstream.com/what-is-video-bitrate/)

[1] “Vonets VAP11G-500,” _en.vonets.es_, 2023.

[https://www.amazon.com/Vonets-VAP11G-300-Wireless-Multi-Functional-Amplifier/dp/B014SK2H6W/ref=sr_1_1_sspa?crid=WCTZO0AN6W4B&keywords=VONETS+VAP11G-300&qid=1676496048&sprefix=vonets+vap11g-300%2Caps%2C132&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyQlg3NkIwUkhaM0NTJmVuY3J5cHRlZElkPUEwOTk5NDQ1MjI1WThGUTc2UjBWMSZlbmNyeXB0ZWRBZElkPUEwOTk1OTgzMTBHOTdYRlMzSFQwViZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=](https://www.amazon.com/Vonets-VAP11G-300-Wireless-Multi-Functional-Amplifier/dp/B014SK2H6W/ref=sr_1_1_sspa?crid=WCTZO0AN6W4B&keywords=VONETS+VAP11G-300&qid=1676496048&sprefix=vonets+vap11g-300%2Caps%2C132&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyQlg3NkIwUkhaM0NTJmVuY3J5cHRlZElkPUEwOTk5NDQ1MjI1WThGUTc2UjBWMSZlbmNyeXB0ZWRBZElkPUEwOTk1OTgzMTBHOTdYRlMzSFQwViZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=)

[2]”StarDot Technologies Bandwidth and Storage Calculator,” _stardom.com,_ 2023.

[http://stardot.com/bandwidth-and-storage-calculator](http://stardot.com/bandwidth-and-storage-calculator)

# Revisions

2/15/2023 - Reformatted and expanded upon
