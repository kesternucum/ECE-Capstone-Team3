# Sign System Detail Design



## Function of the Subsystem

The sign will be a physical entity at the entrance of the parking lot that will display the current number of available parking spots in the parking lot. This will allow students to decide if they even enter the parking lot and has the potential to save the students time searching for a parking spot. This subsystem is to be used in unity with the mobile application which will also display the same information. It will acquire its data from the server/database wirelessly with the initial data being from the data acquisition subsystem(s). It will then use custom seven-segment displays, a microprocessor, and a power transistor circuit to display this information on the physical sign.

## Constraints

1. Seven-Segment Display & Controls
- Must have waterproof controllable display viewable in the daylight (At least 2000 millicandelas at a 60 degree viewing angle or 1.68 Lumens [12] [13]) and from the road capable of showing number of open parking spots 
- Must have a microcontroller with at least a 14 Digital output PINs, RX/TX PINs, and capable of connecting a external wireless communication module to connect to the 
- Must have a power circuit for switching display LEDs on/off using power from separate subsystem

2. Outdoor Physical Sign/Stand
- Must be large enough to hold controllable display and static text viewable from the road
- Must be able to withstand reasonable weather requirements (storm, mid to heavy wind, etc.)

3. Weatherproofing
- Must protect Seven-Segment display controls at least partially from dust and water
- Must be mountable on interior of Physical Sign





## Buildable Schematic

![Figure 1. Arduino Circuit Diagram](../Electrical/Schematics/Sources/Display_Schematic.PNG)
<div align="center"> Figure 1. Arduino Circuit Diagram
<br />
<div align="left">


![Figure 2. Physical Sign Schematic](../3D&#32;Models/NewSignView1.PNG)
<div align="center"> Figure 2. Physical Sign PDF Schematic 
<br />
<div align="left">


![Figure 3. Physical Sign Schematic View 2](../3D&#32;Models/NewSignView2.PNG)
<div align="center"> Figure 2. Physical Sign PDF Schematic View 2
<br />
<div align="left">


## Analysis

1. Seven-Segment Display & Controls

a. LED Strips 

- Will consist of 7 red 12 V LED light strips per display (14 total)
- Wires will be fed through the sign through drilled holes at the end of each strip
> - Each LED strip is roughly 6 inches long
> - Each segment is roughly 7 inches (W) x 13 inches (H) 
> - The following analysis shows how these seven-segments will meet the required constraints of visibility:
> > - Length of road parallel to main entrance is roughly 100 feet and width is roughly 20 feet [9]
> > - Maximum viewing angle when entering the lot is 102 feet [9]
> > - Optimum viewing distance is 120 feet and maximum viewing distance is 525 feet [8]

- Keiurot LED strips chosen for:
> - Already waterproof (IP67 rated)
> - These LED strips claim to be rated for 1000 Lumens each, which meets the constraint of at least 2000 millicandelas at a 60 degree viewing angle or 1.68 Lumens to be seen in the daylight. 
> - 3M adhesive weather-resistant backing to attach directly to the sign.

The specs/features above show that the product meets the required constraints.
	
b. Microcontroller

- Arduino Mega board chosen for:
> - Necessary capabilities for number of PINs, serial communication, and output for ESP8266 module
> - 54 digital I/O ports and multiple serial communication PIN options
> - 3.3 V output for ESP8266 module and 16 PINs for outputs to power transistors and serial communication to external module
> - Arduino's IDE works well with ESP8266 module
> - Readily available from many different sources

The specs/features above show that the product meets the required constraints.
	
c. Power Transistor Circuits

- Power transistor circuit used for each LED, consisting of IRLZ44N power transistor, 12V DC source, 10 KOhm resistor, and grounding
- Each transistor connected to an Arduino Mega digital I/O pin

- IRLZ44NPBF power transistors chosen for:
> - Switching works with Arduino output voltage (5 V) and current (40 mA)
> - Power source of 12 V DC works well with board, LED strip, and power transistor configuration

The specs/features above show that the product meets the required constraints.

2. Wireless Data Transfer Module

- The Sparkfun ESP8266 Module was chosen for:
> - Its wireless capabilities
> - The module is very compatible with the Arduino Mega board and its IDE
- In-depth analysis can be found in the corresponding communication signoff.

The specs/features above show that the product meets the required constraints.
	
3. Outdoor Physical Sign/Stand

The RoadTrafficSigns Custom 18” x 24” Aluminum Sign was chosen due to it meeting the size constraint of being to at least be able to hold both seven segment displays totalling 16 inches x 13 inches (each display being 7 inches x 13 inches with 2 inches of spacing).

This sign also has customizable text options for placement and size when ordering  this meets the static text constraint.

This will then be mounted to the post shown in the power subsystem design using the add on mounting hardware with the custom sign. 
 
4. Power 

The power that will be sent to the sign will be a separate subsystem sending out 12 Volts and the required current output for connected components. This will be sent to each LED strip on the sign and to the Arduino. 

The in depth analysis of this will be in the corresponding power signoff.


5. Weatherproofing

Weatherproofing will be designed in the Sign Power subsystem. This will include casing for all of the transistors, Arduino, communication module, and battery.



## BOM for Sign

| Name of Item | Description | Used in which subsystem(s) | Part Number | Manufacturer | Quantity |    Price   | Total |
| ------------ | ----------- | -------------------------- | ----------- | ------------ | -------- | ---------- | ----- |
|Arduino Mega 2560 REV3 [A000067]|     "Microprocessor, 54 digital I/O pins, 16 analog inputs "|     Sign|     2560 R3|     Arduino|     1|     $48.40|     $48.40|
|Keiurot Car Led Strip Lights|     "2CM Waterproof Led Light Strips for Cars Motorcycles Golf Cart Interior & Exterior Marine Boat Red Led Strip 12V 5050 18SMD Pack of 4"|     Sign|     4P-MDLEST0011-R|     Keiurot|     4|     $12.69|     $50.76|
|IRLZ44NPBF|     "N-Channel 55 V 47A (Tc) 3.8W (Ta) 110W (Tc) Through Hole TO-220AB"|     Sign|     IRLZ44NPBF|     Infineon Technologies|     14|     $1.52|     $21.28|
|WiFi Module - ESP8266 (4MB Flash)|      Self contained SOC with integrated TCP/IP protocol stack that can give any microcontroller access to your WiFi network|     Sign|     WRL-17146|     Sparkfun|     1|     $7.50|     $7.50|
|Custom 18” x 24” Aluminum Sign|      Custom Aluminum Sign with Custom Wording|     Sign|    K-3428-BK|     RoadTrafficSigns|     1|     $37.75|     $37.75|
|Post Attachment Kit|      2 Bolts for Heavy Duty Posts and 2 Bolts for Economy Posts Attachment Hardware for Posts - 4 bolts|     Sign|	K-KIT2|     RoadTrafficSigns|     1|     $1.87|     $1.87|
|Total|     |     |     |     Total Components|    22|     Total Cost|     $167.56|

## Revisions

Rev. 1 
Added more detail to 3D schematic
Updated Analysis and Constraints with more detail
Switched some info in Analysis to Constraints

Rev. 2
Clarified LED strip and vinyl poster mounting in correlation to the 3D buildable schematic.
Removed unnecessary text from Constraints section.
Added mounting tape to BOM.

Rev. 3
Reorganized info completely/cut out most paragraphs and listed spec/constraints.

Rev. 4
Added info about LED visibility in daylight.

Rev. 5
Changed design from A-Frame sign to post with aluminum sign and clarified details about this in the analysis, BOM, and sources. 
	
## Cited Sources
 [1] “Arduino Mega 2560 REV3 [A000067],”amazon.com, 2022.
https://www.amazon.com/ARDUINO-MEGA-2560-REV3-A000067/dp/B0046AMGW0/ref=sr_1_3?keywords=Amazon.com%3A+Arduino+Mega+2560+REV3+%5BA000067%5D+%3A+Electronics&qid=1675097507&sr=8-3

[2] “Car Led Strip Lights 32CM Waterproof Led Light Strips for Cars Motorcycles Golf Cart Interior & Exterior Marine Boat Red Led Strip 12V 5050 18SMD,Pack of 4,” amazon.com, 2022. https://www.amazon.com/Lights-Waterproof-Motorcycles-Interior-Exterior/dp/B09NBFTN34?th=1

[3] “IRLZ44NPBF,” digikey.com, 2022.
https://www.digikey.com/en/products/detail/infineon-technologies/IRLZ44NPBF/811808

[4] “WiFi Module - ESP8266 (4MB Flash).” sparkfun.com, 2022.
https://www.sparkfun.com/products/17146

[5] “Sign Letter Height Visibility Chart.” Signazon.com, 2022. https://www.signazon.com/help-center/sign-letter-height-visibility-chart.aspx

[6] “Detailed Design for Camera Subsystem within Primary Data Acquisition System”. Github.com, 2022. https://github.com/kesternucum/ECE-Capstone-Team3/blob/main/Documentation/Signoffs/detaildesign_camera.md

[7] "Flemoon Large Outdoor Electrical Box (12.5 x 8.5 x 5 inch), IP54 Waterproof Outdoor Extension Cord Cover Weatherproof, Protect Outlet, Plug, Socket, Timer, Power Strip, Holiday Light Decoration, Black." Amazon.com, 2022. https://www.amazon.com/Flemoon-Electrical-Waterproof-Weatherproof-Decoration/dp/B09NLW5HMX/ref=sr_1_6?crid=1LA2KM2X4G1R0&keywords=waterproof%2Bjunction%2Bbox&qid=1675091689&sprefix=waterproof%2Bjunctio%2Caps%2C480&sr=8-6&th=1

[8] “Millicandela to lumens calculator.” Rapid Tables, 2022.
https://www.rapidtables.com/calc/light/mcd-to-lumen-calculator.html

[9] “LEDs that are visible in sunlight.” Maker Pro, 2022. https://maker.pro/forums/threads/leds-that-are-visible-in-sunlight.1046/

[10] “18" x 24" Customizable Horizontal Black Sign Template.” RoadTrafficSigns, 2022.
https://www.roadtrafficsigns.com/fos/custom-metal-sign/custom-metal-sign-18x24/sku-k-3428-bk
