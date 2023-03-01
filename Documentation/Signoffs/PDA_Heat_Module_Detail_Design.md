# Primary Data Acquisition Heat Module Detail Design

## Big Picture

The primary data acquisition will use cameras designed for indoor use, but in an outdoor setting. Therefore, a few more additional constraints must be addressed in order to ensure the cameras don’t malfunction during operation. This document addresses temperature control of the cameras to ensure the camera’s specified operation temperature is not exceeded.

## Specifications

Existing Hardware Constraints

1. Avigilon Cameras [1]
    * Operating Temperature: -10 °C to +50 °C (14 °F to 122 °F)

Reliability Constraints

1. Any device installed should last long enough to not require frequent replacement
2. Installed devices should not interfere with camera vision and operation
3. The temperature control element should only operate when the appropriate environmental temperature has been reached

## Buildable Schematic

<img width="711" alt="Heat_Module_Connections" src="https://user-images.githubusercontent.com/80428236/220764233-ebf7f7dd-a200-4a18-8d08-23d50f3e80be.png">

Figure 1. Hardware Electrical Connections

## Analysis

Environmental Temperatures

1. The average range of temperature within Cookeville for the year usually goes between 28 °F to 88 °F with it rarely going lower than 12 °F and higher than 94 °F [2]. The lowest and highest temperature ever recorded in Cookeville are -22 °F and 105 °F, respectively [3]. This means there is no concern for cooling the cameras given it has a max operating temperature of 122 °F, but they must be warmed up in the winter due to the minimum operating temperature of 14 °F [1].

Collecting Temperature Data

1. In order to get the current temperature, it has been decided to get information via a local weather station in Cookeville, TN. The server subsystem will get the temperature and send it to an Arduino Nano 33 IoT. This Arduino is capable of connecting to WiFi [4], so it should be able to receive information from the server once connected. The Arduino is also small (45 x 18 mm) and lightweight (5 g) [4], so it should not occupy a significant amount of space within the primary data acquisition system casing.

Heating the Environment

1. To heat the environment around the camera, it has been decided to go with a film heating plate. The films can reach temperatures of up to 80 °C (176 °F) [6] which should be plenty of heat to keep the surrounding environment of the camera warm. They are also small (30 x 40 mm) and lightweight (0.634 oz), and feature an adhesive side [6] which should make attachment to the casing of the primary data acquisition system simple.

Powering the Heating Element

1. To make sure that the heater plate only provides heat when needed, there will be a connection made between one of the Arduino digital pins and the heat plate mediated by a transistor. The transistor will act as a switch allowing power to be delivered to the heat plate from the power supply as seen in Figure 1 of the buildable schematic section. The Arduino will be programmed to source voltage to the transistor from its digital pin when a cold enough is read and keep sourcing voltage to the transistor for one minute before shutting off the digital pin. After a two minute delay, the Arduino will check the temperature again and repeat the powering process if needed.
2. The chosen transistor is an N-MOS transistor with the needed features to be compatible with both the Arduino and power supply.
    * A VDSS of 55 V and 47 A [8] which is far above the 5 V and 200 mA requirement to power the heat plate [6].
    * A VGS(th) of 1 V [8] which should meet the constraint of the 1.8-3.3 V output of the Arduino digital pin [5].

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

**02/28/2023**

Updated big picture to more accurately reflect intent of design.

Updated constraints to more accurately reflect intent of design.

Updated analysis to make it more readable and added electrical analysis.

## Cited Sources

[1] “2.0 Megapixel Day/Night H.264 HD Indoor Dome Camera,” _AVIGILON_, 2013.  https://www.securityinformed.com/datasheets/avigilon-2-0-h3-d1-ip-dome-camera/co-3126-ga/2.0-H3-DdatasheetEN2.pdf.

[2] “Climate and Average Weather Year Round in Cookeville,” _Weather Spark_, 2023. https://weatherspark.com/y/15151/Average-Weather-in-Cookeville-Tennessee-United-States-Year-Round.

[3] “Cookeville Weather Records,” _Extreme Weather Watch_, 2022. https://www.extremeweatherwatch.com/cities/cookeville.

[4] “Arduino Nano 33 IoT,” _Arduino Store_, 2023. https://store-usa.arduino.cc/products/arduino-nano-33-iot.

[5] “V[oltage on digital output pins depending on voltage source?](https://forum.arduino.cc/t/voltage-on-digital-output-pins-depending-on-voltage-source/686526),” _Arduino Forum_, Dec 2020. https://forum.arduino.cc/t/voltage-on-digital-output-pins-depending-on-voltage-source/686526/2.

[6] “4 PCS Film Heater Plate Adhesive Pad, Icstation PI Heating Elements Film 5V 1W Flexible Polymerize Heater Film Stripboard Mat 30mmx40mm,” _amazon.com_, 2023. https://www.amazon.com/5V-Flexible-Polyimide-Heater-Plate/dp/B0727X2DGC/.

[7] “IRLZ44NPBF,” _Digi-Key_, 2023. https://www.digikey.com/en/products/detail/infineon-technologies/IRLZ44NPBF/811808.

[8] “IRLZ44NPbF,” _International Rectifier_, 11 Nov 2003. https://www.infineon.com/dgdl/irlz44npbf.pdf?fileId=5546d462533600a40153567217c32725.
