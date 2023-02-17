# Primary Data Acquisition Power Detail Design

## Big Picture

The primary data acquisition will use cameras designed for power over ethernet. Due to the monitoring system being outdoors and away from buildings, the cameras can’t be powered by traditional means of ethernet cables. Therefore, a “wireless” solution will have to be developed in order to ensure that the cameras can have a reliable and hands-off way to remain powered.

## Specifications

Hardware Constraints

1. Avigilon Cameras
    * Power Consumption
        * 6 W with external power (10 W for -IR option)
        * 6 W with IEEE 802.3af Class 3 PoE (10 W for -IR option)
    * Input Voltage
        * 12 VDC +/- 10%, 6 W min (10 W min with -IR option)
        * 24 VAC +/- 10%, 8 VA min (12 VA min with -IR option)
    * Power Supply Connection
        * Power over Ethernet - IEEE 802.3af Class 3 compliant
        * 2-pin terminal block
2. WiFi Module [2]
    * Power Consumption
        * Less than 2 W
    * Input Voltage
        * 5-15 VDC
    * Power Supply Connection
        * 2.1mm plug
        * USB
3. Arduino Nano 33 BLE Sense [3]
    * Operating Voltage
        * 3.3 V
    * Input Voltage Limit
        * 21 V
    * Power Supply Connection
        * USB, Vin & GND pin

Reliability Constraints

1. Should keep all devices powered during operational hours (8:00am - 4:30pm)
2. Should not interfere with operations of the primary data acquisition system
3. Should require minimal maintenance once installed
4. Weather should not impact power to the devices

## Buildable Schematic



## Analysis

Meeting Hardware Requirements

1. It has worked in our favor that all devices that need to be powered can run off a 12 volt power source. Therefore, a Howell Energy 12 volt 7 amp-hour rechargeable battery [4] has been selected. The battery is lightweight, compact, and provides the needed 12 volts to all devices [4].
2. There are a few connection options for some of the devices and the following will be done for each device. The WiFi module only has a 2.1mm plug or USB power option, and in this case it has been decided to use a converter buck module which takes a 12v positive and negative wire input and steps it down to a 5v output [7]. For the Arduino, the Vin and GND input will be used for reuse of some wiring resources used for a different design [8] to maintain cost-effectiveness and connected by crimping. Lastly, the 2-pin terminal for the camera will be connected to the battery, as the ethernet port will be used by the WiFi module making it unavailable for power.

Meeting Reliability Requirements

1. In order to make sure that the system will require little maintenance power-wise, the battery chosen is rechargeable, and the easiest method of recharging will be done via solar power given there are no nearby outlets. Therefore, the 12 volt solar panel made by Dakota Lithium has been selected. The panel is compatible with 12 volt 7 amp-hour batteries, weatherproof, and can fully charge the battery in under 9 hours (about a day's worth of sunlight) [5]. It also does not require a charge controller [5], so a connection to the battery via crimping should be sufficient to get it working. 
2. Replacement of the solar panel is also not a major concern, as most solar panels do not begin until about 10 years into its lifespan [6] and Dakota Lithium’s solar panel in particular has an 11 year warranty [5]. The Howell Energy battery only has a three-year warranty [4], but given that the project serves as a proof of concept, and the lower price of this battery, this will be accepted. Longer lasting batteries will be a consideration for future iterations of the project.
3. Protection of the battery and Arduino will be handled in the casing subsystem design.

## Bill of Materials

| Name of Item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
|Rechargeable Battery| 12V 7Ah Battery, HWE Energy Rechargeable LiFePO4 Battery, 4000+ Deep Cycle Lithium Iron Phosphate Battery Built-in BMS | Primary Data Acquisition | Number Not Found | Howell Energy | 7 | $34.56 | $241.92 |
|Solar Panel| 12V FLEXIBLE SOLAR PANEL – 20 WATTS | Primary Data Acquisition | Number Not Found | Dakota Lithium | 7 | $49.00 | $343.00 |
|USB Power Adapter| DGZZI DC Converter Buck Module 12V to USB 5V 3A DC-DC Converter Step Down Adapter | Primary Data Acquisition | Number Not Found | DGZZI | 7 | $10.59 | $74.13 |
| Total | | | | Total Components | 21 | Total Cost | $659.05 |

## Revisions

**02/16/2023**

Revised and added to the constraints section.

Added new valid buildable schematic.

Rewrote analysis section.

Added items to the Bill of Materials.

## Cited Sources

[1] “2.0 Megapixel Day/Night H.264 HD Indoor Dome Camera,” _AVIGILON_, 2013.  https://www.securityinformed.com/datasheets/avigilon-2-0-h3-d1-ip-dome-camera/co-3126-ga/2.0-H3-DdatasheetEN2.pdf.

[2] “VAP11G-500,” _Vonets_, 2023. http://www.vonets.com/ProductViews.asp?D_ID=83.

[3] “Arduino Nano 33 BLE Sense,” _arduino.cc_, 2023. https://store-usa.arduino.cc/products/arduino-nano-33-ble-sense.

[4] “12V 7Ah Battery, HWE Energy Rechargeable LiFePO4 Battery, 4000+ Deep Cycle Lithium Iron Phosphate Battery Built-in BMS, Perfect for Fish Finder, Alarm System, Small UPS, Solar, Ride on Toys,” _amazon.com_, 2023. https://www.amazon.com/Battery-HWE-Energy-Rechargeable-Phosphate/dp/B0B4R1PJK9/ref=asc_df_B0B4R1PJK9/.

[5] “12V FLEXIBLE SOLAR PANEL - 20 WATTS,” _Dakota Lithium_, 2023. https://dakotalithium.com/product/12v-solar-panel/.

[6] Sendy, Andrew, “How long do solar panels actually last?” _SolarReviews_, 14 Jan 2022.  https://www.solarreviews.com/blog/how-long-do-solar-panels-last.

[7] “DGZZI DC Converter Buck Module 12V to USB 5V 3A DC-DC Converter Step Down Adapter for Car,” _amazon.com_, 2023. https://www.amazon.com/DGZZI-Converter-Module-DC-DC-Adapter/dp/B086DF7646/ref=asc_df_B086DF7646/. 

[8] Laboy, Gabriel, “Secondary Data Acquisition & Sign Power Detail Design,” _GitHub_, 11 Feb 2023. https://github.com/kesternucum/ECE-Capstone-Team3/blob/Gabe-SDA-And-Sign-Power-Signoff/Documentation/Signoffs/SDA_And_Sign_Power_Detail_Design.md.
