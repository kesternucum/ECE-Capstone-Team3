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
2. In order to make sure the cameras stay warm, it has been decided to go with film heater plates. These films are extremely small (under 2 square inches), require little energy (about 1 watt of power at 5 volts), and get up to 80 °C (176 °F) which should be plenty of heat to keep the surrounding environment of the camera warm [7]. The plates also feature an adhesive side, which alongside its flexibility and light weight, should make attachment to the system casing simple [7].

Meeting Reliability Requirements

1. In order to make sure that the heat plates go on when needed, they will be connected to an Arduino Nano 33 BLE Sense model. This Arduino features an on-board temperature sensor [4] capable of reading a temperature range of  -10 °C to +120 °C (-40 °F to +248 °F) [5]. The Arduino will be programmed to read the temperature when it hits a low enough temperature (for now a target of 0 °C (32 °F)), and then will power on the heat plate using its 5 volt output pin [4]. To prevent the heat plate from staying on too long, the Arduino will stop supplying power once it detects an environment temperature of 5 °C (41 °F).
2. The arduino is also a small device (45mm x 18mm), so fitting the arduino along with the heat plate shouldn’t be a complicated task. How the arduino and heat plate will be fitted, though, will be handled in the casing subsystem design.

Addressing Risks

1. Utilization of the heating plates comes with a few drawbacks. The first being that the heat plate can reach temperatures up to 80 °C (176 °F). While it is expected to heat the environment around the cameras rather quickly, if the heat plate reaches this temperature it serves as a risk to damaging all other components in the primary data acquisition system if not located in an appropriate area. This issue will have to be addressed in the casing design for the system to ensure the heat plate is placed in a safe location.
2. The other issue is the risk of condensation. Given that this module is only supposed to operate when the temperature is around freezing, applying that much heat in a short amount of time could lead to heavy condensation of the camera lens or other parts of the casing. Excessive condensation could also lead to part damage via moisture. While good practice is to make sure the system casing is well ventilated (as this will also be needed to prevent condensation in the spring and summer months), this will be considered an acceptable risk.
3. Protection of the arduino and heating plate from the weather will be handled in the casing subsystem design.

## Bill of Materials

| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
|Arduino Nano| Arduino Nano 33 BLE Sense | Primary Data Acquisition | ABX00031 | Arduino | 7 | $40.50 | $283.50 |
|Film Heater Plate| 4 PCS Film Heater Plate Adhesive Pad, Icstation PI Heating Elements Film 5V 1W Flexible Polymerize Heater Film Stripboard Mat 30mmx40mm | Primary Data Acquisition | Number Not Found | Icstation | 2 | $15.99 | $31.98 |
| Total | | | | Total Components | 9 | Total Cost | $315.48 |

## Cited Sources

[1] “2.0 Megapixel Day/Night H.264 HD Indoor Dome Camera,” _AVIGILON_, 2013.  https://www.securityinformed.com/datasheets/avigilon-2-0-h3-d1-ip-dome-camera/co-3126-ga/2.0-H3-DdatasheetEN2.pdf.

[2] “Climate and Average Weather Year Round in Cookeville,” _Weather Spark_, 2023. https://weatherspark.com/y/15151/Average-Weather-in-Cookeville-Tennessee-United-States-Year-Round.

[3] “Cookeville Weather Records,” _Extreme Weather Watch_, 2022. https://www.extremeweatherwatch.com/cities/cookeville.

[4] “Arduino Nano 33 BLE Sense,” _arduino.cc_, 2023. https://store-usa.arduino.cc/products/arduino-nano-33-ble-sense.

[5] “HTS221,” _arduino.cc_, Aug 2016. https://content.arduino.cc/assets/Nano_BLE_Sense_HTS221.pdf. 

[6] Garcia, Jose, “Reading Temperature & Humidity on Nano 33 BLE Sense,” _arduino.cc_, 2023. https://docs.arduino.cc/tutorials/nano-33-ble-sense/humidity-and-temperature-sensor.

[7] “4 PCS Film Heater Plate Adhesive Pad, Icstation PI Heating Elements Film 5V 1W Flexible Polymerize Heater Film Stripboard Mat 30mmx40mm,” _amazon.com_, 2023. https://www.amazon.com/5V-Flexible-Polyimide-Heater-Plate/dp/B0727X2DGC/.

## Revisions

**02/11/2023**

Updated constraints requirement.

Removed invalid buildable schematic.

Changed method of temperature detection.

Created a Bill of Materials.
