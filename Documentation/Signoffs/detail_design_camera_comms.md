# Camera Communications Detail Design

## Big Picture

The camera communications subsystem is a critical component of the camera build and will interact directly with each camera. Its purpose is to allow each camera to connect to the university's Wi-Fi network. The selected cameras have only Ethernet (RJ45) inputs and therefore require an adapter to connect to the Wi-Fi network.


## Requirements

The requirements for this subsystem are derived from shall statements in the conceptual design and the specifications of other subsystems. The key requirements are:
1. The device chosen or designed must be able to communicate back and forth between Ethernet(RJ45) and WiFi.
2. The device chosen or designed must have the ability to establish a reliable and stable wireless connection to the Wi-Fi network in Bell Hall from its camera position. The Wi-Fi connection should have sufficient range and signal strength to allow for uninterrupted transmission of data.
3. The device chosen or designed must be able to communicate live video feed with  the WiFi from Bell Hall. The video feed must be clear and have minimal latency to ensure efficient and effective communication.
4. The device must have low power consumption capability as the system operates on a solar panel and battery power source. The device should be designed to efficiently use energy to ensure the longevity of the battery and minimize the strain on the solar panels.


## Specifications

1. Chosen Device
    * Vonets VAP11G-500[1]
2. Network Capabilities
    * 300Mbps transmission rate
3. Security Protocols
    * WEP(64,128), WPA, WPA-PSK, WPA2, and WPA2-PSK
4. Power
    * Consumes Less than 2W
    * 5V DC
    * DC 2.0 power hole or USB power input
5. Range
    * 500m unobstructed, 250m obstructed
6. Inputs
    * RJ45, DC 2.0, USB
7. Dimensions
    * 90mm x 45mm x 15mm


## Analysis

1. This device is an Ethernet to WiFi adapter. This allows for the device to communicate between the network and the cameras.
2. The range that this device must reach was determined to be 100 meters after liberally measuring the distance from Bell Hall to the corner of the parking lot. The chosen device is able to reach 250 meters in poor conditions.

 ![The distance measurement between cameras and the building](../images/distanceparkinglot.png)

3. Using an aggressive estimate to approximate the bandwidth required by the device, using 3 megapixels and 30 frames per second at the highest quality in the calculations, the camera would require only 76.8 Mbps[2], compared to the 300Mbps provided by the adapter, this is well within scope.
4. The setup of this device would be simple, consisting of connecting the ethernet cable to a POE injector that feeds into the camera’s CAT5 RJ45 port directly. To power it, the device can be fed 5V DC to its DC 2.0 power hole. The power consumption of this device is considered “low” by most standards and will be able to be designed for in the power subsystem.

![The adapter circuit](../images/adaptercircuit.jpg)

5. Thorough research showed this to be the only device currently on the market that provided the functionality necessary as well as fulfilling all of the requirements of the system.


## Cited Sources

[1] “Vonets VAP11G-500,” _en.vonets.es_, 2023.

[http://www.vonets.com/ProductViews.asp?D_ID=83](http://www.vonets.com/ProductViews.asp?D_ID=83)

[2]”StarDot Technologies Bandwidth and Storage Calculator,” _stardom.com,_ 2023.

[http://stardot.com/bandwidth-and-storage-calculator](http://stardot.com/bandwidth-and-storage-calculator)
