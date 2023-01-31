# Sign System Detail Design



## Function of the Subsystem

The sign will be a physical entity at the entrance of the parking lot that will display the current number of available parking spots in the parking lot. This will allow students to decide if they even enter the parking lot and has the potential to save the students time searching for a parking spot. This subsystem is to be used in unity with the mobile application which will also display the same information. It will acquire its data from the server/database wirelessly with the initial data being from the data acquisition subsystem(s). It will then use custom seven-segment displays, a microprocessor, and a power transistor circuit to display this information on the physical sign.

## Constraints

1. Seven-Segment Display & Controls

The Seven-Segment (SS) display needs to be large enough to be seen from the entrance into the parking lot. After lots of research, not many options are available for large seven segment displays that are waterproof/weatherproof and cost-effective, so the idea of creating a custom large waterproof seven-segment display arose. This will consist of seven red 12 V LED light strips [2] per display, so 14 of them total. The chosen LED strips can be cut to the desired length for whatever application, which will roughly be 6 inches per strip. This will make each segment roughly 7 inches (W) x 13 inches (H). With each display having a height of 13 inches this would correlate to an optimum viewing distance of 120 feet and a maximum viewing distance of 525 feet. This would be just above perfect with the length of the road parallel to the main entrance of the lot being roughly 100 feet and a width of roughly 20 feet the max viewing angle when coming into the lot would not exceed 102 feet [9] . Keep in mind that this is for an optimum viewing distance and the max viewing distance will be significantly greater. [8]

These will be configured and controlled much like typical SS displays minus the decimal point due to that not being necessary for this application. Each LED will then be controlled either being on or off by an Arduino Mega 2560 REV3 [A000067] [1]. This specific Arduino board has 54 digital I/O ports which is necessary for this application. Previously, an Arduino Uno board was chosen for this, but the wireless module must use the serial pins (TXD and RXD) for communication on the board. These pins share the same ports as two of the digital I/O ports. This would leave only 12 I/O pins available, while 14 are needed. Each output only sends a 5 V signal with 40 mA of current. This is not enough voltage or current for the LEDs, therefore a power transistor circuit will be used for each LED consisting of a IRLZ44N [6] power transistor, a 12V DC source, a 10 KOhm resistor, and necessary grounding. Each LED strip will then be connected to each Arduino Uno digital I/O pin. The necessary programming will then be in place to control each pin on the Arduino board. Please note that the 12 V source will be separate, and will be designed to meet the load requirements for the board, module, and each LED strip.

![Figure 1. Arduino Circuit Diagram](../Electrical/Schematics/Sources/Display_Schematic.PNG)
<div align="center"> Figure 1. Arduino Circuit Diagram
<br />
<div align="left">


2. Wireless Data Transfer Module

The chosen wireless data transfer module will be a part of the communications subsystem, but the device that will allow for this capability will be the ESP8288 WiFi module [7]. This device also specifically works with the Arduino IDE very well. 




3. Outdoor Physical Sign/Stand

The physical sign stand will be an A-Frame sandwich style sign that expands and has room to put each SS display. As stated above, each segment will roughly be 7 inches x 13 inches which will fit in the sign (24 inches x 36 inches). Each display will be evenly spaced with roughly a 2 inch gap in between displays. The chosen sign also has holes to fill with sand for added weight and stability[4]. A custom waterproof vinyl poster will also be attached to this sign displaying the text “Open Spots Available” [5].  


4. Power 

The power that will be sent to the sign will be a separate subsystem sending out 12 Volts. This will be sent to each LED strip on the sign and to the Arduino. 

5. Weatherproofing

The board must be protected from the elements, since it will be placed outdoors in the parking lot. Therefore, an enclosure for the Arduino and the power transistor circuits is crucial. Preferably, an IP67 rated enclosure would be used for every non-waterproof electronic device. Yet, for a more cost effective option an IP54 rated enclosure could be used with some extra reinforcing around where the wires come in and out. This is due to the extra protection it will get due to it being mounted on the inside of the A-Frame sign. This enclosure would then need to be large enough to fit the Arduino Mega, all 14 power transistors, the ESP8266 module and all wiring connecting each of these devices.

The Arduino Mega board is roughly 101mm x 53.3mm[1]. The dimensions of the IRLZ44NPBF power transistors are 3.3mm x 3.3mm x 1.6mm (L x W x H)[6]. Therefore, if two rows of 7 transistors were mounted with a spacing of 2mm in between each transistor an area of 37.1 mm x 10.6 mm (L x W) would be necessary for the transistors. The height will not be an issue due to how miniscule of a number it is. Then, with the Arduino Mega board included with a spacing of 20 mm from the transistors (for wiring) it would be a total area of 110.4 mm x 84.1 mm. Then, the Sparkfun ESP8266 Wi-Fi module then has dimensions 25.4 mm x 24.8 mm, so adding this with a spacing of at least 10 mm the total area would then be at least 145.2 mm x 119.5 mm. Lastly, to add a tolerance from each edge of the enclosure of at least 40 mm, the total area should be at least 225.2 mm x 199.5 mm (8.87 inches x 7.85 inches) for the entire enclosure. Anything larger than the minimal area would be fine as well.
	


## Buildable Schematic

![Figure 2. Physical Sign Schematic](../3D&#32;Models/3DSign.PNG)
<div align="center"> Figure 2. Physical Sign PDF Schematic 
<br />
<div align="left">

## Analysis
	
Seven-Segment Display 

The Keiurot LED strips were chosen due to them being an adjustable (length 32 cm) cost-effective option that is already waterproof (IP67 rated), bright, and a readily available product. The Arduino Mega board was chosen due to the necessary capabilities mentioned in the constraints above (number of PINs, serial communication, available power output for the ESP8266 module). It has 54 digital I/O ports as well as multiple serial communication PIN options, but the most important point is that the board has a 3.3 V output for the ESP8266 module and all 16 PINS needed for the outputs to the power transistors and serial communication to the external module. This board was also chosen due to Arduino’s IDE working very well with the ESP8266 module. This board is also readily available from many different sources unlike other comparable boards. The IRLZ44NPBF power transistors were chosen due to them being a cost-effective option that has switching that works with the Arduino output voltage (5 V) and current (40 mA) from the output PINs using the configuration seen in Figure 1. A power source of 12 V DC also works perfectly with the board and the chosen 12 V LED strip and power transistor configuration [1][6].

Wireless Transfer Module
The Sparkfun ESP8266 Module was chosen due to its wireless capabilities as well as its ease of use with the Arduino Mega board and IDE. The in depth analysis of this will be included in the corresponding communication signoff.


Physical Sign
The physical sign was chosen due to it being large enough to hold both seven-segment displays on the face (24 in x 36 in), the option to add sand for added weight and stability, and it being able to be easily moved from one spot to another before the sand is added. The custom vinyl poster was chosen due to it being a waterproof and readily available option. The A-Frame design was also a chosen benefit due to it adding extra protection and a mounting surface for the case holding the Arduino, transistors, and ESP8266 module.


Power
The in depth analysis of this will be in the corresponding power signoff.

Weatherproofing
The chosen weatherproofing case is the Flemoon IP54 rated enclosure [10]. This was chosen due to its cost-effectiveness and size (12.5 in x 8.5 in x 5 in). This will also meet all of the required specifications of size and water resistance. 



## BOM for Sign

| Name of Item | Description | Used in which subsystem(s) | Part Number | Manufacturer | Quantity |    Price   | Total |
| ------------ | ----------- | -------------------------- | ----------- | ------------ | -------- | ---------- | ----- |
|Arduino Mega 2560 REV3 [A000067]|     "Microprocessor, 54 digital I/O pins, 16 analog inputs "|     Sign|     2560 R3|     Arduino|     1|     $48.40|     $48.40|
|Keiurot Car Led Strip Lights|     "2CM Waterproof Led Light Strips for Cars Motorcycles Golf Cart Interior & Exterior Marine Boat Red Led Strip 12V 5050 18SMD|      Pack of 4"|     Sign|     4P-MDLEST0011-R|     Keiurot|     4|     $12.69|     $50.76|
|Jumbl Outdoor A-Frame Sandwich Signboard 24” x 36” Display Surface|     PVC Sign Protector & Sand Fill Holes – Duel Display Signage Stand for Storefront Sidewalk Curb (Black)|     Sign|     JUMCHH583B|     Jumbl|     1|     $129.99|     $129.99|
|Sakrete 0.5-cu ft 50-lb All-purpose Sand|     All Purpose Sand|     Sign|     40100223|     Sakrete|     1|     $5.48|     $5.48|
|wall26 Custom Poster Prints|     "Personalized Pictures Photos to Vinyl|      Durable and Waterproof 24x36 inches"|     Sign|     PPP-CUSTOM-24x36|     wall26|     1|     $22.99|     $22.99|
|IRLZ44NPBF|     "N-Channel 55 V 47A (Tc) 3.8W (Ta)|      110W (Tc) Through Hole TO-220AB"|     Sign|     IRLZ44NPBF|     Infineon Technologies|     14|     $1.52|     $21.28|
|WiFi Module - ESP8266 (4MB Flash)|      Self contained SOC with integrated TCP/IP protocol stack that can give any microcontroller access to your WiFi network|     Sign|     WRL-17146|     Sparkfun|     1|     $7.50|     $7.50|
|Flemoon Electrical Junction Box|     IP54 Waterproof Outdoor Extension Cord Cover Weatherproof, Protect Outlet|     Sign|     B09NLW5HMX|    Flemoon|     1|     $29.99|     $29.99|
|Total|     |     |     |     Total Components|     24|     Total Cost|     $316.47|

## Revisions

Rev 1. 
Added more detail to 3D schematic
Updated Analysis and Constraints with more detail
Switched some info in Analysis to Constraints

## Cited Sources
 [1] “Arduino Mega 2560 REV3 [A000067],”amazon.com, 2022.
https://www.amazon.com/ARDUINO-MEGA-2560-REV3-A000067/dp/B0046AMGW0/ref=sr_1_3?keywords=Amazon.com%3A+Arduino+Mega+2560+REV3+%5BA000067%5D+%3A+Electronics&qid=1675097507&sr=8-3

[2] “Car Led Strip Lights 32CM Waterproof Led Light Strips for Cars Motorcycles Golf Cart Interior & Exterior Marine Boat Red Led Strip 12V 5050 18SMD,Pack of 4,” amazon.com, 2022. https://www.amazon.com/Lights-Waterproof-Motorcycles-Interior-Exterior/dp/B09NBFTN34?th=1

[3] “Jumbl Outdoor A-Frame Sandwich Signboard 24” x 36” Display Surface – w/PVC Sign Protector & Sand Fill Holes – Duel Display Signage Stand for Storefront Sidewalk Curb (Black),” amazon.com, 2022.
https://www.amazon.com/Jumbl-Outdoor-Sandwich-Signboard-Display/dp/B07VXKV2QB

[4] “Sakrete  0.5-cu ft 50-lb All-purpose Sand,” lowes.com, 2022.
https://www.lowes.com/pd/Sakrete-50-lb-All-purpose-Sand/1000489239

[5] “wall26 Custom Poster Prints, Personalized Pictures Photos to Vinyl, Durable and Waterproof 24x36 inches,” amazon.com, 2022.
https://www.amazon.com/wall26-Custom-Poster-Print-Personalized/dp/B079Y7VBZF/ref=sr_1_1?crid=1WILJ4L2P2HH1&keywords=Amazon.com%3A%2Bwall26%2BCustom%2BPoster%2BPrints%2C%2BPersonalized%2BPictures%2BPhotos%2Bto%2BVinyl%2C%2BDurable%2Band%2BWaterproof%2B24x36%2Binches%3A%2BPosters%2B%26%2BPrints&qid=1675098243&sprefix=amazon.com%2Bwall26%2Bcustom%2Bposter%2Bprints%2C%2Bpersonalized%2Bpictures%2Bphotos%2Bto%2Bvinyl%2C%2Bdurable%2Band%2Bwaterproof%2B24x36%2Binches%2Bposters%2B%26%2Bprints%2Caps%2C379&sr=8-1&th=1

[6] “IRLZ44NPBF,” digikey.com, 2022.
https://www.digikey.com/en/products/detail/infineon-technologies/IRLZ44NPBF/811808

[7] “WiFi Module - ESP8266 (4MB Flash).” sparkfun.com, 2022.
https://www.sparkfun.com/products/17146

[8] “Sign Letter Height Visibility Chart.” Signazon.com, 2022. https://www.signazon.com/help-center/sign-letter-height-visibility-chart.aspx

[9] “Detailed Design for Camera Subsystem within Primary Data Acquisition System”. Github.com, 2022. https://github.com/kesternucum/ECE-Capstone-Team3/blob/main/Documentation/Signoffs/detaildesign_camera.md

[10] "Flemoon Large Outdoor Electrical Box (12.5 x 8.5 x 5 inch), IP54 Waterproof Outdoor Extension Cord Cover Weatherproof, Protect Outlet, Plug, Socket, Timer, Power Strip, Holiday Light Decoration, Black." Amazon.com, 2022. https://www.amazon.com/Flemoon-Electrical-Waterproof-Weatherproof-Decoration/dp/B09NLW5HMX/ref=sr_1_6?crid=1LA2KM2X4G1R0&keywords=waterproof%2Bjunction%2Bbox&qid=1675091689&sprefix=waterproof%2Bjunctio%2Caps%2C480&sr=8-6&th=1
