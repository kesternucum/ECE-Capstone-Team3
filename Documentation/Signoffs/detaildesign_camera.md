# Detailed Design for Camera Subsystem within Primary Data Acquisition System

## Big Picture
The primary data acquisition system will utilize real-time camera sensors to collect images of sectors of parking spots in the lot behind Bell Hall, in which these images will then be transmitted via wireless communication to a server where the images will be processed by an artificial intelligence (AI) algorithm to determine the number of red parking spots that are filled and unfilled by cars. This subsystem is a critical subsystem because these cameras will provide the primary data to the system that will determine the count of vehicles in a lot.

## Specifications

1. Selected Camera Specifications
  * Camera to Be Used: Avigilon 2.0 Megapixel Day/Night H.264 HD Indoor Dome Camera
    - Resolution: 2 MP
    - Active Pixels: 1920 pixels x 1080 pixels
    - Angle of View: 98°
    - Image Compression Method: H.264 (MPEG-4 Part 10/AVC), Motion JPEG
    - Image Rate: 30 fps
    - Streaming: Multi-Stream H.264 and Motion JPEG
    - API: ONVIF Compliant
    - Protocols: IPv4, HTTP, HTTPS, SOAP, DNS, NTP, RTSP, RTCP, RTP, TCP,UDP, IGMP, ICMP, DHCP, Zeroconf, ARP
    - Streaming Protocols: RTP/UDP, RTP/UDP multicast, RTP/RTSP/TCP, RTP/RTSP/HTTP/TCP, RTP/RTSP/ HTTPS/TCP, HTTP
    - Operating Temperature: -10°C - +50°C (14°F to 122°F)
    - Dimensions: 138 mm x 104 mm (5.4 in. by 4.1 in.)
    - Weight : 530g (1.17 lbs)
    - Power Consumption: 6 W with external power (10 W for -IR option)
    - Power Source: VDC: 12 V +/- 10%, 6 W min (10 W min with -IR option)
  * An important note is that these cameras can be obtained from the Information Technology Services (ITS) for no charge.

2. Positioning of Cameras
  * Placement in Parking Lot
    - The parking lot behind Bell Hall has 78 Red parking spots, as shown in Figure 1.

![Figure 1. Bell Hall Parking Lot with Red Spots and Light Posts] (../Images/Bell_Hall_Red_Spaces.png)

    - The only approved places that the cameras could be mounted upon are the light posts shown in Figure 1, thanks to Facilities at Tennessee Tech. The City of Cookeville did not allow us to hook up cameras on the lamp posts outlining the sidewalk around the Bell Hall lot. In addition, creating additional infrastructure (i.e. inflatable posts) was also not allowed by Facilities. The light posts, which are 5” square steel and are 25 ft tall on top of a 2 ft cement block. They provide a simple flat surface for easy mounting.
    - A total of 7 cameras will be used in this design implementation. Please see Figure 4 for their placement.
  * Attachment
    - Because drilling into posts is not allowed, hose clamps will be used to mount the cameras. The Dahua Technology PFA150 Pole Mount Bracket has been selected as the clamps to be used.
    - To maximize the field of range that the cameras can see, all cameras except Camera 6b will be placed at a height of 22 ft (2 ft cement block plus 20 ft of the post, giving some room between the cameras and the lights–the 5 ft space between the lights and the cameras give room to avoid the lights shining onto and then overheating the cameras). Camera 6b will be placed at 5 ft (2 ft cement block plus 3 ft of the post) since this camera is intended for detecting vehicles as they pass by (the same applies to Camera 6a), rather than tracking static parking spots.
  * Casing
    - The casing must protect the cameras from vandalism, weather, birds, etc.
    - The casing also cannot obstruct the view of the lens of the cameras.
    - The casing will be designed by the Mechanical Engineering team.

3. Monitoring of Parking Spaces and Entrances
  * Tracking Static Parking Spots
    - 5 cameras will be used to monitor individual parking spots in specified sectors (Sectors 1-5, see Analysis). For the sector in which it would be difficult to place cameras (Sector 6, in which the closest light post has a tree surrounding most of the light post), cameras will be placed at the entrances of that sector to monitor and track if a vehicle has entered or exited that area.

![Figure 2. Bell Hall Parking Lot Sectors] (../Images/Bell_Hall_Sectors.png)

  * Minimum Resolution
    - The measurements for a single parking spot in the Bell Hall lot is 18.8 ft x 8.69 ft (575 cm x 265 cm). Based on these measurements the whole area of the lot is then calculated in Figure 3.  The computer vision algorithms implemented [1] and [2] which detect and/or identify vehicles used training set images of the rear side of cars that were 64 x 64 pixels. A standard car is on average 5.8 feet [3], which translates to roughly a little over 10 pixels per foot (or 100 pixels per square foot) for these images of cars to be identified as such. Thus, the cameras must have a minimum pixels per foot of 10 pixels per foot (or 100 pixels per/square foot) to identify the presence of a car in a parking spot or entrance at the furthest point from the camera that a car could be positioned (see Analysis).

4. Maintainability
  * These cameras will require minimum maintenance once installed, and there should be a way to “recalibrate” the cameras remotely without having to physically access the cameras.

## Buildable PDF Schematic

[Datasheet with Schematic of Camera](../3D%Models/luxriot-vms-2022-11-22-172106.pdf)

[Mounting of Cameras on Light Posts] (../3D%Models/Camera_on_Light_Post.pdf)

## Analysis

1. Mounting
  *The mounting will be taken care of by a separate subsystem. This will include a mount to the pole as well as the mount to the cameras.

2. Positioning of Cameras (Field of View)

![Figure 3. Bell Hall Sectors Analysis] (../Images/Bell_Hall_Sectors_Analysis.png)

  * The above calculations display the minimum field of view required to capture each sector (excluding Sector 6). Sectors 1 through 5 can be captured within the field of view of the selected cameras, which have an FOV of 98°. In addition, for all sectors, the minimum pixels per foot of a car at the furthest point in the interested range has been calculated, all of which are greater than the desired 10 pixels per foot (meaning that the AI algorithm has a good pixel per foot to work with to identify vehicles).
  * To address the worst-case scenario, in which a tall car (e.g. a Toyota Tacoma roughly 7.67 ft) is next to a small car (e.g. a Nissan Sentra roughly 4.74 ft), with the small car in the further spot, to ensure at least 2.69 ft of the parking spot is visible, an angle of incidence from the 2.69 ft point to the camera of 22.7° (derived from the inverse tangent of 2.93 ft, the difference in height of the cars, divided by 7 ft, derived from assuming that the tall car is 1 ft from the parking spot boundary plus 6 ft of the parking spot the small car is in) is required, or a maximum angle that the camera can be pointed of 67.3°. This satisfies all static sectors except Sector 2; however, the frequency this scenario may occur (which is uncommon due to the prevalence of students driving SUVs) as well as that this may provide an error for one parking spot (compared with the acceptable margin of error with the secondary data acquisition system to be roughly 8 parking spots), shows that this risk is acceptable.

## Bill of Materials

| Name of Item | Description | Used in which subsystem(s) | Part Number | Manufacturer | Quantity | Unit Price | Total |
| ------------ | ----------- | -------------------------- | ----------- | ------------ | -------- | ---------- | ----- |
| Avigilon 2.0 Megapixel Day/Night H.264 HD Indoor Dome Camera | Camera | Primary Data Acquisition | 2.0-H3-D1 | Avigilon | 7 | $0.00 | $0.00 |
| | | | | | | | **$0.00** |

  * Note: ITS will be supplying these cameras, hence the cost of $0.00.

## Cited Sources

[1] A. Gunzi, “Vehicle Detection and Tracking using Computer Vision,” _Chatbots Life_, 7 Mar 2017. [https://chatbotslife.com/vehicle-detection-and-tracking-using-computer-vision-baea4df65906](https://chatbotslife.com/vehicle-detection-and-tracking-using-computer-vision-baea4df65906)

[2] B. Djukic, “Detecting vehicles using machine learning and computer vision,” _Towards Data Science_, 25 Apr 2017. [https://towardsdatascience.com/detecting-vehicles-using-machine-learning-and-computer-vision-e319ee149e10](https://towardsdatascience.com/detecting-vehicles-using-machine-learning-and-computer-vision-e319ee149e10)

[3] S. Meyer, “STUDY: Average Car Size is Increasing – will roads still be safe for small cars and pedestrians?,” _The Zebra_, 2022. [https://www.thezebra.com/resources/driving/average-car-size/](https://www.thezebra.com/resources/driving/average-car-size/)

[4] Duda, David, “Designing Video Surveillance Systems: Managing Owner’s Expectations,” _Newcomb & Boyd_, 2022. [https://www.newcomb-boyd.com/solutions/designing-video-surveillance-systems-managing-owners-expectations/](https://www.newcomb-boyd.com/solutions/designing-video-surveillance-systems-managing-owners-expectations/)

[5] “Security Cameras Wireless Outdoor, 2K ZUMIMALL 360° PTZ Outdoor Camera Wireless, Solar Security Cameras for Home, Spotlight & Siren/2.4G WiFi/3MP Color Night vision/2-Way Talk /PIR Detection/SD/Cloud,” _amazon.com_, 2022. [https://www.amazon.com/Zumimall-Security-Detection-Waterproof-Encrypted/dp/B092HPZJD5/ref=sr_1_2?crid=2ZK6O8X21WVLW&keywords=120%2Bdegree%2Boutdoor%2Bcamera&qid=1668026837&sprefix=%2Caps%2C81&sr=8-2&th=1](https://www.amazon.com/Zumimall-Security-Detection-Waterproof-Encrypted/dp/B092HPZJD5/ref=sr_1_2?crid=2ZK6O8X21WVLW&keywords=120%2Bdegree%2Boutdoor%2Bcamera&qid=1668026837&sprefix=%2Caps%2C81&sr=8-2&th=1)

[6] “Multi-Camera Vehicle Tracking System for AI City Challenge 2022,” _CvF_, 2022. [https://openaccess.thecvf.com/content/CVPR2022W/AICity/papers/Li_Multi-Camera_Vehicle_Tracking_System_for_AI_City_Challenge_2022_CVPRW_2022_paper.pdf](https://openaccess.thecvf.com/content/CVPR2022W/AICity/papers/Li_Multi-Camera_Vehicle_Tracking_System_for_AI_City_Challenge_2022_CVPRW_2022_paper.pdf)

# Revisions

Address previous comments by adding CAD schematics of cameras, more in-depth analysis of required field-of-view, re-scoping of this detailed design to just camera selection
