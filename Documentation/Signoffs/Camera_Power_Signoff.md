# Primary Data Acquisition Power Detail Design

## Big Picture

The primary data acquisition subsystem will utilize a number of different electrical components in order to ensure the cameras can transfer images over to the server. Given its high elevation on the outdoor posts, there will be no simple way to wire the subsystem to a grounded power source. Therefore, a “wireless” solution will have to be developed in order to ensure that the subsystem can have a reliable and hands-off way to remain powered, and this design goes over the implementation.

## Specifications

Hardware Specifications

1. Avigilon Cameras [1]
    * Input Voltage - 12 VDC +/- 10%
    * Input Power - 6 W (min) 
    * Power Supply Connections - Power over Ethernet (IEEE 802.3af Class 3), 2-pin terminal block
2. WiFi Module [2]
    * Input Voltage - 5-24 VDC
    * Current Draw - 2 A
    * Power Supply Connections - USB, barrel plug, DC connector
3. Arduino Nano 33 IoT [3]
    * Input Voltage - 3.3-21 V 
    * Current Draw - 85 mA [4]
    * Power Supply Connections - USB, Vin & GND pin
4. Heater Plate [5]
    * Input Voltage - 5 V
    * Input Power - 1 W
    * Power Supply Connection - Positive and Negative wire

Electrical Constraints

1. The power supply must meet the voltage/current needs for all devices requiring power
2. Devices drawing current from the power supply must be protected from overcurrent
3. Devices receiving power must use the correct adapters to connect to the power supply
4. The power supply must be rechargeable to minimize maintenance

Reliability Constraints

1. The power supply must not take up much space

## Buildable Schematic

![PDA_Wiring_Schematic](https://user-images.githubusercontent.com/80428236/219553780-1b5e38c1-d0f1-47f3-a0a0-48e2fc9916c7.png)

Figure 1. Electrical Wiring Schematic

## Analysis

Electrical Constraint Analysis

1. All devices requiring power can accept a 12 volt input and summed together has about a  maximum current draw of about 2.8 amps. Therefore, a 12 volt, 7 amp-hour LiFePO4 rechargeable battery made by Howell Energy [6] has been selected since it provides both the needed voltage and current.
2. The camera and communication module have a functional dependency on each other since they work together to send images to the server, and the heater plate and Arduino have a similar functional dependency since it determines when to allow power to go to the heater plate based on the weather read from the server. Therefore, a 3.5 amp fuse [7] and a 1 amp fuse [8] will be connected between the battery and respective devices to protect from overcurrent.
3. Each device requires a different method of connection to power, so each selected adapter will be analyzed separately.
    * The camera will not have PoE available as the selected communication module will be connected to the camera’s ethernet port to be able to connect to the server. Therefore, the 2-pin terminal block on the camera will be connected to power, and crimping will be used to secure the connection since it is wiring.
    * The communication module specifically requires 5 volts input, so to prevent issues with voltage conversion causing changes in current, the barrel plug will be connected to instead since it accepts a wide range of voltage (including the battery’s output of 12 volts). The device comes with a barrel plug to 2-pin block adapter [2], so it will be wired to the power supply via crimping.
    * The Arduino USB port is designed specifically for connection to laptops [3], so to prevent potential issues of powering with an adapter, the Vin and GND pins will be used. Therefore, connection via crimping will be used to secure a connection between the Arduino and power supply.
    * The heater plate only has a positive and negative wire leading out of the device, so it will be crimped together to the power supply.
4. The LiFePO4 battery requires a 14.6 volt, 0.7-3.5 amp (recommended) input to be charged [6]. Therefore, a combination of a solar panel and charge controller will be used since there are not many commercially available 14.6 volt solar panels.
    * The selected solar panel is a 24 volt, 60 watt panel made by Newpowa [10]. The current output produced is 2.5 amps which is within the recommended current range needed to charge the battery.
    * The charge controller is a maximum power point tracker (MPPT) DC-to-DC converter made by Powerwerx [11]. The controller can convert a 16-25 volt input to 14.6 volt and is rated for up to 150 watts [11], so it can handle the input from the solar panel and create the needed output to the battery.

Reliability Constraint Analysis

1. The battery’s dimensions are 5.94 x 2.56 x 3.7 in and weighs 1.8 lbs [6], and the charge controller’s dimensions are 4 x 4 x 2 in with a weight of 0.3 lbs [11]. These are  considered small and lightweight enough according to the ME team designing the protective casing for the camera and other devices.
    * The solar panel is not a device that needs to be protected from the weather as it is rated for outdoor use [10] and is not planned to be put inside the protective casing, so its size is irrelevant.

Important Notes

1. A diagram of how all devices will be connected together is shown in Figure 1.
2. Protection of all devices against weather will be handled by the ME team on the project.
3. The BoM does not accurately reflect what will be purchased, but instead how much the system would need given the original outline of the project. 

## Bill of Materials

| Name of Item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
|Rechargeable Battery| 12V 7Ah Battery, HWE Energy Rechargeable LiFePO4 Battery, Built-in BMS | Primary Data Acquisition | N/A | Howell Energy | 7 | $34.56 | $241.92 |
|Solar Panel| 60W 24V Monocrystalline Solar Panel | Primary Data Acquisition | N/A | Newpowa | 7 | $75.99 | $531.93 |
|Charge Controller| MPPT-150-14.6, DC-to-DC Solar Charger Controller | Primary Data Acquisition | N/A | Powerwerx | 7 | $41.99 | $293.93 |
|3.5A Fuse| Pack of 5-3.5A Glass Fuse (GMA), 250v, 5mm x 20mm (3/16" X 3/4") Fast Blow | Primary Data Acquisition | N/A | Techman | 3 | $6.99 | $20.97 |
|1A Fuse| 5x20mm 1A 250V Fast-Blow Glass Fuses (Pack of 20 Pcs) | Primary Data Acquisition | N/A | Techman | 1 | $5.99 | $5.99 |
|Fuse Cartridge| FUSE HLDR CARTRIDGE 250V 5A PCB | Primary Data Acquisition | 4268 | Keystone Electronics | 14 | $0.73 | $10.22 |
| Total | | | | Total Components | 39 | Total Cost | $1,104.96 |

## Cited Sources

[1] “2.0 Megapixel Day/Night H.264 HD Indoor Dome Camera,” _AVIGILON_, 2013.  https://www.securityinformed.com/datasheets/avigilon-2-0-h3-d1-ip-dome-camera/co-3126-ga/2.0-H3-DdatasheetEN2.pdf.

[2] “【Upgraded Version】 VONETS VAP11G-500S Industrial High-Power 2.4GHz WiFi Bridge/Wireless Router/Ethernet WiFi to Ethernet Adapter for Industrial Application, PLC, Printer, Medical, Network Devices,” _amazon.com_, 2023. https://www.amazon.com/%E3%80%90Upgraded-VAP11G-500S-Industrial-High-Power-Application/dp/B0B8ND6MQL.

[3] “Arduino Nano 33 IoT,” _arduino.cc_, 2023. https://store-usa.arduino.cc/products/arduino-nano-33-iot.

[4] “[Nano 33 IOT power consumption > 22mA in sleep](https://forum.arduino.cc/t/nano-33-iot-power-consumption-22ma-in-sleep/1014574),” _Arduino Forum_, Jul 2022. https://forum.arduino.cc/t/nano-33-iot-power-consumption-22ma-in-sleep/1014574.

[5] “4 PCS Film Heater Plate Adhesive Pad, Icstation PI Heating Elements Film 5V 1W Flexible Polymerize Heater Film Stripboard Mat 30mmx40mm,” _amazon.com_, 2023. https://www.amazon.com/5V-Flexible-Polyimide-Heater-Plate/dp/B0727X2DGC/.

[6] “12V 7Ah Battery, HWE Energy Rechargeable LiFePO4 Battery, 4000+ Deep Cycle Lithium Iron Phosphate Battery Built-in BMS, Perfect for Fish Finder, Alarm System, Small UPS, Solar, Ride on Toys,” _amazon.com_, 2023. https://www.amazon.com/Battery-HWE-Energy-Rechargeable-Phosphate/dp/B0B4R1PJK9/.

[7] “Pack of 5-3.5A Glass Fuse (GMA), 250v, 5mm x 20mm (3/16" X 3/4") Fast Blow (Fast Acting),” _amazon.com_, 2023.  https://www.amazon.com/Pack-5-3-5A-Glass-Fuse-Acting/dp/B074HH3VZ7/.

[8] “BOJACK 5x20mm 1A 1amp 250V 0.2 x 0.78 Inch F1AL250V Fast-Blow Glass Fuses(Pack of 20 Pcs),” _amazon.com_, 2023. https://www.amazon.com/BOJACK-5x20mm-F1AL250V-Fast-Blow-Glass/dp/B07S96VTJR/.

[9] “4268,” _Digi-Key_, 2023. https://www.digikey.com/en/products/detail/keystone-electronics/4628/2137316.

[10] “Newpowa 9BB 60W(Watt) Solar Panel High-Efficiency Monocrystalline 24V PV Module Designed for 24V Off Grid System, Charge Your 24V Battery of RV, Boat, Camper, Trailer, Gate Opener (60W New),” _amazon.com_, 2023. https://www.amazon.com/Newpowa-High-Efficiency-Monocrystalline-Designed-Battery/dp/B09W22RQGK/.

[11] “Powerwerx MPPT-150-14.6, DC-to-DC Solar Charger Controller for Bioenno 12V LiFePO4 Batteries,” _amazon.com_, 2023. https://www.amazon.com/Powerwerx-MPPT-150-14-6-Charger-Controller-Batteries/dp/B087ZSY8CR.

## Revisions

**02/16/2023**

Revised and added to the constraints section.

Added new valid buildable schematic.

Rewrote analysis section.

Added items to the Bill of Materials.

**03/07/2023**

Updated Big Picture section to better reflect the purpose of detail design.

Revised the constraints sections to better reflect what needs to be analyzed.

Updated buildable schematic to reflect changes in components.

Updated Analysis section to be more concise.

Updated Bill of Materials.

Revised references.
