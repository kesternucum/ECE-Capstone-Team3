# Secondary Data Acquisition & Sign Power Detail Design

## Big Picture

The Secondary Data Acquisition System and the Sign System have a number of design details in common including location, hardware usage, and power needs. Therefore, it should not be difficult to have both systems operating under one source of power. This design will go over the two cases of powering the “Post System” which includes with and without the sign, as well as how the posts will be structured to hold the power and other devices in a safe and accessible manner.

## Constraints

Existing Hardware Constraints

1. Sign Included
    * Arduino Mega 2560 Rev3 [2]
        * Input Voltage (recommended) - 7-12 V
        * Power Supply Connections - USB, 2.1mm center-positive plug, Vin & GND pin
        * Length - 101.52mm
        * Width - 53.3mm
    * LED Light Strips [3]
        * Input Voltage - 12 V
        * Power Supply Connection - Positive & Negative wire
    * IRLZ44NPBF (Transistor) [14]
        * Length - 3.3mm 
        * Width - 3.3mm 
        * Height - 1.6mm
2. Sign Not Included
    * Arduino Uno Rev3 [1]
        * Input Voltage (recommended) - 7-12 V
        * Power Supply Connections - USB, 2.1mm center-positive plug, Vin & GND pin
        * Length - 68.6mm
        * Width - 53.4mm
3. Sign Inclusion Irrelevant
    * Differential Pressure Sensor [14]
        * Length - 29.85mm
        * Width - 11.05mm
        * Height - 29.34mm
    * WiFi Module [16]
        * Length - 25.4mm
        * Width - 24.8mm

Chosen Hardware Constraints

1. Howell Energy Battery [5]
    * Length - 5.94 in (150.876mm)
    * Width - 2.56 in (65.024mm)
    * Height - 3.70 in (93.98mm)

Reliability Constraints

1. At a minimum, provide power during operational hours (8:00am - 4:30pm)
2. Protect electrical components from bad weather conditions (e.g. windy, rainy, snowy)
3. Components should have a good lifespan to minimize part replacement
4. Power should be rechargeable to minimize maintenance

Placement Constraints

1. The power source must be in a location that does not interfere with university parking
2. The power source must be within close proximity of the pneumatic tubes

## Buildable Schematic

![Figure 1. Device Connection](../Electrical/Arduino_Wiring_No_Sign_Schematic.PNG)

&lt;div align="center"> Figure 1. Device Connection

&lt;br />

&lt;div align="left">

![Figure 2. Device Connection With Sign](../Electrical/Arduino_Wiring_With_Sign_Schematic.PNG)

&lt;div align="center"> Figure 2. Device Connection With Sign

&lt;br />

&lt;div align="left">

![Figure 3. Post Model](../3D Models/Post_Model.PNG)

&lt;div align="center"> Figure 3. Post Model

&lt;br />

&lt;div align="left">

![Figure 4. Post Side View](../Images/Post_Side_Model.PNG)

&lt;div align="center"> Figure 4. Post Side View

&lt;br />

&lt;div align="left">

![Figure 5. Post Front View](../Images/Post_Front_Model.PNG)

&lt;div align="center"> Figure 5. Post Front View

&lt;br />

&lt;div align="left">

![Figure 6. Post Back View](../Images/Post_Back_Model.PNG)

&lt;div align="center"> Figure 6. Post Back View

&lt;br />

&lt;div align="left">

## Analysis

Meeting Hardware Constraints

1. It has worked in our favor that all devices that need to be powered, regardless of if the post has a sign or not, require 12 volts to be powered. Therefore, a Howell Energy 12 volt 7 amp-hour rechargeable battery [5] has been selected. The battery is lightweight, compact, and provides the needed 12 volts to all devices [5].
2. The Arduinos have a few options in order to receive power. Adapters for the USB option and the 2.1mm plug are both cheap [10][11], with the only additional requirement being for the USB adapter which is to ground the data pins [11]. For this design though, it has been decided to go with using the on-board Vin and GND pins. The reasoning behind this is that crimping the wiring from the battery to the Arduinos should be simple, the purchased wire is inexpensive for the amount received [7][8], the leftover wire can be used for other systems adding to its cost-effectiveness, and the wiring method will be consistent with the wiring plan for the LED strips (also crimping).

Meeting Reliability Constraints

1. In order to make sure that the system will require little maintenance power-wise, the battery chosen is rechargeable, and the easiest method of recharging will be done via solar power given the posts will be nowhere near any outlets outside. Therefore, the 12 volt solar panel made by Dakota Lithium has been selected. The panel is compatible with 12 volt 7 amp-hour batteries, weatherproof, and can fully charge the battery in under 9 hours (about a day's worth of sunlight) [4]. It also does not require a charge controller [4], so a connection to the battery via crimping should be sufficient to get it working. 
2. Replacement of the solar panel is also not a major concern, as most solar panels do not begin until about 10 years into its lifespan [12] and Dakota Lithium’s solar panel in particular has an 11 year warranty [4]. The Howell Energy battery only has a three-year warranty [5], but given that the project serves as a proof of concept, and the lower price of this battery, this will be accepted. Longer lasting batteries will be a consideration for future iterations of the project.
3. The battery, Arduinos, WiFi module, differential pressure sensors, and transistors are all devices that can’t be exposed to bad weather or they will quickly malfunction. Therefore, a casing to protect all of these devices is needed. In terms of amount, there will be one battery, one Arduino, one WiFi module, 2 differential sensors, and 14 transistors at most (as this is with the sign included). By adding all the dimensions of the items mentioned this means we need a space of, at a minimum, 383.696mm x 211.424mm x 175.06mm (15.106 in x 8.324 in x 6.892 in) where the Arduino used for this total is the Arduino Mega. To compensate for additional spacing needed to connect devices together, changes in device orientation, and not have a tight fit, the dimensions will be moved up to 406.4mm x 228.6mm x 177.8mm (16 in x 9 in x 7 in). Therefore, in order to fit all the devices, a QILIPSU 410mm x 310mm x 180mm junction box [18] has been chosen. It provides the needed space calculated, is IP67 rated so it should be sufficient to sustain the outdoors, and can easily be drilled into given it’s made of plastic [18] so wires can be pulled outside the box.

Meeting Placement Requirements

1. Our team has been granted permission to place posts into the ground around the Bell Hall parking lot, therefore, a post will be used to hold the needed solar panel, battery, and arduino. The posts will be placed in the areas as seen in Figure 7 with the post holding the sign notated by the yellow square. These locations are right next to the pneumatic tubes which will prevent leaving an excess of loose wire, as well as being located on the grass so they should not obstruct parking. The post with the sign is also located next to a parking entrance, so the sign should be easy to see for students driving into the lot.

![Figure 7. Post Placement](../Images/Post_Placement.PNG)

&lt;div align="center"> Figure 7. Post Placement

&lt;br />

&lt;div align="left">

## Bill of Materials

| Name of Item | Description | Used in which subsystem(s) | Part Number | Manufacturer | Quantity |    Price   | Total |

| ------------ | ----------- | -------------------------- | ----------- | ------------ | -------- | ---------- | ----- |

|Solar Panel|     "12V FLEXIBLE SOLAR PANEL – 20 WATTS"|     Post|     Number Not Found|     Dakota Lithium|     3|     $49.00|     $147.00|

|Rechargeable Battery|     "12V 7Ah Battery, HWE Energy Rechargeable LiFePO4 Battery, 4000+ Deep Cycle Lithium Iron Phosphate Battery Built-in BMS"|     Post|     Number Not Found|     Amazon|     3|     $34.56|     $103.68|

|Steel Post|     "Blue Hawk Powder-coated Steel U-post For Garden Fence"|     Post|     493053|     Lowe’s|     3|     $7.98|     $23.94|

|22 AWG Wire|     "BATTERY DOCTOR Primary Automotive Wire: 22 AWG Wire Size, PVC, Stranded, 100 ft Lg, Red"|     Post|     34GC76|     Grainger|     1|     $9.93|     $9.93|

|22 AWG Wire|     "BATTERY DOCTOR Primary Automotive Wire: 22 AWG Wire Size, PVC, Stranded, 100 ft Lg, Black"|     Post|     34GC72|     Grainger|     1|     $10.61|     $10.61|

|Crimp Kit|     "620pcs Dupont Line Connector 2.54mm Dupont Cable Jumper Wire Pin Header Housing Kit Male Crimp Pin Female Pin Terminal Connector"|     Post|     CQ00824|     Temu|     1|     $10.99|     $10.99|

|Junction Box|     "QILIPSU Hinged Cover Stainless Steel Latch 410x310x180mm Junction Box with Mounting Plate, Universal IP67 Project Box Waterproof DIY Electrical Enclosure, ABS Plastic Grey (16.1"x12.2"x7.1")"|     Post|     Number Not Found|     Amazon|     3|     $75.99|     $227.97|

|Locknut|     "QILIPSU 3/4 NPT Nylon Cable Gland, Waterproof IP68 Adjustable Locknut for 13-18mm Cable Diameter (3/4 NPT, 6pcs)"|     Post|     Number Not Found|     Amazon|     2|     $10.99|     $21.98|

## Cited Sources

[1] “Arduino Uno Rev3,” _arduino.cc_, 2023. https://store-usa.arduino.cc/products/arduino-uno-rev3.

[2] “Mega 2560 Rev3,” _arduino.cc_, 2023. https://store-usa.arduino.cc/products/arduino-mega-2560-rev3.

[3] “Car Led Strip Lights 32CM Waterproof Led Light Strips for Cars Motorcycles Golf Cart Interior & Exterior Marine Boat Red Led Strip 12V 5050 18SMD,Pack of 4,” _amazon.com_, 2022. https://www.amazon.com/Lights-Waterproof-Motorcycles-Interior-Exterior/dp/B09NBFTN34.

[4] “12V FLEXIBLE SOLAR PANEL - 20 WATTS,” _Dakota Lithium_, 2023. https://dakotalithium.com/product/12v-solar-panel/.

[5] “12V 7Ah Battery, HWE Energy Rechargeable LiFePO4 Battery, 4000+ Deep Cycle Lithium Iron Phosphate Battery Built-in BMS, Perfect for Fish Finder, Alarm System, Small UPS, Solar, Ride on Toys,” _amazon.com_, 2023. https://www.amazon.com/Battery-HWE-Energy-Rechargeable-Phosphate/dp/B0B4R1PJK9/ref=asc_df_B0B4R1PJK9/.

[6] “Blue Hawk Powder-coated Steel U-post For Garden Fence,” _Lowes_, 2023. https://www.lowes.com/pd/Blue-Hawk-Common-3-1-2-in-x-5-ft-Actual-0-6-in-x-3-5-in-x-5-ft-Powder-Coated-Steel-Garden-Fence-U-post-Post/4780965.

[7] “BATTERY DOCTOR Primary Automotive Wire: 22 AWG Wire Size, PVC, Stranded, 100 ft Lg, Red,” _Grainger_, 2023. https://www.grainger.com/product/34GC76.

[8] “BATTERY DOCTOR Primary Automotive Wire: 22 AWG Wire Size, PVC, Stranded, 100 ft Lg, Black,” _Grainger_, 2023. https://www.grainger.com/product/34GC72. 

[9] “620pcs Dupont Line Connector 2.54mm Dupont Cable Jumper Wire Pin Header Housing Kit Male Crimp Pin Female Pin Terminal Connector,” _Temu_, 2023. https://www.temu.com/620pcs-dupont-line-connector-2-54mm-dupont-cable-jumper-wire-pin-header-housing-kit-male-crimp-pin-female-pin-terminal-connector-g-601099512221152.html.

[10] “10-01935,” _Digi-Key_, 2023. https://www.digikey.com/en/products/detail/tensility-international-corp/10-01935/5638259. 

[11] “USB Type A Plug Breakout Cable with Premium Female Jumpers - 30cm long,” _adafruit_, 2023. https://www.adafruit.com/product/4448.

[12] Sendy, Andrew, “How long do solar panels actually last?” _SolarReviews_, 14 Jan 2022.  https://www.solarreviews.com/blog/how-long-do-solar-panels-last.

[13] “MPX53, 0 to 50 kPa, Differential and Gauge, Uncompensated, Silicon Pressure Sensors,” _NXP_, 2015. https://www.nxp.com/docs/en/data-sheet/MPX53.pdf.

[14] “IRLZ44NPBF,” _Digi-Key_, 2023. https://www.digikey.com/en/products/detail/infineon-technologies/IRLZ44NPBF/811808.

[15] “QILIPSU 3/4 NPT Nylon Cable Gland, Waterproof IP68 Adjustable Locknut for 13-18mm Cable Diameter (3/4 NPT, 6pcs),” _amazon.com_, 2023. https://www.amazon.com/dp/B07ZRHPRP7/ref=emc_b_5_t.

[16] “WiFi Module - ESP8266 (4MB Flash),” _sparkfun_, 2023. https://www.sparkfun.com/products/17146.

[17] “IP Ratings Explained,” _Clarion_, 2023. https://clarionuk.com/resources/ip-ratings/.

[17] “QILIPSU Hinged Cover Stainless Steel Latch 410x310x180mm Junction Box with Mounting Plate, Universal IP67 Project Box Waterproof DIY Electrical Enclosure, ABS Plastic Grey (16.1"x12.2"x7.1"),” _amazon.com_, 2023. https://www.amazon.com/dp/B08ZRR2DJX/ref=sspa_dk_detail_3.
