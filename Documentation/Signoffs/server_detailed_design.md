# Detailed Design for Hardware of Server

## Big Picture
The server can be likened to the heart of the entire parking lot monitoring system, in which the server receives input data from the sensors, processes and stores it, and then outputs them to the sign and the mobile application. The server communicates with the other subsystems as well as processes the data from the sensors so that it could be meaningful for students who use the mobile application and view the sign.

## Specifications
1. CPU
  * The processor must be powerful enough to perform tasks such as determining the number of vehicles present in a parking lot via AI analyzing feed from multiple cameras and via keeping track of counts from road tubes, compiling statistical data and history about parking availability, and hosting a HTTP website for the mobile application. Thus, the CPU needs at least 8 cores with double threads so that 4 cores could be allocated to receiving video feeds (1 core per 2 cameras, which makes 1 thread per camera). Thus, the other 4 cores could be used for the other functions such as processing mobile application queries, sending data to the mobile app and sign, etc. For live streaming applications, a minimum of an i7 processor at 3.0 GHz is required for 1080p streaming (1080p is the intended resolution of the camera feeds) [1]. A high frequency for the CPU is needed due to the desired specification that the mobile application and sign updates at a maximum rate of every minute. The CPU will also need to have ECC support to ensure data integrity (see RAM). The CPU must also support DD4 RAM.

2. GPU
  * For live streaming, a GPU card with 4-8 GB of VRAM can handle up to 4 1080p cameras while a GPU card with 8-12 GB of VRAM can handle up to 6 4K cameras [1]. Thus, since 7 1080p cameras are being used, roughly 8-12 GB of VRAM is needed to handle the cameras as well as the other applications of the system.

3. RAM
  * It is recommended to have at least 4 GB RAM to run the OpenCV AI library [2]. In addition, 1-4 cameras at 1080p setup for streaming requires roughly 8-16 GB of DRAM while using more 1080p cameras or multiple 4K cameras requires roughly 16-32 GB of DRAM [1]. For home security surveillance systems, it is recommended to allocate about 2-3 GB of RAM per camera [3]. For the SentiVeillance surveillance software development kit, 16 GB of RAM is recommended for 8-10 cameras [4]. Thus, it can be safe to say that at least 16 GB is required for the cameras alone while another 16 GB is needed for the rest of the system processes (including running OpenCV), thus bringing the RAM requirement up to 32 GB. DDR4 (or above) should be used due to its energy efficiency. Also, due to the nature of the data being transmitted (having a very wrong number of available parking spots in a lot could cause more traffic than ideal, for example), and how numerous cameras are transmitting data to the server, the integrity of the data is critical, which is why ECC is desired in a RAM stick.

4. Storage
  * For the storage, two different storage drives are needed to ensure the highest efficiency when storing collected data and system data. A small SSD (128 GB) shall be used to store the boot of OS, which has been determined to be Linux, to increase the speed of the server. Since no images are being stored, only vehicle count data (which does not require as much as space as images), multiple SSDs that add up to more than 4 TB or a hard drive with at least 7200 rpm (the standard rpm for desktop hard drives) and at least 4 TB space would be plenty to store data for multiple years.

5. Power Supply
  * Since this server will be running 24/7, the Power Supply will need to be at minimum an 80 Plus Gold Rating, which is considered a sweet spot for price-performance (i.e. most cost-effective) [5]. Also, the power supply should be able to supply at least the estimated wattage of all the parts, as determined when entering the selected parts in PCPartPicker [6]. The power supply will also need to be suitable to be plugged into a typical American wall outlet with 120 V. The power supply should also have a high mean time between failures (MTBF) since this server is to be built as if it were to run for years without failure.

6. Motherboard
  * The motherboard must be able to fit the CPU, GPU, RAM, storage drives, and Wi-Fi adapter. The motherboard must be compatible with the CPU processor (i.e. supports AMD if an AMD processor is used), and the socket must be up-to-date with other current popular models (i.e. AM4). Ideally the size of the motherboard should be ATX so that the server could be easily built without worrying about size constraints. The motherboard could have an embedded LAN chip for Wi-Fi; however, this is not required, as long as the motherboard is able to have a Wi-Fi adapter attached. The motherboard must also be ECC compatible.

7. Case
  * The case must be able to house the CPU, GPU, RAM, storage drives, wi-fi adapter, and cooler for the CPU. The case must also have or be able to have at least 2 or 3 fans as well as good filters so that the entire server could have proper airflow and could prevent accumulation of dust.

8. Wi-Fi Adapter
  * Because the system will have to communicate wirelessly via Wi-Fi with the cameras, sign, and mobile application, a Wi-Fi adapter is needed. The server needs to be able to obtain video feed from the cameras of the Primary Data Acquisition System, vehicle counts from the road tubes of the Secondary Data Acquisition System, local weather information for Cookeville, TN, from an online source/local station, and data requests from the mobile application. In addition, the server needs to be able to output the current available parking count to the outdoor signage and requested data and notifications to the mobile application. All of the hardware will not be physically connected to the server, hence the server’s needs for wireless communication via Wi-Fi.
  * Because the server will be connected to cameras, the current cameras that have been selected to be used to implement the Primary Data Acquisition System have a resolution of 1080p (active pixels are 1920 x 1080) and a frame rate of 30 fps, which imputes a minimum bit rate of 4541 kbps (kbits/s), or 4.541 Mbps (Mbits/s) [7]. Because at least a 30-40% buffer is ideal to have to account for fluctuations in upload speeds since the server will be receiving data constantly [8], at least 6.3 Mbps should be accounted for per camera, meaning that for a 7-camera system, a minimum bit rate of 44.1 Mbps is required.

9. CPU Cooler
  * Since the server will be running 24/7 and will be doing very heavy computations due to the number of video feeds being inputted and the amount of processing required for the AI algorithm and the mobile application queries, to prevent the CPU from overheating, a cooling mechanism is needed. The CPU cooler must be able to be fitted into the case.

## Buildable PDF Schematic

[Server Components] (../3D%Models/Server.pdf)

## Analysis
1. CPU
  * Selected Part: AMD Ryzen 7 5700X - Ryzen 7 5000 Series 8-Core Socket AM4 65W Desktop Processor
    - The AMD Ryzen 7 5700X meets the specifications listed above. This CPU has 8 cores, a frequency of 3.4 GHz, a maximum frequency of 4.6 GHz, and DDR4 and ECC compatibility [9].

2. GPU
  * Selected Part: GIGABYTE Vision GeForce RTX 3060 12GB GDDR6 PCI Express 4.0 ATX Video Card
    - The RTX 3060 GPU meets the specifications listed above. This GPU has 12 GB of GDDR6 RAM, which is enough to handle the amount of cameras to be connected to this server.

3. RAM
  * Selected Part: Kingston 32GB DDR4 3200Mhz CL22 2Rx8 ECC Unbuffered Memory RAM DIMM Module
    - The Kingston 32GB DDR4 RAM meets the specifications listed above. This RAM has 32 GB of RAM, which is enough to handle the streaming from all cameras and the other applications the system will need to perform. This RAM is DDR4 and has ECC, which will ensure data integrity.

4. Storage
  * Selected Part for Boot Drive: Team Group MP33 M.2 2280 128GB PCIe 3.0 x4 with NVMe 1.3 3D NAND Internal Solid State Drive (SSD)
    - The Team Group SSD meets the specifications listed for the boot drive SSD since it meets the storage requirements of 128 GB.
  * Selected Part for Storage Drive: Seagate IronWolf Pro 8TB NAS Hard Drive 7200 RPM 256MB Cache CMR SATA 6.0Gb/s 3.5" Internal HDD
    - The Seagate IronWolf Pro Hard Drive meets the specifications listed for the storage drive since it has 7200 rpm as well as 8 TB for years of storage.

5. Power Supply
  * Selected Part: CORSAIR RMx Series (2021) RM750x CP-9020199-NA 750 W ATX12V / EPS12V 80 PLUS GOLD Certified Full Modular Power Supply
    - The CORSAIR RM750x Power Supply meets the specifications listed above, for it is 750 W as well as 80 Plus Gold certified with a MTBF of 100,000 hours.

6. Motherboard
  * Selected Part: GIGABYTE B550 GAMING X V2 AM4 AMD B550 SATA 6Gb/s USB 3.0 ATX AMD Motherboard
  * The Gigabyte B550 Motherboard meets the specifications listed above. It is compatible with the AMD 5700X CPU, is ECC compatible, has an AM4, and is able to have a Wi-Fi adapter be able to be connected. The motherboard is also ATX which also for easy fitting of the parts in the case.

7. Case
  * Selected Part: Corsair 4000D Airflow CC-9011200-WW Black Steel / Plastic / Tempered Glass ATX Mid Tower Computer Case https://www.newegg.com/black-corsair-4000d-airflow-atx-mid-tower/p/N82E16811139156
  * The Corsair 4000D case meets the above specifications by having enough space to fit all components and by having two fans for airflow.

8. Wi-Fi Adapter
  * Selected Part: Wavlink AX3000 Wifi 6 PCIe WiFi Card Bluetooth 5.2 Tri-band 2.4G/5G/6G Network Card 802.11ax,Up to 3000Mbps WiFi Network Card with MU-MIMO, OFDMA, Heat Sink, for Desktop PC Support Windows 11,10 64bit
  * The Wavlink AX3000 Wi-Fi Adapter meets the above specifications since it can accommodate up to 3000 Mbps.

9. CPU Cooler
  * Selected Part: Vetroo V5 CPU Air Cooler w/ 5 Heat Pipes 120mm PWM Processor 150W TDP Cooler for Intel LGA 1700/1200/115X AMD AM5/AM4 w/Addressable RGB Lights Sync
  * The CPU cooler meets the above specifications by being able to fit into the case.

## BOM

| Name of Item | Description | Used in which subsystem(s) | Part Number | Manufacturer | Quantity | Unit Price | Total |
| ------------ | ----------- | -------------------------- | ----------- | ------------ | -------- | ---------- | ----- |
| AMD Ryzen 7 5700X Processor | Ryzen 7 5000 Series 8-Core Socket AM4 65W Desktop Processor | Server | 100-100000926WOF | AMD | 1 | $239.00 | $239.00 |
| GIGABYTE Vision GeForce RTX 3060 Video Card | 12GB GDDR6 PCI Express 4.0 ATX GPU | Server | GV-N3060VISION OC-12GD | NVIDIA | 1 | $279.00 | $279.00 |
| Kingston 32GB DDR4 RAM DIMM Module | 3200Mhz CL22 2Rx8 ECC Unbuffered Memory | Server | KSM32ED8/32ME | Kingston | 1 | $142.99 | $142.99 |
| Team Group 128GB SSD | MP33 M.2 2280 128GB PCIe 3.0 x4 with NVMe 1.3 3D NAND Internal SSD | Server | TM8FP6128G0C101 | Team Group | 1 | $17.99 | $17.99 |
| Seagate IronWolf Pro 8TB NAS Hard Drive | 7200 RPM 256MB Cache CMR SATA 6.0Gb/s 3.5" Internal HDD | Server | ST8000NE001 | Seagate | 1 | $169.98 | $169.98 |
| CORSAIR RMx Series (2021) RM750x 80 PLUS GOLD Certified Power Supply | 750 W ATX12V / EPS12V Full Modular Power Supply | Server | CP-9020199-NA | Corsair | 1 | $99.99 | $99.99 |
| GIGABYTE B550 GAMING X V2 ATX AMD Motherboard | AM4 AMD B550 SATA 6Gb/s USB 3.0 Motherboard | Server | B550 | Gigabyte | 1 | $178.00 | $178.00 |
| Corsair 4000D ATX Mid Tower Computer Case | Airflow Black Steel / Plastic / Tempered Glass Case | Server | CC-9011200-WW | Corsair | 1 | $89.99 | $89.99 |
| Wavlink AX3000 WiFi Network Card |Wifi 6 PCIe WiFi Card Bluetooth 5.2 Tri-band 2.4G/5G/6G Network Card 802.11ax,Up to 3000Mbps with MU-MIMO, OFDMA, Heat Sink, for Desktop PC Support Windows 11,10 64bit Wi-Fi Adapter | Server | 675X2 | Wavlink | 1 | $29.99 | $29.99 |
| Vetroo V5 CPU Air Cooler | Air Cooler with 5 Heat Pipes 120mm PWM Processor 150W TDP Cooler for Intel LGA 1700/1200/115X AMD AM5/AM4 w/Addressable RGB Lights Sync | Server | V5 | Vetroo | 1 | $34.99 | $34.99 |
| | | | | | | | **$1281.92** |

## Links to Purchase Parts

AMD Ryzen 7 5700X CPU:
[https://www.bestbuy.com/site/amd-ryzen-7-5700x-w-o-fan-black/6510770.p?skuId=6510770](https://www.bestbuy.com/site/amd-ryzen-7-5700x-w-o-fan-black/6510770.p?skuId=6510770)

GIGABYTE Vision GeForce RTX 3060 Video Card: [https://www.newegg.com/gigabyte-geforce-rtx-3060-gv-n3060vision-oc-12gd/p/N82E16814932482R?Description=rtx%203060&cm_re=rtx_3060-_-14-932-482R-_-Product](https://www.newegg.com/gigabyte-geforce-rtx-3060-gv-n3060vision-oc-12gd/p/N82E16814932482R?Description=rtx%203060&cm_re=rtx_3060-_-14-932-482R-_-Product )

RAM - Kingston 32GB DDR4 RAM DIMM Module: [https://www.newegg.com/kingston-32gb-288-pin-ddr4-sdram/p/1B4-00M4-003X5](https://www.newegg.com/kingston-32gb-288-pin-ddr4-sdram/p/1B4-00M4-003X5)

Team Group 128GB M.2 SSD: [https://www.newegg.com/team-group-mp33-128gb/p/N82E16820331414?Description=m.2%20ssd%20128%20gb&cm_re=m.2_ssd%20128%20gb-_-20-331-414-_-Product](https://www.newegg.com/team-group-mp33-128gb/p/N82E16820331414?Description=m.2%20ssd%20128%20gb&cm_re=m.2_ssd%20128%20gb-_-20-331-414-_-Product)

Seagate IronWolf Pro 8TB NAS Hard Drive: [https://www.newegg.com/seagate-ironwolf-pro-st8000ne001-8tb/p/N82E16822184795?Description=hard%20drive%207200%20rpm&cm_re=hard_drive%207200%20rpm-_-22-184-795-_-Product](https://www.newegg.com/seagate-ironwolf-pro-st8000ne001-8tb/p/N82E16822184795?Description=hard%20drive%207200%20rpm&cm_re=hard_drive%207200%20rpm-_-22-184-795-_-Product)

CORSAIR RMx Series (2021) RM750x 80 PLUS GOLD Certified Power Supply: [https://www.corsair.com/us/en/Categories/Products/Power-Supply-Units/RMx-Series/p/CP-9020199-NA?utm_source=PCPartPicker_79301&utm_medium=Affiliate&utm_campaign=497986_CORSAIR%20US%20Product%20Catalog%20Ad&utm_content=Corsair&clickid=0NzSTu38HxyNT6eyCsW-kVVqUkA0omQIK0d8xo0&utm_coupon=Content&irgwc=1](https://www.corsair.com/us/en/Categories/Products/Power-Supply-Units/RMx-Series/p/CP-9020199-NA?utm_source=PCPartPicker_79301&utm_medium=Affiliate&utm_campaign=497986_CORSAIR%20US%20Product%20Catalog%20Ad&utm_content=Corsair&clickid=0NzSTu38HxyNT6eyCsW-kVVqUkA0omQIK0d8xo0&utm_coupon=Content&irgwc=1)

GIGABYTE B550 ATX AMD Motherboard: [https://www.amazon.com/Gigabyte-B550-Gaming-Ryzen-Motherboard/dp/B08LGKGBKT/ref=asc_df_B08LGKGBKT/?tag=hyprod-20&linkCode=df0&hvadid=475789631743&hvpos=&hvnetw=g&hvrand=14935087167591533577&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9013566&hvtargid=pla-1224022204512&th=1](https://www.amazon.com/Gigabyte-B550-Gaming-Ryzen-Motherboard/dp/B08LGKGBKT/ref=asc_df_B08LGKGBKT/?tag=hyprod-20&linkCode=df0&hvadid=475789631743&hvpos=&hvnetw=g&hvrand=14935087167591533577&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9013566&hvtargid=pla-1224022204512&th=1)

Corsair 4000D ATX Mid Tower Computer Case: [https://www.newegg.com/black-corsair-4000d-airflow-atx-mid-tower/p/N82E16811139156](https://www.newegg.com/black-corsair-4000d-airflow-atx-mid-tower/p/N82E16811139156)

Wavlink AX3000 Wifi Network Card: [https://www.newegg.com/wavlink-690a5d-usb-3-0/p/0XM-00B5-00053?Description=wifi%20adapter&cm_re=wifi_adapter-_-0XM-00B5-00053-_-Product&quicklink=true](https://www.newegg.com/wavlink-690a5d-usb-3-0/p/0XM-00B5-00053?Description=wifi%20adapter&cm_re=wifi_adapter-_-0XM-00B5-00053-_-Product&quicklink=true)

Vetroo V5 CPU Air Cooler: [https://www.newegg.com/vetroo-v5/p/13C-00F3-00002?Item=9SIAPNCBP46768&Description=amd%20cpu%20cooler&cm_re=amd_cpu%20cooler-_-9SIAPNCBP46768-_-Product&cm_sp=SP-_-974390-_-0-_-1-_-9SIAPNCBP46768-_-amd%20cpu%20cooler-_-cooler|cpu-_-1](https://www.newegg.com/vetroo-v5/p/13C-00F3-00002?Item=9SIAPNCBP46768&Description=amd%20cpu%20cooler&cm_re=amd_cpu%20cooler-_-9SIAPNCBP46768-_-Product&cm_sp=SP-_-974390-_-0-_-1-_-9SIAPNCBP46768-_-amd%20cpu%20cooler-_-cooler|cpu-_-1)

## Cited Sources

[1] P. Richards, “What Type of Computer Do I Need to Live Stream?,” _StreamGeeks_, 24 Mar. 2021. [https://streamgeeks.us/what-computer-do-i-need-to-live-stream/.](https://streamgeeks.us/what-computer-do-i-need-to-live-stream/)

[2] A. Sharma, V. R. Shrimali, M. Beyeler, “Technical requirements,” _Machine Learning for OpenCV_, 2nd ed., _Packet Publishing Ltd._, Birmingham, UK, Sept. 2019. [https://www.oreilly.com/library/view/machine-learning-for/9781789536300/038d70bd-e186-483b-8ef0-23b344f46ecc.xhtml](https://www.oreilly.com/library/view/machine-learning-for/9781789536300/038d70bd-e186-483b-8ef0-23b344f46ecc.xhtml).

[3] Online Forum. “Hardware recommendation, 10 to 15 cameras, 5mp,” _ZoneMinder Forums), 12 Dec. 2021. [https://forums.zoneminder.com/viewtopic.php?t=31384](https://forums.zoneminder.com/viewtopic.php?t=31384).

[4] NeuroTechnology, “SentiVeillance SDK,”  _NeuroTechnology_, 2022. [https://www.sentiveillance.com/sentiveillance-sdk/](https://www.sentiveillance.com/sentiveillance-sdk/).

[5] J. Fox, “80 PLUS Bronze vs Gold vs Platinum vs Titanium: Which PSU Rating do you Need?,” _TechGuided.com_, 13 Jun. 2022. [https://techguided.com/80-plus-bronze-vs-gold-vs-platinum-vs-titanium-which-psu-rating-do-you-need/](https://techguided.com/80-plus-bronze-vs-gold-vs-platinum-vs-titanium-which-psu-rating-do-you-need/).

[6] PCPartPicker, “Choose Your Parts,” _PCPartPicker_, 2022. [https://pcpartpicker.com/list/](https://pcpartpicker.com/list/).

[7] “Omni Calculator,” [https://www.omnicalculator.com/other/streaming-bitrate](https://www.omnicalculator.com/other/streaming-bitrate).

[8] Restream Team, “What is a good upload speed for streaming?,” _Restream, Inc._, 1 Jul. 2022, [https://restream.io/blog/what-is-a-good-upload-speed-for-streaming/](https://restream.io/blog/what-is-a-good-upload-speed-for-streaming/).

[9] “AMD Ryzen 7 5700X specifications,” _CPU-World_, 15 Nov. 2022. [https://www.cpu-world.com/CPUs/Zen/AMD-Ryzen%207%205700X.html](https://www.cpu-world.com/CPUs/Zen/AMD-Ryzen%207%205700X.html).

## Revisions
