# Camera Communications Detail Design

## Function of Subsystems

The camera communications subsystem allows each camera to connect to the university's Wi-Fi network so that the images collected from each camera can be transmitted wirelessly to the remote server for AI image processing.

## Constraints

1. The Avigilon cameras have only Ethernet (RJ45) inputs and therefore require an adapter to connect to the Wi-Fi network, so the chosen adapter must be able to communicate back and forth between Ethernet (RJ45) and Wi-Fi.

2. This device must have the ability to establish a reliable and stable wireless connection to the Wi-Fi network in Bell Hall from its camera position. This device should be able to connect to Wi-Fi at a range of 100 m, which is the distance from Bell Hall to the southeast corner of the parking lot.

 ![Figure 1. Distance Measurement between Cameras and Building](../Images/distanceparkinglot.png)

3. This device must be able to transmit frames at a resolution of 1080p (the resolution of the Avigilon cameras) at a frame rate of 30 fps (the rate of the Avigilon cameras). To stream a YouTube video at a 1080p resolution with a standard frame rate of 30 fps, a bitrate setting of 8 Mbps is recommended [1]. Thus, the Ethernet-to-WiFi converter adaptor must be able to transmit data at a rate of at least 8 Mbps.

# Buildable Schematic

![Figure 2. Wiring Diagram for Vonets VAP11G-50 Wi-Fi Bridge/Repeater](../Images/Camera_Comms_Wiring.png)

![Figure 3. Camera Communications 3D Schematic](../3D&#32;Models/CameraComm3DV2.PNG)
<div align="center"> Figure 3. Camera Communication Module 3D Placement Schematic
<br />
<div align="left">

Note: The Module will be attached to the interior of the casing using a double sided adhesive tape.

## Analysis

Selected Adapter: Vonets VAP11G-500S Wi-Fi Bridge/Repeater

1. Ethernet-to-WiFi Adaptor
  - The VAP116-500S Wi-Fi Bridge/Repeater has an ethernet cable that can be connected to the Avigilon cameras (which can either be used for power over ethernet or transmission via ethernet, if no power is available).

2. Network Capabilities
  - The device has a transmission rate of 300 Mbps, which is well above the needed streaming rate of 8 Mbps.

3. Range
  - The ethernet-to-WiFi converter has a unobstructed range of 200 m unobstructed and obstructed of 100 m, which are both well-above the maximum range of 85 m needed to reach routers in Bell Hall.

## Bill of Materials

| Name of Item | Description | Used in which subsystem(s) | Part Number | Manufacturer | Quantity | Unit Price | Total |
| ------------ | ----------- | -------------------------- | ----------- | ------------ | -------- | ---------- | ----- |
| VONETS VAP11G-500S WiFi to Ethernet Converter | WiFi Bridge 2.4GHz WiFi Repeater/Point to Point with RJ45 Male DC/USB Powered for PLC IP Camera Printer Medical Devices Network Device | Primary Data Acquisition | VAP11G-500S | Vonets | 2 | $37.98 | $37.98 |
| | | | | | | | **$75.96** |

Link to Purchase: [Purchase Link](https://www.amazon.com/%E3%80%90Upgraded-VAP11G-500S-Industrial-High-Power-Application/dp/B0B8ND6MQL/ref=asc_df_B0B8ND6MQL/?tag=hyprod-20&linkCode=df0&hvadid=632999243731&hvpos=&hvnetw=g&hvrand=9508670858144407738&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9013670&hvtargid=pla-1892171855661&psc=1)
 
## Cited Sources

[1] [https://golightstream.com/what-is-video-bitrate/](https://golightstream.com/what-is-video-bitrate/)

# Revisions

2/15/2023 - Reformatted and reworked sign off with different Ethernet-to-WiFi adaptor
