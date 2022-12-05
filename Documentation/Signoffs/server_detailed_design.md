# Detailed Design for Hardware of Server

## Function of the Subsystem
The server can be likened to the heart of the entire parking lot monitoring system, in which the server receives input data from the sensors, processes the data, and then send the data to be stored in a Firebase remote server. The server communicates with the Primary and Secondary Data Acquisition Systems, and it will have an AI application to process images from the Primary Data Acquisition System cameras to determine the number of cars in the parking lot. The server will also have a program to store the count from the road tubes in the Secondary Data Acquisition system, determine the accuracy of the counts between the Primary and Secondary systems, and calculate parking histories and averages.

## Constraints

Many of these constraints were determined by researching the hardware needed for a full-scale surveillance system with 7 cameras (which will constantly provide video feed). However, a surveillance system (an ideal) requires much more than what we need, so we will not need that high of performance constraints for our system to function properly and efficiently.

1. CPU
  * The processor must be powerful enough to perform tasks such as determining the number of vehicles present in a parking lot via AI analyzing images sampled from multiple cameras and via keeping track of counts from road tubes and compiling statistical data and history about parking availability. For a surveillance system, it is recommended to have one thread per camera, which for this system means 7 threads (which can be provided in 4 double-threaded cores). Thus, the CPU needs at least 6 double-threaded cores which allows half of the threads to be devoted to obtaining images from the cameras and the other half for processing the images, processing road tube counts, and sending the processed data to the server. For live streaming applications, a frequency of 3.0 GHz is required for 1080p streaming (1080p is the intended resolution of the camera feeds) [1].

2. GPU
  * Because we are not live streaming for display on a screen, but rather collecting images and processing them on a server, the GPU does not need a lot of VRAM. Thus, 4 GB of VRAM would be sufficient for the server’s purposes.

3. RAM
  * It is recommended to have at least 4 GB RAM to run the OpenCV AI library [2]. In addition, for a surveillance system, 16 GB of RAM is recommended for 8-10 cameras [3]. However, because we are not live streaming, 16 GB should be sufficient for image collection and processing using the OpenCV AI library.

4. Storage
  * For the storage, two different storage drives are needed to ensure the highest efficiency when storing collected data and system data. A small SSD (128 GB) shall be used to store the boot of OS, which has been determined to be Linux, to increase the speed of the server. This is considered good practice for PCs/servers. In addition, since no images are being stored on the server, the server does not need a lot of storage, so 2 TB should be sufficient.

5. Power Supply
  * Since this server will be running 24/7, the Power Supply will need to be at minimum an 80 Plus Gold Rating, which is considered a sweet spot for price-performance (i.e. most cost-effective) [4]. Also, the power supply should be able to supply at least the estimated wattage of all the parts, as determined when entering the selected parts in PCPartPicker [5]. The power supply will also need to be suitable to be plugged into a typical American wall outlet with 120 V. The power supply should also have a high mean time between failures (MTBF) since this server is to be built as if it were to run for years without failure.

6. Motherboard
  * The motherboard must be able to fit the CPU, GPU, RAM, storage drives, and Wi-Fi adapter. The motherboard must be compatible with the CPU processor (i.e. supports AMD if an AMD processor is used), and the socket must be up-to-date with other current popular models (i.e. AM4). Ideally the size of the motherboard should be ATX so that the server could be easily built without worrying about size constraints. The motherboard could have an embedded LAN chip for Wi-Fi; however, this is not required, as long as the motherboard is able to have a Wi-Fi adapter attached.

7. Case
  * The case must be able to house the CPU, GPU, RAM, storage drives, Wi-Fi adapter, and cooler for the CPU. The case must also have or be able to have at least 2 or 3 fans as well as good filters so that the entire server could have proper airflow and could prevent accumulation of dust.

8. Wi-Fi Adapter
  * Because the system will have to communicate wirelessly via Wi-Fi with the cameras, sign, and mobile application, a Wi-Fi adapter is needed. The server needs to be able to obtain images from the cameras of the Primary Data Acquisition System and vehicle counts from the road tubes of the Secondary Data Acquisition System. In addition, the server needs to be able to output the current available parking count (processed data) to the remote Firebase server and to the outdoor signage. All of the hardware will not be physically connected to the server, hence the server’s needs for wireless communication via Wi-Fi.
  * Because the server will be connected to cameras, the current cameras that have been selected to be used to implement the Primary Data Acquisition System have a resolution of 1080p (active pixels are 1920 x 1080) and a frame rate of 30 fps, which imputes a minimum bit rate of 4541 kbps (kbits/s), or 4.541 Mbps (Mbits/s) [6]. Because at least a 30-40% buffer is ideal to have to account for fluctuations in upload speeds since the server will be receiving data constantly [7], at least 6.3 Mbps should be accounted for per camera, meaning that for a 7-camera system, a minimum bit rate of 44.1 Mbps is required.

9. CPU Cooler
  * Since the server will be running 24/7 and will be doing very heavy computations due to the number of video feeds being inputted and the amount of processing required for the AI algorithm and the mobile application queries, to prevent the CPU from overheating, a cooling mechanism is needed. The CPU cooler must be able to be fitted into the case.

## Buildable Schematic

![Figure 1. Server Components within Case](../3D&#32;Models/Server.jpg)
<div align="center"> Figure 1. Server Components within Case
<div align="left">

## Analysis

When selecting these parts, these parts were entered into PCPartPicker to ensure all parts listed below are compatible.

1. CPU
  * Selected Part: AMD Ryzen 5 3600 6-Core, 12-Thread Unlocked Desktop Processor with Wraith Stealth Cooler
    - The AMD Ryzen 5 3600 meets the specifications listed above. This CPU has 6 cores and 12 threads, a base clock frequency of 3.6 GHz, a maximum frequency of 4.2 GHz, and a maximum frequency of 4.6 GHz.
    - Purchasing this CPU from Amazon comes with its own cooling unit.

2. GPU
  * Selected Part: GIGABYTE GeForce GTX 1630 4GB GDDR6 PCI Express 3.0 x16 ATX Video Card
    - The RTX 3060 GPU meets the specifications listed above. This GPU has 4 GB of GDDR6 RAM, which is enough for the server’s purpose of processing images from 7 cameras.

3. RAM
  * Selected Part: Neo Forza FAYE 16GB (2x8GB) 288-Pin DDR4 3200 (PC4 25600) SDRAM Desktop Memory Model
    - The Neo Forza GB DDR4 RAM meets the specifications listed above. This RAM has 16 GB of RAM, which is enough to handle the image collection and processing from all cameras and the other applications the system will need to perform.

4. Storage
  * Selected Part for Boot Drive: Team Group MP33 M.2 2280 128GB PCIe 3.0 x4 with NVMe 1.3 3D NAND Internal Solid State Drive (SSD)
    - The Team Group SSD meets the specifications listed for the boot drive SSD since it meets the storage requirements of 128 GB.
  * Selected Part for Storage Drive: Seagate BarraCuda 2TB Internal Hard Drive HDD – 3.5 Inch SATA 6Gb/s 7200 RPM 256MB Cache 3.5-Inch
    - The Seagate BarraCuda Hard Drive meets the specifications listed for the storage drive since it has 7200 rpm as well as 2TB for storage.

5. Power Supply
  * Selected Part: Thermaltake Toughpower GX1 80+ Gold 500W SLI/CrossFire Ready Continuous Power ATX 12V V2.4/EPS V2.92 Non Modular Power Supply
    - The Thermaltake Toughpower GX1 Power Supply meets the specifications listed above since the estimated wattage of all of the selected parts according to PCPartPicker is 254 W [5]. This power supply is 500 W and 80 Plus Gold certified, and it has a MTBF of 100,000 hours as well as an input voltage of 100 V to 240 V.

6. Motherboard
  * Selected Part: GIGABYTE B550 GAMING X V2 AM4 AMD B550 SATA 6Gb/s USB 3.0 ATX AMD Motherboard
  * The Gigabyte B550 Motherboard meets the specifications listed above. It is compatible with the AMD 5700X CPU, has an AM4, and is able to have a Wi-Fi adapter be able to be connected. The motherboard is also ATX which also for easy fitting of the parts in the case.

7. Case
  * Selected Part: Corsair 4000D Airflow CC-9011200-WW Black Steel / Plastic / Tempered Glass ATX Mid Tower Computer Case
  * The Corsair 4000D case meets the above specifications by having enough space to fit all components and by having two fans for airflow.

8. Wi-Fi Adapter
  * Selected Part: Wavlink AX3000 Wifi 6 PCIe WiFi Card Bluetooth 5.2 Tri-band 2.4G/5G/6G Network Card 802.11ax,Up to 3000Mbps WiFi Network Card with MU-MIMO, OFDMA, Heat Sink, for Desktop PC Support Windows 11,10 64bit
  * The Wavlink AX3000 Wi-Fi Adapter meets the above specifications since it can accommodate up to 3000 Mbps.

9. CPU Cooler
  * The AMD Ryzen 5 3600 Processor comes with its own Wraith Stealth Cooler which fits over the CPU.

## BOM

| Name of Item | Description | Used in which subsystem(s) | Part Number | Manufacturer | Quantity | Unit Price | Total |
| ------------ | ----------- | -------------------------- | ----------- | ------------ | -------- | ---------- | ----- |
| AMD Ryzen 5 3600 Processor | 6-Core, 12-Thread Unlocked Desktop Processor with Wraith Stealth Cooler | Server | 100-100000031BOX | AMD | 1 | $114.75 | $114.75 |
| GIGABYTE GeForce GTX 1630 Video Card | 4GB GDDR6 PCI Express 3.0 x16 ATX GPU | Server | GV-N1630OC-4GD | NVIDIA | 1 | $139.00 | $139.00 |
| Neo Forza FAYE 16GB (2x8GB) SDRAM Desktop Memory Model |  288-Pin DDR4 3200 (PC4 25600) Desktop Memory Model | Server | NMUD480E82-3200DG20 | Neo Forza | 1 | $42.99 | $42.99 |
| Team Group 128GB SSD | MP33 M.2 2280 128GB PCIe 3.0 x4 with NVMe 1.3 3D NAND Internal SSD | Server | TM8FP6128G0C101 | Team Group | 1 | $20.99 | $20.99 |
| Seagate BarraCuda 2TB Internal Hard Drive |  3.5 Inch SATA 6Gb/s 7200 RPM 256MB Cache 3.5-Inch HDD | Server | ST2000DM008 | Seagate | 1 | $46.00 | $46.00 |
| Thermaltake Toughpower GX1 80+ Gold 500W Power Supply | 500W SLI/CrossFire Ready Continuous Non Modular Power Supply | Server | PS-TPD-0500Nnfagu-1 | Corsair | 1 | $59.99 | $59.99 |
| GIGABYTE B550 GAMING X V2 ATX AMD Motherboard | AM4 AMD B550 SATA 6Gb/s USB 3.0 Motherboard | Server | B550 | Gigabyte | 1 | $129.99 | $129.99 |
| Corsair 4000D ATX Mid Tower Computer Case | Airflow Black Steel / Plastic / Tempered Glass Case | Server | CC-9011200-WW | Corsair | 1 | $104.99 | $104.99 |
| Wavlink AX3000 WiFi Network Card |Wifi 6 PCIe WiFi Card Bluetooth 5.2 Tri-band 2.4G/5G/6G Network Card 802.11ax,Up to 3000Mbps with MU-MIMO, OFDMA, Heat Sink, for Desktop PC Support Windows 11,10 64bit Wi-Fi Adapter | Server | 675X2 | Wavlink | 1 | $32.99 | $32.99 |
| | | | | | | | **$571.44** |

## Links to Purchase Parts

AMD Ryzen 5 3600 CPU:
[https://www.amazon.com/AMD-Ryzen-3600-12-Thread-Processor/dp/B07STGGQ18/ref=asc_df_B07STGGQ18/?tag=&linkCode=df0&hvadid=366315306136&hvpos=&hvnetw=g&hvrand=13518499605173326940&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1025954&hvtargid=pla-784457979043&ref=&adgrpid=75347436639&th=1](https://www.amazon.com/AMD-Ryzen-3600-12-Thread-Processor/dp/B07STGGQ18/ref=asc_df_B07STGGQ18/?tag=&linkCode=df0&hvadid=366315306136&hvpos=&hvnetw=g&hvrand=13518499605173326940&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1025954&hvtargid=pla-784457979043&ref=&adgrpid=75347436639&th=1)

GIGABYTE GeForce GTX 1630 4GB Video Card: [https://www.newegg.com/gigabyte-geforce-gtx-1630-gv-n1630oc-4gd/p/N82E16814932548?Item=N82E16814932548&Source=socialshare&cm_mmc=snc-social-_-sr-_-14-932-548-_-12042022](https://www.newegg.com/gigabyte-geforce-gtx-1630-gv-n1630oc-4gd/p/N82E16814932548?Item=N82E16814932548&Source=socialshare&cm_mmc=snc-social-_-sr-_-14-932-548-_-12042022)

Neo Forza FAYE 16GB (2x8GB) SDRAM Desktop Memory Model: [https://www.newegg.com/neo-forza-16gb-288-pin-ddr4-sdram/p/0RN-0097-00019](https://www.newegg.com/neo-forza-16gb-288-pin-ddr4-sdram/p/0RN-0097-00019)

Team Group 128GB M.2 SSD: [https://www.newegg.com/team-group-mp33-128gb/p/N82E16820331414?Description=m.2%20ssd%20128%20gb&cm_re=m.2_ssd%20128%20gb-_-20-331-414-_-Product](https://www.newegg.com/team-group-mp33-128gb/p/N82E16820331414?Description=m.2%20ssd%20128%20gb&cm_re=m.2_ssd%20128%20gb-_-20-331-414-_-Product)

Seagate BarraCuda 2TB Internal Hard Drive: [https://www.amazon.com/Seagate-BarraCuda-Internal-Drive-3-5-Inch/dp/B07H2RR55Q/ref=asc_df_B07H2RR55Q/?tag=hyprod-20&linkCode=df0&hvadid=319972287270&hvpos=&hvnetw=g&hvrand=9119350792040813109&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1025954&hvtargid=pla-613251472056&th=1](https://www.amazon.com/Seagate-BarraCuda-Internal-Drive-3-5-Inch/dp/B07H2RR55Q/ref=asc_df_B07H2RR55Q/?tag=hyprod-20&linkCode=df0&hvadid=319972287270&hvpos=&hvnetw=g&hvrand=9119350792040813109&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1025954&hvtargid=pla-613251472056&th=1)

Thermaltake Toughpower GX1 80+ Gold 500W Power Supply: [https://www.amazon.com/dp/B07LGMXWP3?tag=pcpapi-20&linkCode=ogi&th=1](https://www.amazon.com/dp/B07LGMXWP3?tag=pcpapi-20&linkCode=ogi&th=1)

GIGABYTE B550 ATX AMD Motherboard: [https://www.newegg.com/gigabyte-b550-gaming-x-v2/p/N82E16813145255?Description=GIGABYTE%20B550%20GAMING%20X%20V2%20AM4%20AMD%20B550%20SATA%206Gb/s%20USB%203.0%20ATX%20AMD%20Motherboard&cm_re=GIGABYTE_B550%20GAMING%20X%20V2%20AM4%20AMD%20B550%20SATA%206Gb/s%20USB%203.0%20ATX%20AMD%20Motherboard-_-13-145-255-_-Product&quicklink=true](https://www.newegg.com/gigabyte-b550-gaming-x-v2/p/N82E16813145255?Description=GIGABYTE%20B550%20GAMING%20X%20V2%20AM4%20AMD%20B550%20SATA%206Gb/s%20USB%203.0%20ATX%20AMD%20Motherboard&cm_re=GIGABYTE_B550%20GAMING%20X%20V2%20AM4%20AMD%20B550%20SATA%206Gb/s%20USB%203.0%20ATX%20AMD%20Motherboard-_-13-145-255-_-Product&quicklink=true)

Corsair 4000D ATX Mid Tower Computer Case: [https://www.newegg.com/black-corsair-4000d-airflow-atx-mid-tower/p/N82E16811139156](https://www.newegg.com/black-corsair-4000d-airflow-atx-mid-tower/p/N82E16811139156)

Wavlink AX3000 Wifi Network Card: [https://www.newegg.com/wavlink-690a5d-usb-3-0/p/0XM-00B5-00053?Description=wifi%20adapter&cm_re=wifi_adapter-_-0XM-00B5-00053-_-Product&quicklink=true](https://www.newegg.com/wavlink-690a5d-usb-3-0/p/0XM-00B5-00053?Description=wifi%20adapter&cm_re=wifi_adapter-_-0XM-00B5-00053-_-Product&quicklink=true)


## Cited Sources

[1] P. Richards, “What Type of Computer Do I Need to Live Stream?,” _StreamGeeks_, 24 Mar. 2021. [https://streamgeeks.us/what-computer-do-i-need-to-live-stream/.](https://streamgeeks.us/what-computer-do-i-need-to-live-stream/)

[2] A. Sharma, V. R. Shrimali, M. Beyeler, “Technical requirements,” _Machine Learning for OpenCV_, 2nd ed., _Packet Publishing Ltd._, Birmingham, UK, Sept. 2019. [https://www.oreilly.com/library/view/machine-learning-for/9781789536300/038d70bd-e186-483b-8ef0-23b344f46ecc.xhtml](https://www.oreilly.com/library/view/machine-learning-for/9781789536300/038d70bd-e186-483b-8ef0-23b344f46ecc.xhtml).

[3] NeuroTechnology, “SentiVeillance SDK,”  _NeuroTechnology_, 2022. [https://www.sentiveillance.com/sentiveillance-sdk/](https://www.sentiveillance.com/sentiveillance-sdk/).

[4] J. Fox, “80 PLUS Bronze vs Gold vs Platinum vs Titanium: Which PSU Rating do you Need?,” _TechGuided.com_, 13 Jun. 2022. [https://techguided.com/80-plus-bronze-vs-gold-vs-platinum-vs-titanium-which-psu-rating-do-you-need/](https://techguided.com/80-plus-bronze-vs-gold-vs-platinum-vs-titanium-which-psu-rating-do-you-need/).

[5] PCPartPicker, “Choose Your Parts,” _PCPartPicker_, 2022. [https://pcpartpicker.com/list/](https://pcpartpicker.com/list/).

[6] “Omni Calculator,” [https://www.omnicalculator.com/other/streaming-bitrate](https://www.omnicalculator.com/other/streaming-bitrate).

[7] Restream Team, “What is a good upload speed for streaming?,” _Restream, Inc._, 1 Jul. 2022, [https://restream.io/blog/what-is-a-good-upload-speed-for-streaming/](https://restream.io/blog/what-is-a-good-upload-speed-for-streaming/).


## Revisions

12/4/2022 - Downscaled components to cut costs
