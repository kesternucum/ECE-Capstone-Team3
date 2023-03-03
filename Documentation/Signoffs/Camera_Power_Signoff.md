# Primary Data Acquisition Power Detail Design

## Big Picture

The primary data acquisition subsystem will utilize a number of different electrical components in order to ensure the cameras can transfer images over to the server. Given its high elevation location on the outdoor posts, there will be no easily feasible way to wire the subsystem to a grounded power source. Therefore, a “wireless” solution will have to be developed in order to ensure that the cameras can have a reliable and hands-off way to remain powered, along with any other needed devices to ensure the system remains operational.

## Specifications

Hardware Constraints

1. Avigilon Cameras [1]
    * Input Voltage - 12 VDC +/- 10%
    * Input Power - 6 W min 
    * Power Supply Connection - Power over Ethernet (IEEE 802.3af Class 3), 2-pin terminal block
2. WiFi Module [2]
    * Input Voltage - 5 VDC (Max 24 VDC)
    * Current Draw - 2 A
    * Power Supply Connection - USB, 2.1mm plug
3. Arduino Nano 33 IoT [3]
    * Input Voltage - 3.3 V (Max 21 V)
    * Current Draw - 85 mA [4]
    * Power Supply Connection - USB, Vin & GND pin
4. Heater Plate [5]
    * Input Voltage - 5 V
    * Input Power - 1 W
    * Power Supply Connection - Positive and Negative wire

Reliability Constraints

1. Should keep all devices powered during operational hours (8:00am - 4:30pm)
2. Should not interfere with operations of the primary data acquisition system
3. Power source should be rechargeable to minimize maintenance

## Buildable Schematic

![PDA_Wiring_Schematic](https://user-images.githubusercontent.com/80428236/219553780-1b5e38c1-d0f1-47f3-a0a0-48e2fc9916c7.png)

Figure 1. Electrical Wiring Schematic

## Analysis

Selecting the Power Source

1. It serves to the convenience of this subsystem that all devices that need to be powered can accept or require 12 V to operate (as seen in the constraints section). Therefore, it has been decided to go with a 12 V 7 Ah LiFePO4 battery produced by Howell Energy [6]. These batteries do not occupy much space (5.94 x 2.56 x 3.7 in) and last much longer than their sealed lead-acid counterpart, as well as being capable of being recharged [6]. 

Recharging the Power Source

1. The only feasible solution for recharging the battery given its location is by using a solar panel. Therefore, a 30 W 24 V solar panel made by Newpowa [7] has been selected. The solar panel will be used in tandem with a charger controller designed to take in 16-25 V and convert it to a 12-14.6 V output [9], and is also rated to handle up to 150 W so there should be no compatibility issues. The charge controller is also designed in mind for charging LiFePO4 batteries [9], so it should function well with the Howell battery.

Connecting the Devices

1. Cameras
    * Given that the wifi module for this subsystem will take the ethernet port located on the camera, the 2-pin terminal block will have to be used. Therefore, wire will just be crimped between the camera and battery with an intermediary 750 mA fuse [12] in order to protect it in the case of overcurrent.
2. Wifi Module
    * It has already been decided in the communication subsystem for primary data acquisition that the USB power supply will remain connected. Given that the USB connection looks for a 5 V input [2], it has been decided to use a step down converter from 12 V to 5 V which can handle a maximum current of 3 A [10]. This should be compatible given the wifi module will draw a maximum of 2 A [2], and it will be protected with 2.5 A fuse [13] to prevent overcurrent.
3. Arduino Nano
    * Given that the Arduino board only allows the option of using the Vin and GND pins for an external power source [3], wire from the battery to the Arduino pins will be used to connect to power. To protect the Arduino from overcurrent, 250 mA fuses [11] will be connected between the Arduino and battery.
4. Heat Plate
    * The heat plate only has a positive and negative wire, so it will be connected via crimping to the battery. In order to protect from overcurrent, 250 mA fuses [11] will be used.

Distributing Power

1. The camera, wifi module, Arduino, and heat plate draw roughly 500 mA, 2 A, 85 mA, and 200 mA, respectively, as seen in the constraints. Summed up, this equals 2.785 A of current drawn which is far less than the max 7 A outputted by the Howell battery [6], so there is no concern about making sure all devices get sufficient power.

Important Notes

1. High level wiring connections are shown in figure 1.
2. Protection of all devices against weather will be handled by the ME team on the project.
3. The BoM does not accurately reflect what will be purchased, but instead how much the system would need given the original outline of the project. 

## Bill of Materials

| Name of Item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
|Rechargeable Battery| 12V 7Ah Battery, HWE Energy Rechargeable LiFePO4 Battery, Built-in BMS | Primary Data Acquisition | N/A | Howell Energy | 7 | $34.56 | $241.92 |
|Solar Panel| 30W 24V Monocrystalline Solar Panel | Primary Data Acquisition | N/A | Newpowa | 7 | $46.99 | $328.93 |
|USB Power Adapter| DGZZI DC Converter Buck Module 12V to USB 5V 3A DC-DC Converter Step Down Adapter | Primary Data Acquisition | N/A | DGZZI | 7 | $10.59 | $74.13 |
|250mA Fuse| Pack of 5-250mA (0.25A) Glass Fuse (GMA), 250v, 5mm x 20mm (3/16" X 3/4") Fast Blow | Primary Data Acquisition | N/A | Techman | 14 | $6.49 | $90.86 |
|750mA Fuse| Pack of 5-750mA (0.75A) Glass Fuse (GDC), 250v, 5mm x 20mm (3/16" X 3/4") Slow Blow | Primary Data Acquisition | N/A | Techman | 7 | $5.99 | $41.93 |
|2.5A Fuse| Pack of 5-2.5A Glass Fuse (GMA), 250v, 5mm x 20mm (3/16" X 3/4") Fast Blow (Fast Acting) | Primary Data Acquisition | N/A | Techman | 7 | $6.79 | $47.53 |
|Fuse Cartridge| FUSE HLDR CARTRIDGE 250V 5A PCB | Primary Data Acquisition | 4268 | Keystone Electronics | 28 | $0.73 | $20.44 |
| Total | | | | Total Components | 77 | Total Cost | $845.74 |

## Cited Sources

[1] “2.0 Megapixel Day/Night H.264 HD Indoor Dome Camera,” _AVIGILON_, 2013.  https://www.securityinformed.com/datasheets/avigilon-2-0-h3-d1-ip-dome-camera/co-3126-ga/2.0-H3-DdatasheetEN2.pdf.

[2] “【Upgraded Version】 VONETS VAP11G-500S Industrial High-Power 2.4GHz WiFi Bridge/Wireless Router/Ethernet WiFi to Ethernet Adapter for Industrial Application, PLC, Printer, Medical, Network Devices,” _amazon.com_, 2023. https://www.amazon.com/%E3%80%90Upgraded-VAP11G-500S-Industrial-High-Power-Application/dp/B0B8ND6MQL.

[3] “Arduino Nano 33 IoT,” _arduino.cc_, 2023. https://store-usa.arduino.cc/products/arduino-nano-33-iot.

[4] “[Nano 33 IOT power consumption > 22mA in sleep](https://forum.arduino.cc/t/nano-33-iot-power-consumption-22ma-in-sleep/1014574),” _Arduino Forum_, Jul 2022. https://forum.arduino.cc/t/nano-33-iot-power-consumption-22ma-in-sleep/1014574.

[5] “4 PCS Film Heater Plate Adhesive Pad, Icstation PI Heating Elements Film 5V 1W Flexible Polymerize Heater Film Stripboard Mat 30mmx40mm,” _amazon.com_, 2023. https://www.amazon.com/5V-Flexible-Polyimide-Heater-Plate/dp/B0727X2DGC/.

[6] “12V 7Ah Battery, HWE Energy Rechargeable LiFePO4 Battery, 4000+ Deep Cycle Lithium Iron Phosphate Battery Built-in BMS, Perfect for Fish Finder, Alarm System, Small UPS, Solar, Ride on Toys,” _amazon.com_, 2023. https://www.amazon.com/Battery-HWE-Energy-Rechargeable-Phosphate/dp/B0B4R1PJK9/.

[7] “30W 24V Monocrystalline Solar Panel,” _Newpowa_, 2023. https://www.newpowa.com/30w-24v-monocrystalline-solar-panel/.

[8] Sendy, Andrew, “How long do solar panels actually last?” _SolarReviews_, 14 Jan 2022.  https://www.solarreviews.com/blog/how-long-do-solar-panels-last.

[9] “Powerwerx MPPT-150-14.6, DC-to-DC Solar Charger Controller for Bioenno 12V LiFePO4 Batteries,” _amazon.com_, 2023. https://www.amazon.com/Powerwerx-MPPT-150-14-6-Charger-Controller-Batteries/dp/B087ZSY8CR.

[10] “DGZZI DC Converter Buck Module 12V to USB 5V 3A DC-DC Converter Step Down Adapter for Car,” _amazon.com_, 2023. https://www.amazon.com/DGZZI-Converter-Module-DC-DC-Adapter/dp/B086DF7646. 

[11] “Pack of 5-250mA (0.25A) Glass Fuse (GMA), 250v, 5mm x 20mm (3/16" X 3/4") Fast Blow (Fast Acting),” _amazon.com_, 2023.  https://www.amazon.com/Pack-250mA-0-25A-Glass-Acting/dp/B074LB1CWC/ref=asc_df_B074LB1CWC/.

[12] “Pack of 5-750mA (0.75A) Glass Fuse (GDC), 250v, 5mm x 20mm (3/16" X 3/4") Slow Blow (Time Delay),” _amazon.com_, 2023. https://www.amazon.com/Pack-5-750mA-0-75A-Glass-Delay/dp/B074L9P4JM/ref=asc_df_B074L9P4JM/.

[13] “Pack of 5-2.5A Glass Fuse (GMA), 250v, 5mm x 20mm (3/16" X 3/4") Fast Blow (Fast Acting),” _amazon.com_, 2023. https://www.amazon.com/Pack-5-2-5A-Glass-Fuse-Acting/dp/B074HFG2P6/.

[14] “4268,” _Digi-Key_, 2023. https://www.digikey.com/en/products/detail/keystone-electronics/4628/2137316.

## Revisions

**02/16/2023**

Revised and added to the constraints section.

Added new valid buildable schematic.

Rewrote analysis section.

Added items to the Bill of Materials.

**03/03/2023**

Updated Big Picture section to better reflect the purpose of detail design.

Revised the constraints sections for readability.

Reorganized analysis section for readability and included electrical analysis.

Updated Bill of Materials.

Added more references.
