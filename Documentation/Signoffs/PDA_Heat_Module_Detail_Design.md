# Primary Data Acquisition Heat Module Detail Design

## Big Picture

The primary data acquisition will use cameras designed for indoor use, but in an outdoor setting. Therefore, a few more additional constraints must be addressed in order to ensure the cameras can operate properly and don’t run into hardware issues. This document addresses temperature control of the cameras to ensure they don’t go below their specified operation temperature.

## Specifications

Existing Hardware Constraints

1. Avigilon Cameras [1]
    * Operating Temperature: -10 °C to +50 °C (14 °F to 122 °F)

Reliability Constraints

1. Any device installed should last long enough to not require frequent replacement
2. The heating module should only power on when it’s cold enough
3. Should not interfere with camera vision and operation

## Buildable Schematic

![Heat_Module_Wiring](https://user-images.githubusercontent.com/80428236/219547418-005a2b73-7603-46de-b484-d2eaae911cac.png)

Figure 1. Electrical Wiring Schematic

## Analysis

Meeting Hardware Constraints

1. The average range of temperature within Cookeville for the year usually goes between 28 °F to 88 °F with it rarely going lower than 12 °F and higher than 94 °F [2]. The lowest and highest temperature ever recorded in Cookeville are -22 °F and 105 °F, respectively [3]. This means that while there is no concern for cooling the cameras in the high range temperatures of the summer, making sure the device stays warm during potential lows in the winter is a must.
2. In order to make sure the cameras stay warm, it has been decided to go with film heater plates. These films are extremely small (under 2 square inches), require little energy (about 1 watt of power at 5 volts), and get up to 80 °C (176 °F) which should be plenty of heat to keep the surrounding environment of the camera warm [5]. The plates also feature an adhesive side, which alongside its flexibility and light weight, should make attachment to the system casing simple [5].

Meeting Reliability Requirements

1. In order to make sure that the heat plates go on when needed, they will be connected to a transistor and microcontroller system that can communicate to the server. The selected Arduino Nano 33 IoT which has WiFi capability and digital output pins [4] and a simple nMOS transistor [6] connected between the Arduino and power source will allow for the heat plate to be turned on and off when needed. Connections between the devices are shown in Figure 1.
2. The server will get information from a local weather station, and when the weather station reads a temperature of 0 °C (32 °F), a bit will be sent to the Arduino indicating that the transistor should be switched on to allow for power to be sent to the heat plate. After 60 seconds, or the bit from the server reads false, the heat plate will be turned off. In the even that the 60 second time expires and the bit still reads true, the program will wait 3 minutes until turning the heat plate on again to prevent the heat plate from being on for an excessive amount of time and causing subsystem damage given how it can hit a temperature of up to 80 °C (176 °F) [5].
3. The arduino is also a small device (45mm x 18mm) [4], so fitting the arduino along with the heat plate shouldn’t be a complicated task. How the arduino and heat plate will be fitted, though, will be handled in the casing subsystem design.

Addressing Risks

1. Condensation is a major concern given that the heating element will get very hot and operate around freezing temperatures. Proper ventilation of the primary data acquisition casing, though, will be handled by the ME team.
2. Protection of the arduino and heating plate from the weather will be handled in the casing subsystem design.

Important Notes

1. The BoM does not accurately reflect what will be purchased, but instead how much the system would need given the original outline of the project.

## Bill of Materials

| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
|Arduino Nano| Arduino Nano 33 IoT | Primary Data Acquisition | ABX00027 | Arduino | 7 | $24.00 | $168.00 |
|Transistor| MOSFET N-CH 55V 47A | Primary Data Acquisition | IRLZ44NPBF-ND | Infineon Technologies | 7 | $1.52 | $10.64 |
|Film Heater Plate| 5V 1W Flexible Polymerize Heater Film Stripboard Mat 30mmx40mm | Primary Data Acquisition | Number Not Found | Icstation | 2 | $15.99 | $31.98 |
| Total | | | | Total Components | 16 | Total Cost | $210.62 |

## Cited Sources

[1] “2.0 Megapixel Day/Night H.264 HD Indoor Dome Camera,” _AVIGILON_, 2013.  https://www.securityinformed.com/datasheets/avigilon-2-0-h3-d1-ip-dome-camera/co-3126-ga/2.0-H3-DdatasheetEN2.pdf.

[2] “Climate and Average Weather Year Round in Cookeville,” _Weather Spark_, 2023. https://weatherspark.com/y/15151/Average-Weather-in-Cookeville-Tennessee-United-States-Year-Round.

[3] “Cookeville Weather Records,” _Extreme Weather Watch_, 2022. https://www.extremeweatherwatch.com/cities/cookeville.

[4] “Arduino Nano 33 IoT,” _arduino.cc_, 2023. https://store-usa.arduino.cc/products/arduino-nano-33-iot.

[5] “4 PCS Film Heater Plate Adhesive Pad, Icstation PI Heating Elements Film 5V 1W Flexible Polymerize Heater Film Stripboard Mat 30mmx40mm,” _amazon.com_, 2023. https://www.amazon.com/5V-Flexible-Polyimide-Heater-Plate/dp/B0727X2DGC/.

[6] “IRLZ44NPBF,” _Digi-Key_, 2023. https://www.digikey.com/en/products/detail/infineon-technologies/IRLZ44NPBF/811808.

## Revisions

**02/11/2023**

Updated constraints requirement.

Removed invalid buildable schematic.

Changed method of temperature detection.

Created a Bill of Materials.

**02/20/2023**

Updated analysis to detail how the subsystem will get weather status.

Updated analysis to address being able to power the heat module.

Changed device used to communicate to server and power on heating element.

Update Bill of Materials.
