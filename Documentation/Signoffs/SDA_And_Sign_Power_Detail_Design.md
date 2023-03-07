# Secondary Data Acquisition & Sign Power Detail Design

## Big Picture

The Secondary Data Acquisition subsystem and the Sign subsystem have a number of design details in common including location of the power supply and input voltage needs. Therefore, it has been decided to have both systems operating under one source of power. This design covers the streamlined design of powering both of the aforementioned subsystems, as well as how the power supply and all relevant connected devices will be protected.

## Constraints

Hardware Specifications

1. Arduino Mega 2560 Rev3 [1]
    * Input Voltage (recommended) - 7-12 V
    * Current Draw - 73.19 mA @ 9 V [2]
    * Power Supply Connections - USB, 2.1mm center-positive plug, Vin & GND pin
    * Dimensions - 101.52 x 53.3 mm  (L x W)
2. LED Light Strips [3]
    * Input Voltage - 12 V
    * Current Draw - 700 mA
    * Power Supply Connection - Positive & Negative wire
3. IRLZ44NPBF (Transistor) [4]
    * Dimensions - 3.3 x 3.3 x 1.6 mm  (L x W x H)
4. Arduino Uno Rev3 [5]
    * Input Voltage (recommended) - 7-12 V
    * Current Draw - 98.43 mA @ 9 V [6]
    * Power Supply Connections - USB, 2.1mm center-positive plug, Vin & GND pin
    * Dimensions - 68.6 x 53.4 mm  (L x W)
5. Differential Pressure Sensor [7]
    * Dimensions - 29.85 x 11.05 x 29.34 mm (L x W x H)
6. WiFi Module [8]
    * Dimensions - 25.4 x 24.8 mm (L x W)

Placement Constraints

1. The power source must be in a location that does not interfere with university parking
2. The power source must be located within close proximity of the pneumatic tubes
3. The power source must be located within close proximity of the sign

Electrical Constraints

1. The power supply must meet the voltage/current needs for all devices requiring power
2. Devices drawing current from the power supply must be protected from overcurrent
3. Devices receiving power must use the correct adapters to connect to the power supply
4. The power supply must be rechargeable to minimize maintenance
5. The power supply must not take up much space

Reliability Constraints

1. All electrical components must be protected from bad weather (e.g. windy, rainy, snowy)

## Buildable Schematics

<img width="474" alt="image" src="https://user-images.githubusercontent.com/80428236/219544087-3666c724-eb90-476f-9c66-4056ddcab685.png">

Figure 1. Wiring Schematic Without Sign

![Arduino_Wiring_With_Sign_Schematic](https://user-images.githubusercontent.com/80428236/219543255-b8a8db36-60c3-46c1-867e-7cf3528142ec.png)

Figure 2. Wiring Schematic With Sign

![Post_Model](https://user-images.githubusercontent.com/80428236/219543298-e8a7edb6-a43f-4d11-9a07-de3856bceb66.png)

Figure 3. Post Model

![Post_Side_Model](https://user-images.githubusercontent.com/80428236/219543316-c5561a02-4226-4d40-8b0a-a6c3202c7a98.png)

Figure 4. Post Side View

![Post_Front_Model](https://user-images.githubusercontent.com/80428236/219543334-61d1f62a-2539-4eb8-9c46-672756a36deb.png)

Figure 5. Post Front View

![Post_Back_Model](https://user-images.githubusercontent.com/80428236/219543340-2048f3db-c25c-4541-9b26-5bff8f9fe251.png)

Figure 6. Post Back View

## Analysis

Placement Constraint Analysis

1. In order to stay close to the pneumatic tubes, solar panel posts will be placed in the locations referenced in Figure 7. These spots are on the grass, so it should not interfere with the ability to park or lot visibility.
2. The sign will be attached to the post itself (denoted as the yellow square in Figure 7) given the post is a tall enough height to make the sign easily visible to people coming in from the south-side parking lot entrance.
3. The selected post is a 5 ft powder-coated steel post made by Blue Hawk [9]. It provides the needed height to see the sign, and was approved by the Facilities department to be installed at the chosen locations.

![Post_Placement](https://user-images.githubusercontent.com/80428236/219543389-bb18b5e1-8dec-4e8c-9cc5-fdf84bdf782e.jpg)

Figure 7. Post Placement

Electrical Constraint Analysis

1. All devices requiring power can accept a 12 volt input and summed together has about a  maximum current draw of 9.9 amps. Therefore, a 12 volt, 12 amp-hour LiFePO4 rechargeable battery made by Howell Energy [10] has been selected since it provides both the needed voltage and current.
2. To protect the devices from overcurrent, a 12.5 amp fuse [11] will be connected between the battery and devices.
    * The posts only powering pneumatic tubes is a different case since it only needs to power the Arduino Uno, so a 250 milliamp fuse [12] will be connected between the device and battery instead.
3. To avoid complications with maintaining permanent wire connections to the Arduino Vin and GND pins, a 2.1 mm center-positive plug made by Tensility [15] will be used to connect the battery to the Arduino. The plug has a positive and negative wire leading out of it which will be crimped to wires going to the battery, and the plug itself is rated for a maximum of 48 volts and 8.5 amps [16] so it should function properly given the Arduino’s power needs.
    * The LED strips only have a positive and negative wire leading out of the device, so there will be no special adapter used and connection to the battery will be done via crimping.
4. The LiFePO4 battery requires a 14.6 volt, 12 amp (max) input to be charged [10]. Therefore, a combination of a solar panel and charge controller will be used since there are not many commercially available 14.6 volt solar panels.
    * The selected solar panel is a 18 volt, 150 watt panel made by Dokio [13]. The current output produced is 8.33 amps which exceeds the minimum 6 amps needed to charge the battery [10].
    * The charge controller is a maximum power point tracker (MPPT) DC-to-DC converter made by Powerwerx [14]. The controller can convert a 16-25 volt input to 14.6 volt and is rated for up to 150 watts [14], so it can handle the input from the solar panel and create the needed output to the battery.
5. The battery’s dimensions are 5.94 x 3.86 x 3.86 in and weighs 3.13 lbs [10], and the charge controller’s dimensions are 4 x 4 x 2 in with a weight of 0.3 lbs [14]. These are reasonably small and lightweight given that they must be mounted up with the post, so they are not expected to cause any mounting issues.
    * The solar panel is not a device that needs to be protected from the weather as it is rated for outdoor use [13] and is not planned to be put inside the protective casing, so its size is irrelevant.

Reliability Constraint Analysis

1. All electrical components requiring protection, combined, will take up roughly 383.82 x 244.4 x 179.08 mm (15.11 x 9.62 x 7.05 in) of space (calculated using the Arduino Mega since it is larger than the Uno). To account for additional space to wire components together, changes in device orientation, and not having a snug fit, the minimum size necessary to fit all components into one space has been rounded up to 406.4 x 254 x 180 mm (or 16 x 10 x 7.08 in). Therefore,  a QILIPSU 410 x 310 x 180 mm junction box [21] has been chosen since it provides the calculated space. The box is IP67 rated [21], so it will be able to sustain any inclement weather [22]. It can also easily be drilled into given it’s made mostly of plastic [21], so wires can be pulled outside the box to connect to the solar panel and pneumatic tubes. IP68 locknuts [23] will be inserted into the drilled holes to ensure case integrity is held.

Important Notes

1. Connections between all devices are shown in Figure 1.
2. The high level setup of the post with the solar panel and pack protecting electrical devices are shown in Figures 2 through 5.
3. The BoM does not accurately reflect what will be purchased, but instead how much the system would need given the original outline of the project. 

## Bill of Materials

| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
|Solar Panel| 150 Watt 18 Volt Monocrystalline Solar Panel High | Secondary Data Acquisition & Sign | N/A | Dokio | 3 | $155.00 | $465.00 |
|Rechargeable Battery| 12V 12Ah Battery, HWE Energy Rechargeable LiFePO4 Battery, Built-in BMS | Secondary Data Acquisition & Sign | N/A | Howell Energy | 3 | $54.99 | $164.97 |
|Steel Post| Powder-coated Steel U-post | Secondary Data Acquisition & Sign | 493053 | Blue Hawk | 3 | $7.98 | $23.94 |
|22 AWG Wire| 22 AWG Wire Size, PVC, Stranded, 100 ft Lg, Red | Secondary Data Acquisition & Sign | 34GC76 |Grainger | 1 | $9.93 | $9.93 |
|22 AWG Wire| 22 AWG Wire Size, PVC, Stranded, 100 ft Lg, Black | Secondary Data Acquisition & Sign | 34GC72 |Grainger | 1 | $10.61 | $10.61 |
|Crimp Kit| CHENBO 620pcs 2.54mm/0.1" Connectors Wire Jumper Cable Pin Header Connector Housing Assortment Kit | Secondary Data Acquisition & Sign | CQ00824 | Chenbo | 1 | $10.99 | $10.99 |
|250 mA Fuse| Pack of 5-250mA (0.25A) Glass Fuse (GMA), 250v, 5mm x 20mm (3/16" X 3/4") Fast Blow | Secondary Data Acquisition & Sign | N/A | Techman | 1 | $6.49 | $6.49 |
|12.5 A Fuse| Pack of 5, 3/16" X 3/4" (5X20mm) 12.5A 250V Glass Fuses, Slow Blow | Secondary Data Acquisition & Sign | N/A | Techman | 1 | $8.79 | $8.79 |
|Fuse Cartridge| Fuse Block 20 A 250V 1 Circuit Cartridge Through Hole | Secondary Data Acquisition & Sign | 696108003002 | Würth Elektronik | 3 | $0.68 | $2.04 |
|Junction Box| Hinged Cover Stainless Steel Latch 410x310x180mm Junction Box with Mounting Plate, Universal IP67 | Secondary Data Acquisition & Sign | N/A | QILIPSU | 3 | $75.99 | $227.97 |
|Locknut| 3/4 NPT Nylon Cable Gland, Waterproof IP68 Adjustable Locknut for 13-18mm Cable Diameter (3/4 NPT, 6pcs) | Secondary Data Acquisition & Sign | N/A | QILIPSU | 2 | $10.99 | $21.98 |
| Total | | | | Total Components | 22 | Total Cost | $1,007.70 |

## Cited Sources

[1] “Mega 2560 Rev3,” _Arduino Store_, 2023. https://store-usa.arduino.cc/products/arduino-mega-2560-rev3.

[2] “Arduino Mega Tutorial [Pinout],” _DiyIOt_. https://diyi0t.com/arduino-mega-tutorial/.

[3] “Car Led Strip Lights 32CM Waterproof Led Light Strips for Cars Motorcycles Golf Cart Interior & Exterior Marine Boat Red Led Strip 12V 5050 18SMD,Pack of 4,” _amazon.com_, 2023. https://www.amazon.com/Lights-Waterproof-Motorcycles-Interior-Exterior/dp/B09NBFTN34.

[4] “IRLZ44NPbF,” _International Rectifier_, 11 Nov 2003. https://www.infineon.com/dgdl/irlz44npbf.pdf?fileId=5546d462533600a40153567217c32725.

[5] “Arduino Uno Rev3,” _Arduino Store_, 2023. https://store-usa.arduino.cc/products/arduino-uno-rev3.

[6] “Arduino Uno Tutorial [Pinout],” _DiyIOt_. https://diyi0t.com/arduino-uno-tutorial/.

[7] “MPX53, 0 to 50 kPa, Differential and Gauge, Uncompensated, Silicon Pressure Sensors,” _NXP_, 2015. https://www.nxp.com/docs/en/data-sheet/MPX53.pdf.

[8] “WiFi Module - ESP8266 (4MB Flash),” _sparkfun_, 2023. https://www.sparkfun.com/products/17146.

[9] “Blue Hawk Powder-coated Steel U-post For Garden Fence,” _Lowes_, 2023. https://www.lowes.com/pd/Blue-Hawk-Common-3-1-2-in-x-5-ft-Actual-0-6-in-x-3-5-in-x-5-ft-Powder-Coated-Steel-Garden-Fence-U-post-Post/4780965.

[10] “12V 12Ah Lithium LiFePO4 Battery, HWE Deep Cycle Lithium Iron Phosphate Battery Built-in BMS, Offer 4000+ Cycles Life for Solar Energy, Small UPS, Fish Finder, Ride on Toy, and Alarm System,” _amazon.com_, 2023.

https://www.amazon.com/Battery-HWE-Lithium-LiFePO4-Lighting/dp/B09FP1NWFX/.

[11] “Pack of 5, 3/16" X 3/4" (5X20mm) 12.5A 250V Glass Fuses, Slow Blow (Time Delay) 12.5a, T12.5a, 12.5 amp 250v,” _amazon.com_, 2023. https://www.amazon.com/5X20mm-12-5A-Glass-Fuses-T12-5a/dp/B00HZLLE9I.

[12] “Pack of 5-250mA (0.25A) Glass Fuse (GMA), 250v, 5mm x 20mm (3/16" X 3/4") Fast Blow (Fast Acting),” _amazon.com_, 2023.  https://www.amazon.com/Pack-250mA-0-25A-Glass-Acting/dp/B074LB1CWC/ref=asc_df_B074LB1CWC/.

[13] “DOKIO 150 Watt 18 Volt Monocrystalline Solar Panel High Efficiency Module Durable RV Marine Boat Off Grid,” _amazon.com_, 2023. https://www.amazon.com/DOKIO-Watt-Monocrystalline-Solar-Panel/dp/B07CG8KV33/.

[14] “Powerwerx MPPT-150-14.6, DC-to-DC Solar Charger Controller for Bioenno 12V LiFePO4 Batteries,” _amazon.com_, 2023. https://www.amazon.com/Powerwerx-MPPT-150-14-6-Charger-Controller-Batteries/dp/B087ZSY8CR.

[15] “10-01776,” _Digi-Key_, 2023. https://www.digikey.com/en/products/detail/tensility-international-corp/10-01776/5638252. 

[16] “10-01776 Datasheet,” _Tensility_, 30 Apr 2015. https://tensility.s3.amazonaws.com/uploads/pdffiles/10-01776.pdf.

[17] “696108003002,” _Digi-Key_, 2023. https://www.digikey.com/en/products/detail/w%C3%BCrth-elektronik/696108003002/7244560.

[18] “BATTERY DOCTOR Primary Automotive Wire: 22 AWG Wire Size, PVC, Stranded, 100 ft Lg, Red,” _Grainger_, 2023. https://www.grainger.com/product/34GC76.

[19] “BATTERY DOCTOR Primary Automotive Wire: 22 AWG Wire Size, PVC, Stranded, 100 ft Lg, Black,” _Grainger_, 2023. https://www.grainger.com/product/34GC72. 

[20] “CHENBO 620pcs 2.54mm/0.1" Connectors Wire Jumper Cable Pin Header Connector Housing Assortment Kit Male Female Crimp Pin Connector Terminal Pitch With Plastic Box,” _amazon.com_, 2023. https://www.amazon.com/CHENBO-Connector-Housing-Assortment-Terminal/dp/B077X8XV2J/.

[21] “QILIPSU Hinged Cover Stainless Steel Latch 410x310x180mm Junction Box with Mounting Plate, Universal IP67 Project Box Waterproof DIY Electrical Enclosure, ABS Plastic Grey (16.1"x12.2"x7.1"),” _amazon.com_, 2023. https://www.amazon.com/dp/B08ZRR2DJX/.

[22] “IP Ratings Explained,” _Clarion_, 2023. https://clarionuk.com/resources/ip-ratings/.

[23] “QILIPSU 3/4 NPT Nylon Cable Gland, Waterproof IP68 Adjustable Locknut for 13-18mm Cable Diameter (3/4 NPT, 6pcs),” _amazon.com_, 2023. https://www.amazon.com/dp/B07ZRHPRP7/.

## Revisions

**02/16/2023**

Updated Big Picture section to better reflect the purpose of detail design.

Revised the constraints sections for readability.

Reorganized analysis section for readability and included electrical analysis.

Updated Bill of Materials.

Added more references.

**03/07/2023**

Updated Big Picture section to be more concise.

Revised the constraints sections to better reflect what needs to be analyzed.

Updated Analysis section to be more concise.

Updated Bill of Materials.

Revised references.
