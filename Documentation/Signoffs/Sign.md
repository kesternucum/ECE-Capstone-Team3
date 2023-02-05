# Sign System Detail Design



## Function of the Subsystem

The sign will be a physical entity at the entrance of the parking lot that will display the current number of available parking spots in the parking lot. This will allow students to decide if they even enter the parking lot and has the potential to save the students time searching for a parking spot. This subsystem is to be used in unity with the mobile application which will also display the same information. It will acquire its data from the server/database wirelessly with the initial data being from the data acquisition subsystem(s). It will then use custom seven-segment displays, a microprocessor, and a power transistor circuit to display this information on the physical sign.

## Constraints

1. Seven-Segment Display & Controls
- Must have waterproof controllable display viewable from the road capable of showing number of open parking spots
- Must have a microcontroller with at least a 14 Digital output PINs, RX/TX PINs, and capable of connecting a external wireless communication module
- Must have a power circuit for switching display LEDs on/off using power from separate subsystem
2. Outdoor Physical Sign/Stand
- Must be large enough to hold controllable display and static text viewable from the road
- Must be able to withstand reasonable weather requirements (storm, mid to heavy wind, etc.)
- Must provide extra protection for seven-segment display controls
3. Weatherproofing
- Must protect Seven-Segment display controls at least partially from dust and water
- Must be mountable on interior of Physical Sign





## Buildable Schematic

![Figure 1. Arduino Circuit Diagram](../Electrical/Schematics/Sources/Display_Schematic.PNG)
<div align="center"> Figure 1. Arduino Circuit Diagram
<br />
<div align="left">


![Figure 2. Physical Sign Schematic](../3D&#32;Models/3DSign.PNG)
<div align="center"> Figure 2. Physical Sign PDF Schematic 
<br />
<div align="left">


![Figure 3. Physical Sign Schematic Showing Mounted Weatherproof Case](../3D&#32;Models/3DSignView2.PNG)
<div align="center"> Figure 2. Physical Sign PDF Schematic Showing Mounted Weatherproof Case
<br />
<div align="left">


## Analysis

1. Seven-Segment Display & Controls

a. LED Strips 

- Will consist of 7 red 12 V LED light strips per display (14 total)
> - Each LED strip is roughly 6 inches long
> - Each segment is roughly 7 inches (W) x 13 inches (H)
> > - Length of road parallel to main entrance is roughly 100 feet and width is roughly 20 feet [9]
> > - Maximum viewing angle when entering the lot is 102 feet [9]
> > - Optimum viewing distance is 120 feet and maximum viewing distance is 525 feet [8]

- Keiurot LED strips chosen for:
> - Cuttable to desired length (32 cm max)
> - Cost-effective ($12.79 for a 4 pack)
> - Already waterproof (IP67 rated)
> - Bright (1000 Lumens)
> - Readily available
> - 3M adhesive weather-resistant backing for easy attachment to sign

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

- Physical sign will be an A-Frame sandwich style sign that expands
- Room for each SS display (7 inches x 13 inches)
- Sign has holes to fill with sand for weight and stability
- Custom waterproof vinyl poster displaying "Open Spots Available" attached using adhesive double-sided tape.

	
- The Jumbl Outdoor A-Frame Sandwich Signboard was chosen for:
> - Its size (24 in x 36 in) which can hold both seven-segment displays.
> - The option to add sand for weight and stability.
> - The ability to be easily moved before the sand is added.
> - The A-Frame design adds extra protection and a mounting surface for the weatherproof box

- The wall26 Custom Poster Prints vinyl poster was chosen for:
> - Waterproof
> - Readily available
> - Mountable using Gorilla double sided weather-resistant adhesive tape 

The specs/features above show that the products meet the required constraints.
	
4. Power 

The power that will be sent to the sign will be a separate subsystem sending out 12 Volts and the required current output for connected components. This will be sent to each LED strip on the sign and to the Arduino. 

The in depth analysis of this will be in the corresponding power signoff.


5. Weatherproofing

- Flemoon IP54 rated enclosure was chosen for:
> - The case was chosen due to its cost-effectiveness and size (12.5 in x 8.5 in x 5 in).
> - Meets required specifications of size and water resistance.
- Mounted to the inside of the physical sign using double-sided weather-resistant adhesive tape.
- Gorilla double sided weather-resistant adhesive tape is rated to hold up to 60 lbs, so weight is not a concern.

The specs/features above show that the product meets the required constraints.

I. Background (Weatherproofing)

A cost-effective option of an IP54 rated enclosure will be used with some extra reinforcing around where the wires come in and out. This is due to the extra protection it will get due to it being mounted on the inside of the A-Frame sign. This enclosure would then need to be large enough to fit the Arduino Mega, all 14 power transistors, the ESP8266 module and all wiring connecting each of these devices.

The Arduino Mega board is roughly 101mm x 53.3mm[1]. The dimensions of the IRLZ44NPBF power transistors are 3.3mm x 3.3mm x 1.6mm (L x W x H)[6]. Therefore, if two rows of 7 transistors were mounted with a spacing of 2mm in between each transistor an area of 37.1 mm x 10.6 mm (L x W) would be necessary for the transistors. Then, with the Arduino Mega board included with a spacing of 20 mm from the transistors (for wiring) it would be a total area of 110.4 mm x 84.1 mm. Then, the Sparkfun ESP8266 Wi-Fi module then has dimensions 25.4 mm x 24.8 mm, so adding this with a spacing of at least 10 mm the total area would then be at least 145.2 mm x 119.5 mm. Lastly, to add a tolerance from each edge of the enclosure of at least 40 mm, the total area should be at least 225.2 mm x 199.5 mm (8.87 inches x 7.85 inches) for the entire enclosure. Anything larger than the minimal area would be fine as well.




## BOM for Sign

| Name of Item | Description | Used in which subsystem(s) | Part Number | Manufacturer | Quantity |    Price   | Total |
| ------------ | ----------- | -------------------------- | ----------- | ------------ | -------- | ---------- | ----- |
|Arduino Mega 2560 REV3 [A000067]|     "Microprocessor, 54 digital I/O pins, 16 analog inputs "|     Sign|     2560 R3|     Arduino|     1|     $48.40|     $48.40|
|Keiurot Car Led Strip Lights|     "2CM Waterproof Led Light Strips for Cars Motorcycles Golf Cart Interior & Exterior Marine Boat Red Led Strip 12V 5050 18SMD Pack of 4"|     Sign|     4P-MDLEST0011-R|     Keiurot|     4|     $12.69|     $50.76|
|Jumbl Outdoor A-Frame Sandwich Signboard 24” x 36” Display Surface|     PVC Sign Protector & Sand Fill Holes – Duel Display Signage Stand for Storefront Sidewalk Curb (Black)|     Sign|     JUMCHH583B|     Jumbl|     1|     $129.99|     $129.99|
|Sakrete 0.5-cu ft 50-lb All-purpose Sand|     All Purpose Sand|     Sign|     40100223|     Sakrete|     1|     $5.48|     $5.48|
|wall26 Custom Poster Prints|     "Personalized Pictures Photos to Vinyl Durable and Waterproof 24x36 inches"|     Sign|     PPP-CUSTOM-24x36|     wall26|     1|     $22.99|     $22.99|
|IRLZ44NPBF|     "N-Channel 55 V 47A (Tc) 3.8W (Ta) 110W (Tc) Through Hole TO-220AB"|     Sign|     IRLZ44NPBF|     Infineon Technologies|     14|     $1.52|     $21.28|
|WiFi Module - ESP8266 (4MB Flash)|      Self contained SOC with integrated TCP/IP protocol stack that can give any microcontroller access to your WiFi network|     Sign|     WRL-17146|     Sparkfun|     1|     $7.50|     $7.50|
|Flemoon Electrical Junction Box|     IP54 Waterproof Outdoor Extension Cord Cover Weatherproof, Protect Outlet|     Sign|     B09NLW5HMX|    Flemoon|     1|     $29.99|     $29.99|
|Gorilla Heavy Duty, Extra Long Double Sided Mounting Tape|  Extra Long Double Sided Mounting Tape|     Sign|    00052427008053|    Gorilla|     1|     $12.24|     $12.24|
|Total|     |     |     |     Total Components|     25|     Total Cost|     $328.71|

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
Reorganized info completely/cut out most paragraphs and listed spec/constraints

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

[11] “Gorilla Heavy Duty, Extra Long Double Sided Mounting Tape, 1" x 120", Black, (Pack of 1).” Amazon.com, 2022.
https://www.amazon.com/Gorilla-Heavy-Double-Sided-Mounting/dp/B082TQ3KB5/ref=asc_df_B082TQ3KB5?tag=bingshoppinga-20&linkCode=df0&hvadid=80195721143474&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=&hvtargid=pla-4583795268108518&th=1

