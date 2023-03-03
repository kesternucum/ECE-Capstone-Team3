# Secondary Data Acquisition & Sign Power Detail Design

## Big Picture

The Secondary Data Acquisition subsystem and the Sign subsystem have a number of design details in common including location, hardware usage, and power needs. Therefore, it should not be difficult to have both systems operating under one source of power. This design covers the streamlined design of powering both of the aforementioned subsystems, as well as how all relevant devices will be secured.

## Constraints

Existing Hardware Constraints

1. Sign Included
    * Arduino Mega 2560 Rev3 [1]
        * Input Voltage (recommended) - 7-12 V
        * Current Draw - 73.19 mA @ 9 V [2]
        * Power Supply Connections - USB, 2.1mm center-positive plug, Vin & GND pin
        * Dimension - 101.52 mm x 53.3 mm
    * LED Light Strips [3]
        * Input Voltage - 12 V
        * Current Draw - 700 mA
        * Power Supply Connection - Positive & Negative wire
    * IRLZ44NPBF (Transistor) [4]
        * Dimensions - 3.3 mm x 3.3 mm x 1.6 mm
2. Sign Not Included
    * Arduino Uno Rev3 [5]
        * Input Voltage (recommended) - 7-12 V
        * Current Draw - 98.43 mA @ 9 V [6]
        * Power Supply Connections - USB, 2.1mm center-positive plug, Vin & GND pin
        * Dimension - 68.6 mm x 53.4 mm
3. Sign Inclusion Irrelevant
    * Differential Pressure Sensor [7]
        * Dimensions - 29.85 mm x 11.05 mm x 29.34 mm
    * WiFi Module [8]
        * Dimensions - 25.4 mm x 24.8 mm

Reliability Constraints

1. Must provide power during operational hours (8:00am - 4:30pm)
2. Protect electrical components from bad weather conditions (e.g. windy, rainy, snowy)
3. Components should have a good lifespan to minimize part replacement
4. Power source should be rechargeable to minimize maintenance

Placement Constraints

1. The power source must be in a location that does not interfere with university parking
2. The power source must be within close proximity of the pneumatic tubes
3. The power source must be within close proximity of the sign

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

Placement of the Power Source

1. Given the needed constraint to have the power source be located close to both the pneumatic tubes and sign, an analysis was done referencing where the pneumatic tubes will be located on the Bell Hall lot as seen in Figure 7. Given that the sign also needs to be mounted at a decent height and located close to one of the parking lot entrances, it was decided to place posts at the designated purple and yellow square locations also seen in Figure 1. By utilizing posts at these locations, there will be a short distance to connect power to the pneumatic tubes while not interfering with parking traffic or visibility. The sign will be placed on the post itself to make connections from the power supply easy.
2. The selected post for the job is a 5 ft powder-coated steel post made by Blue Hawk [9]. This post provides sufficient height for the sign, was permitted to be placed by the campus’ Facilities department, and features a special anchor plate to ensure it remains stable [9] in the ground given any bad weather. It also has a number of small screw holes [9] which should make installation of the sign and other needed items to the post simple and sufficiently secure.

![Post_Placement](https://user-images.githubusercontent.com/80428236/219543389-bb18b5e1-8dec-4e8c-9cc5-fdf84bdf782e.jpg)

Figure 7. Post Placement

Selecting the Power Source

1. It serves to the convenience of this subsystem that all devices that need to be powered (Arduinos and LEDs) can accept or require 12 volts to operate (as seen in the constraints section). Therefore, it has been decided to go with a 12 V 12 Ah LiFePO4 battery produced by Howell Energy [10]. These batteries do not occupy much space (5.94 x 3.86 x 3.86 in or 151 x 98 x 98 mm) and last much longer than their sealed lead-acid counterpart, as well as being capable of being recharged [10]. 

Recharging the Power Source

1. The only feasible solution for recharging the battery given its location is by using a solar panel. Therefore, a 30 W 24 V solar panel made by Newpowa [11] has been selected. The solar panel will be used in tandem with a charger controller designed to take in 16-25 V and convert it to a 12-14.6 V output [13], and is also rated to handle up to 150 W so there should be no compatibility issues. The charge controller is also designed in mind for charging LiFePO4 batteries [13], so it should function well with the Howell battery.

Connecting the Devices

1. Arduinos
    * Both of the Arduinos can use the exact same methods to have power connected to them (those being via USB, a 2.1 mm center-positive plug, or a Vin and GND pin as seen in the constraints). USB-to-terminal adapters do not seem to be as prevalent on the market, and the USB port of the Arduinos looks for a 5 V input [1,5] which may cause some compatibility issues with the battery. The Vin and GND pin would make connections simple given only wire needs to be inserted in the pins then connected with the battery, but due to the issues of trying to get a reliable and permanent connection between the two, it has been decided to go with a 2.1 mm plug instead. The selected 2.1 mm plug has a rating of 48 V and 8.5 A [14], so it should be able to handle any output produced by the battery. In order to protect the Arduinos from the battery, a 250 mA fuse [19] will be connected between it and the battery in the event that the Arduino draws an excessive amount of current.
2. LEDs
    * The LEDs only have a positive and negative terminal wire to connect to, so the wires will be connected to the power source via crimp pins for simplicity. In order to protect the LEDS from the battery, a 750 mA fuse [20] will be connected between them and the battery in the event that the LEDs draw an excessive amount of current.

Distributing Power

1. Each of the LEDs drain about 700 mA of current in order to remain powered, and given that 14 of these LEDs need to be powered at any given time, there will be a maximum current draw of 9.8 A. The battery should be able to handle this given that it can output up to 12 A [10]. 
2. The Arduino Mega draws about 73.19 mA of current [2] and the Arduino Uno draws about 98.43 mA of current [6]. Given that adding either of these values to the current draw of the LEDs still totals less than the 12 A output of the Howell battery [10], there is still no concern that the battery cannot sufficiently power all devices.

Protecting the Electrical Components

1. All electrical components (minus the solar panel) combined are expected to take up about 383.82 x 244.4 x 179.08 mm (or 15.11 x 9.62 x 7.05 in) of space where the Arduino used for this total is the Arduino Mega (since it is larger than the Uno). To compensate for additional spacing needed to connect devices together, changes in device orientation, and not having a tight fit, the dimensions will be rounded to a minimum of 406.4 x 254 x 180 mm (or 16 x 10 x 7.08 in). Therefore,  a QILIPSU 410 x 310 x 180 mm junction box [22] has been chosen. It provides the needed space calculated, is IP67 rated so it should be sufficient to sustain any inclement weather [23], and can easily be drilled into given it’s made of plastic [22] so wires can be pulled outside the box. IP68 locknuts [24] will be inserted into the drilled holes to ensure case integrity still remains good.

Important Notes

1. Wire connections between the Arduinos and LEDs are shown in figures 1 and 2.
2. The high level setup of the post with the solar panel and pack protecting electrical devices are shown in figures 3 through 6.
3. The BoM does not accurately reflect what will be purchased, but instead how much the system would need given the original outline of the project. 

## Bill of Materials

| Name of item | Description | Subsystem | Part Number | Manufacturer | Quantity | Price | Total |
|--------------|-------------|-----------|-------------|--------------|----------|-------|-------|
|Solar Panel| 30W 24V Monocrystalline Solar Panel | Secondary Data Acquisition & Sign | N/A | Newpowa | 3 | $46.99 | $140.97 |
|Rechargeable Battery| 12V 12Ah Battery, HWE Energy Rechargeable LiFePO4 Battery, Built-in BMS | Secondary Data Acquisition & Sign | N/A | Howell Energy | 3 | $54.99 | $164.97 |
|Steel Post| Powder-coated Steel U-post | Secondary Data Acquisition & Sign | 493053 | Blue Hawk | 3 | $7.98 | $23.94 |
|22 AWG Wire| 22 AWG Wire Size, PVC, Stranded, 100 ft Lg, Red | Secondary Data Acquisition & Sign | 34GC76 |Grainger | 1 | $9.93 | $9.93 |
|22 AWG Wire| 22 AWG Wire Size, PVC, Stranded, 100 ft Lg, Black | Secondary Data Acquisition & Sign | 34GC72 |Grainger | 1 | $10.61 | $10.61 |
|Crimp Kit| CHENBO 620pcs 2.54mm/0.1" Connectors Wire Jumper Cable Pin Header Connector Housing Assortment Kit | Secondary Data Acquisition & Sign | CQ00824 | Chenbo | 1 | $10.99 | $10.99 |
|250 mA Fuse| Pack of 5-250mA (0.25A) Glass Fuse (GMA), 250v, 5mm x 20mm (3/16" X 3/4") Fast Blow | Secondary Data Acquisition & Sign | N/A | Techman | 2 | $6.49 | $12.98 |
|750 mA Fuse| Pack of 5-750mA (0.75A) Glass Fuse (GDC), 250v, 5mm x 20mm (3/16" X 3/4") Slow Blow | Secondary Data Acquisition & Sign | N/A | Techman | 3 | $5.99 | $17.97 |
|Fuse Cartridge| FUSE HLDR CARTRIDGE 250V 5A PCB | Secondary Data Acquisition & Sign | 4268 | Keystone Electronics | 17 | $0.73 | $12.41 |
|Junction Box| Hinged Cover Stainless Steel Latch 410x310x180mm Junction Box with Mounting Plate, Universal IP67 | Secondary Data Acquisition & Sign | N/A | QILIPSU | 3 | $75.99 | $227.97 |
|Locknut| 3/4 NPT Nylon Cable Gland, Waterproof IP68 Adjustable Locknut for 13-18mm Cable Diameter (3/4 NPT, 6pcs) | Secondary Data Acquisition & Sign | N/A | QILIPSU | 2 | $10.99 | $21.98 |
| Total | | | | Total Components | 39 | Total Cost | $654.72 |

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

[11] “30W 24V Monocrystalline Solar Panel,” _Newpowa_, 2023. https://www.newpowa.com/30w-24v-monocrystalline-solar-panel/.

[12] Sendy, Andrew, “How long do solar panels actually last?” _SolarReviews_, 14 Jan 2022.  https://www.solarreviews.com/blog/how-long-do-solar-panels-last.

[13] “Powerwerx MPPT-150-14.6, DC-to-DC Solar Charger Controller for Bioenno 12V LiFePO4 Batteries,” _amazon.com_, 2023. https://www.amazon.com/Powerwerx-MPPT-150-14-6-Charger-Controller-Batteries/dp/B087ZSY8CR.

[14] “10-01776,” _Digi-Key_, 2023. https://www.digikey.com/en/products/detail/tensility-international-corp/10-01776/5638252. 

[15] “10-01776 Datasheet,” _Tensility_, 30 Apr 2015. https://tensility.s3.amazonaws.com/uploads/pdffiles/10-01776.pdf.

[16] “BATTERY DOCTOR Primary Automotive Wire: 22 AWG Wire Size, PVC, Stranded, 100 ft Lg, Red,” _Grainger_, 2023. https://www.grainger.com/product/34GC76.

[17] “BATTERY DOCTOR Primary Automotive Wire: 22 AWG Wire Size, PVC, Stranded, 100 ft Lg, Black,” _Grainger_, 2023. https://www.grainger.com/product/34GC72. 

[18] “CHENBO 620pcs 2.54mm/0.1" Connectors Wire Jumper Cable Pin Header Connector Housing Assortment Kit Male Female Crimp Pin Connector Terminal Pitch With Plastic Box,” _amazon.com_, 2023. https://www.amazon.com/CHENBO-Connector-Housing-Assortment-Terminal/dp/B077X8XV2J/.

[19] “Pack of 5-250mA (0.25A) Glass Fuse (GMA), 250v, 5mm x 20mm (3/16" X 3/4") Fast Blow (Fast Acting),” _amazon.com_, 2023.  https://www.amazon.com/Pack-250mA-0-25A-Glass-Acting/dp/B074LB1CWC/ref=asc_df_B074LB1CWC/.

[20] “Pack of 5-750mA (0.75A) Glass Fuse (GDC), 250v, 5mm x 20mm (3/16" X 3/4") Slow Blow (Time Delay),” _amazon.com_, 2023. https://www.amazon.com/Pack-5-750mA-0-75A-Glass-Delay/dp/B074L9P4JM/ref=asc_df_B074L9P4JM/.

[21] “4268,” _Digi-Key_, 2023. https://www.digikey.com/en/products/detail/keystone-electronics/4628/2137316.

[22] “QILIPSU Hinged Cover Stainless Steel Latch 410x310x180mm Junction Box with Mounting Plate, Universal IP67 Project Box Waterproof DIY Electrical Enclosure, ABS Plastic Grey (16.1"x12.2"x7.1"),” _amazon.com_, 2023. https://www.amazon.com/dp/B08ZRR2DJX/.

[23] “IP Ratings Explained,” _Clarion_, 2023. https://clarionuk.com/resources/ip-ratings/.

[24] “QILIPSU 3/4 NPT Nylon Cable Gland, Waterproof IP68 Adjustable Locknut for 13-18mm Cable Diameter (3/4 NPT, 6pcs),” _amazon.com_, 2023. https://www.amazon.com/dp/B07ZRHPRP7/.

## Revisions

**03/02/2023**

Updated Big Picture section to better reflect the purpose of detail design.

Revised the constraints sections for readability.

Reorganized analysis section for readability and included electrical analysis.

Updated Bill of Materials.

Added more references.
