# Detailed Design for Hardware of Server

## Function of the Subsystem
The server can be likened to the heart of the entire parking lot monitoring system, in which the server receives input data from the sensors, processes the data, and then send the data to be stored in a Firebase remote server. The server communicates with the Primary and Secondary Data Acquisition Systems, and it will have an AI application to process images from the Primary Data Acquisition System cameras to determine the number of cars in the parking lot. The server will also have a program to store the count from the road tubes in the Secondary Data Acquisition system, determine the accuracy of the counts between the Primary and Secondary systems, and calculate parking histories and averages.

## Constraints

Many of these constraints were determined first by researching the hardware needed for a full-scale surveillance system with 7 cameras (which will constantly provide video feed) and by determining the computational costs and speed to optimally run a computer vision image processing application that is adequate for our needs. However, a surveillance system requires much more processing power than what we need, so a surveillance system is treated as an ideal for our system.

In addition, the server will be designed to use the YOLO object detection algorithm. The YOLO (You-Only-Look-Once) Algorithm is a popular real-time object detection algorithm that is used in vehicle detection applications such as [1]. YOLO is a deep learning-based approach that can predict an object's class/category (what kind of object is it), bounding box (a box that encompasses the object), and probability inside bounding box, for multiple objects in a frame [2]. YOLOv4 is the latest version of the algorithm, featuring many improvements from its predecessor versions. Although YOLO is known for its high performance, it is very resource-intensive since it does run a deep neural network. On an AMD Ryzen 7 CPU on the Windows platform, YOLO only produces an image processing rate of 2.5 fps, but on a Nvidia GPU in the Linux platform, YOLO can process up to 45 fps [1]. Because the mobile application must update data at a minimum of every second (since this rate will provide enough of a real-time feel to users), the 5 cameras that track the statically tracked lots will only have one processed image every minute. For the dynamically tracked lots, since a minimum image rate of 5 fps is needed to capture at least 2 or 3 images to capture a moving car's motion and determine its direction (edge case is a fast-moving car at 25 mph), each of those cameras will send 5 images to the server per second, i.e. every 6th image. Thus, 5 cameras sending 1 image every minute with 2 cameras sending 5 images per second makes a minimum of 15 images to be processed within a second. The YOLO algorithm will be run on the GPU and primarily influence GPU constraints.

There are two frameworks that will either be used to run the YOLO algorithm. The first is OpenCV, which is a free, open-source library for computer vision applications that has been used extensively throughout industry. It is known for its high performance (as compared with other frameworks like TensorFlow) and its extensive documentation, providing a relatively easy learning experience for beginners. The hardware requirements for OpenCV are listed as according to their influence on certain computer parts. OpenCV (3.4.2 at minimum) has options to use enable CUDA for faster YOLO performance with GPU acceleration, though OpenCV is primarily CPU intensive [3]. The other framework is Darknet, which was made specifically for YOLO but runs only on Linux [4]. Darknet can also be used with OpenCV and CUDA dependencies as well. The computer components will be selected based off being able to support either of these frameworks, which should have similar constraints.

The server must also be able to run the Linux operating system due to the versatility of Linux as compared with Windows or MacOS for the needed programming power with the video feeds and AI applications.

1. CPU
  * The processor must be powerful enough to perform tasks such as determining the number of vehicles present in a parking lot via AI analyzing images sampled from multiple cameras and via keeping track of counts from road tubes and compiling statistical data and history about parking availability. For a surveillance system, it is recommended to have one thread per camera, which for this system means 7 threads (which can be provided in 4 double-threaded cores). Thus, the CPU needs at least 6 double-threaded cores which allows half of the threads to be devoted to obtaining images from the cameras and the other half for processing the images, processing road tube counts, and sending the processed data to the server. For live streaming applications, a frequency of 3.0 GHz is required for 1080p streaming (1080p is the intended resolution of the camera feeds) [5].
  * OpenCV can be run a laptop with a processor as "low" as an Intel Core Duo with a frequency of 1.83 Hz paired with 2 GB of RAM [6]. Since the YOLO algorithm will run primarily on the GPU, [6] provides a minimum baseline of what OpenCV needs to run, which is a minimum of 2 cores each with 1 thread. However, [3] tested YOLOv4 with CUDA-enabled OpenCV on a computer with an Intel Core i5 7300HQ CPU and a Nvidia GTX 1050 Ti GPU, and although the i5 7300HQ produced only 2.1 fps, the CPU for our system must match or exceed the performance of this CPU.

2. GPU
  * Since GPUs are typically used for AI/deep learning applications, the GPU will be mainly used to run the computer vision algorithm that processes the images from the cameras.
  * To run the YOLO algorithm, a Nvidia GPU is needed. [3] tested YOLOv4 with CUDA-enabled OpenCV on a computer with an Intel Core i5 7300HQ CPU and a Nvidia GTX 1050 Ti GPU. Running on the i5 7300HQ produced only 2.1 fps whereas the GTX 1050 Ti produced 20.1 fps. Thus, the GPU must match or exceed the performance of a GTX 1050 Ti.

3. RAM
  * It is recommended to have at least 4 GB RAM to run the OpenCV AI library [8]. In addition, for a surveillance system, 16 GB of RAM is recommended for 8-10 cameras [9]. However, because we are not live streaming, 16 GB should be sufficient for image collection and processing using the OpenCV AI library.

4. Storage
  * For the storage, two different storage drives are needed to ensure the highest efficiency when storing collected data and system data. A small SSD (128 GB) shall be used to store the boot of OS, which has been determined to be Linux, to increase the speed of the server. This is considered good practice for PCs/servers. In addition, since no images are being stored on the server, the server does not need a lot of storage, so 2 TB should be sufficient.

5. Power Supply
  * Since this server will be running 24/7, the Power Supply will need to be at minimum an 80 Plus Gold Rating, which is considered a sweet spot for price-performance (i.e. most cost-effective) [10]. Also, the power supply should be able to supply at least the estimated wattage of all the parts, as determined when entering the selected parts in PCPartPicker [11]. The power supply will also need to be suitable to be plugged into a typical American wall outlet with 120 V. The power supply should also have a high mean time between failures (MTBF) since this server is to be built as if it were to run for years without failure.

6. Motherboard
  * The motherboard must be able to fit the CPU, GPU, RAM, storage drives, and Wi-Fi adapter. The motherboard must be compatible with the CPU processor (i.e. supports AMD if an AMD processor is used), and the socket must be up-to-date with other current popular models (i.e. AM4). Ideally the size of the motherboard should be ATX so that the server could be easily built without worrying about size constraints. The motherboard could have an embedded LAN chip for Wi-Fi; however, this is not required, as long as the motherboard is able to have a Wi-Fi adapter attached.

7. Case
  * The case must be able to house the CPU, GPU, RAM, storage drives, Wi-Fi adapter, and cooler for the CPU. The case must also have or be able to have at least 2 or 3 fans as well as good filters so that the entire server could have proper airflow and could prevent accumulation of dust.

8. Wi-Fi Adapter
  * Because the system will have to communicate wirelessly via Wi-Fi with the cameras, sign, and mobile application, a Wi-Fi adapter is needed. The server needs to be able to obtain images from the cameras of the Primary Data Acquisition System and vehicle counts from the road tubes of the Secondary Data Acquisition System. In addition, the server needs to be able to output the current available parking count (processed data) to the remote Firebase server and to the outdoor signage. All of the hardware will not be physically connected to the server, hence the server’s needs for wireless communication via Wi-Fi.
  * Because the server will be connected to cameras, the current cameras that have been selected to be used to implement the Primary Data Acquisition System have a resolution of 1080p (active pixels are 1920 x 1080) and a frame rate of 30 fps, which imputes a minimum bit rate of 4541 kbps (kbits/s), or 4.541 Mbps (Mbits/s) [12]. Because at least a 30-40% buffer is ideal to have to account for fluctuations in upload speeds since the server will be receiving data constantly [13], at least 6.3 Mbps should be accounted for per camera, meaning that for a 7-camera system, a minimum bit rate of 44.1 Mbps is required.

9. CPU Cooler
  * Since the server will be running 24/7 and will be doing very heavy computations due to the number of video feeds being inputted and the amount of processing required for the AI algorithm and the mobile application queries, to prevent the CPU from overheating, a cooling mechanism is needed. The CPU cooler must be able to be fitted into the case.

In addition, all parts must be compatible with each other in terms of socket size, form factor, etc.

## Buildable Schematic

![Figure 1. Server Components within Case](../3D&#32;Models/Server.png)
<div align="center"> Figure 1. Server Components within Case
<div align="left">

## Analysis

When selecting these parts, these parts were entered into PCPartPicker to ensure all parts listed below are compatible, in which the build can be viewed at [11]. Form factors, socket sizes, etc. have been examined to also ensure compatibility.

1. CPU
  * Selected Part: AMD Ryzen 5 3600 6-Core, 12-Thread Unlocked Desktop Processor with Wraith Stealth Cooler
    - The AMD Ryzen 5 3600 meets the specifications listed above. This CPU has 6 cores and 12 threads, a base clock frequency of 3.6 GHz, a maximum frequency of 4.2 GHz, and a maximum frequency of 4.6 GHz.
    - Purchasing this CPU from Amazon comes with its own cooling unit.
    - The AMD Ryzen 5 3600 also has a better performance especially in terms of speed as compared with the Intel i5 7300HQ used as a minimum CPU marker [14].
    - The AMD Ryzen 5 3600 has an AM4 socket size, which matches that of the Gigabyte B550 motherboard.

2. GPU
  * Selected Part: PNY GeForce GTX 1650 4GB GDDR6 Dual Fan Graphics Card
    - The GTX 1650 GPU meets the specifications listed above. This GPU uses NVIDIA Turing architecture.
    - The GTX 1650 also has a better performance especially in terms of speed as compared with the GTX 1050-Ti used as a minimum GPU marker [15].
    - The graphics card requires a PCIe x16 slot to be fitted onto the motherboard, in which the Gigabyte B550 motherboard has two PCIe x16 slots.

3. RAM
  * Selected Part: CORSAIR Vengeance LPX 16GB (2 x 8GB) 288-Pin PC RAM DDR4 3200 (PC4 25600) Desktop Memory Model
    - The Corsair DDR4 RAM meets the specifications listed above. This RAM has 16 GB of RAM, which is enough to handle the image collection and processing from all cameras and the other applications the system will need to perform.
    - The RAM requires DDR4 sockets to be fitted onto the motherboard, and the Gigbayte B550 motherboard does have four DDR4 sockets for both RAM sticks to be inserted in.

4. Storage
  * Selected Part for Boot Drive: Team Group MP33 M.2 2280 128GB PCIe 3.0 x4 with NVMe 1.3 3D NAND Internal Solid State Drive (SSD)
    - The Team Group SSD meets the specifications listed for the boot drive SSD since it meets the storage requirements of 128 GB.
    - The Gigabyte B550 motherboard has an M.2 port for the SSD drive to be fitted onto.
    - The Linux OS software can be loaded onto Team Group 128 GB SSD in the server via a USB flash drive once this computer has been fully built.
  * Selected Part for Storage Drive: Seagate BarraCuda 2TB Internal Hard Drive HDD – 3.5 Inch SATA 6Gb/s 7200 RPM 256MB Cache 3.5-Inch
    - The Seagate BarraCuda Hard Drive meets the specifications listed for the storage drive since it has 7200 rpm as well as 2TB for storage.
    - The Corsair 4000D case has two 3.5 inch HDD trays in which the hard drive can be fitted onto. The second HDD tray also allows for more storage could be added in the future if needed.

5. Power Supply
  * Selected Part: Thermaltake Toughpower GX1 80+ Gold 500W SLI/CrossFire Ready Continuous Power ATX 12V V2.4/EPS V2.92 Non Modular Power Supply
    - The Thermaltake Toughpower GX1 Power Supply meets the specifications listed above since the estimated wattage of all of the selected parts according to PCPartPicker is 254 W [11]. This power supply is 500 W and 80 Plus Gold certified, and it has a MTBF of 100,000 hours as well as an input voltage of 100 V to 240 V.
    - The power supply has an ATX form factor, which is the same as the Corsair case, so the Thermaltake Toughpower GX1 power supply will fit in the Corsair 4000D case. The Gigabyte B550 is also ATX, so the power supply and motherboard are compatible with each other.
    - Buying a power supply comes with all the standard cables needed for completing a computer. This is a standard in power supply packaging.

6. Motherboard
  * Selected Part: GIGABYTE B550 GAMING X V2 AM4 AMD B550 SATA 6Gb/s USB 3.0 ATX AMD Motherboard
    - The Gigabyte B550 Motherboard meets the specifications listed above.
    - The Gigabyte B550 motherboard has an AM4 socket, in which the AMD Ryzen 5 3600 can be inserted onto. The Wraith Stealth CPU cooler is also compatible with AM4.
    - This motherboard also has an ATX form factor, which matches that of the Corsair case and the Thermaltake Toughpower power supply. Thus, the motherboard will fit in the selected case and is compatible with the power supply.
    - It also has three PCIe x1 slots and two PCIe x16 slots, in which the Wavlink Wi-Fi adapter and the GTX 1650 GPU can be inserted into, respectively.
    - It also has four DDR4 sockets which can support both Corsair Vengeance RAM sticks.
    - The motherboard has an M.2 port for the Team Group SSD.

7. Case
  * Selected Part: Corsair 4000D Airflow CC-9011200-WW Black Steel / Plastic / Tempered Glass ATX Mid Tower Computer Case
    - The Corsair 4000D case meets the above specifications by having enough space to fit all components and by having two fans for airflow. The buildable schematic in Figure 1 shows how all of the listed selected parts can fit in this case.
    - The case has an ATX form factor, which matches that of the Gigabyte B550 motherboard and the Thermaltake Toughpower GX1 power supply, which means that the motherboard and the power supply will fit in the case.
    - The case also has two 3.5 inch HDD trays, in which one can house the Seagate BarraCuda hard drive.

8. Wi-Fi Adapter
  * Selected Part: Wavlink AX3000 Wifi 6 PCIe WiFi Card Bluetooth 5.2 Tri-band 2.4G/5G/6G Network Card 802.11ax,Up to 3000Mbps WiFi Network Card with MU-MIMO, OFDMA, Heat Sink, for Desktop PC Support Windows 11,10 64bit
    - The Wavlink AX3000 Wi-Fi Adapter meets the above specifications since it can accommodate up to 3000 Mbps.
    - The Wavlink AX300 Wi-Fi adapter requires a PCIe x1 slot, in which the Gigabyte B550 motherboard has three PCIe x1 slots (two of which will be accessible once the GPU is placed onto the motherboard). It also has a cable that plugs directly into the motherboard for power and data transmission.

9. CPU Cooler
  * Selected Part: Wraith Stealth Cooler
    -  The AMD Ryzen 5 3600 Processor comes with its own Wraith Stealth Cooler which fits over the CPU. The Wraith Stealth Cooler is also compatible with every AM4 motherboard, just like the one selected.

## BOM

| Name of Item | Description | Used in which subsystem(s) | Part Number | Manufacturer | Quantity | Unit Price | Total |
| ------------ | ----------- | -------------------------- | ----------- | ------------ | -------- | ---------- | ----- |
| AMD Ryzen 5 3600 Processor | 6-Core, 12-Thread Unlocked Desktop Processor with Wraith Stealth Cooler | Server | 100-100000031BOX | AMD | 1 | $111.44 | $111.44 |
| PNY GeForce GTX 1650 Graphics Card | 4GB GDDR6 Dual Fan GPU | Server | GV-N1630OC-4GD | PNY | 1 | $189.99 | $189.99 |
| CORSAIR Vengeance LPX 16GB (2 x 8GB) RAM |  288-Pin PC RAM DDR4 3200 (PC4 25600) Desktop Memory Model | Server | CMK16GX4M2B3200C16R | Corsair | 1 | $48.98 | $48.98 |
| Team Group 128GB SSD | MP33 M.2 2280 128GB PCIe 3.0 x4 with NVMe 1.3 3D NAND Internal SSD | Server | TM8FP6128G0C101 | Team Group | 1 | $17.99 | $17.99 |
| Seagate BarraCuda 2TB Internal Hard Drive |  3.5 Inch SATA 6Gb/s 7200 RPM 256MB Cache 3.5-Inch HDD | Server | ST2000DM008 | Seagate | 1 | $49.99 | $49.99 |
| Thermaltake Toughpower GX2 80+ Gold 600W Power Supply | 500W SLI/CrossFire Ready Continuous Non Modular Power Supply | Server | PS-TPD-0500Nnfagu-1 | Thermaltake | 1 | $59.99 | $59.99 |
| GIGABYTE B550 GAMING X V2 ATX AMD Motherboard | AM4 AMD B550 SATA 6Gb/s USB 3.0 Motherboard | Server | B550 | Gigabyte | 1 | $129.99 | $129.99 |
| Corsair 4000D ATX Mid Tower Computer Case | Airflow Black Steel / Plastic / Tempered Glass Case | Server | CC-9011200-WW | Corsair | 1 | $104.99 | $104.99 |
| Wavlink AX3000 WiFi Network Card |Wifi 6 PCIe WiFi Card Bluetooth 5.2 Tri-band 2.4G/5G/6G Network Card 802.11ax,Up to 3000Mbps with MU-MIMO, OFDMA, Heat Sink, for Desktop PC Support Windows 11,10 64bit Wi-Fi Adapter | Server | 675X2 | Wavlink | 1 | $61.99 | $61.99 |
| | | | | | | | **$775.35** |

## Links to Purchase Parts

AMD Ryzen 5 3600 CPU:
[https://www.amazon.com/AMD-Ryzen-3600-12-Thread-Processor/dp/B07STGGQ18/ref=asc_df_B07STGGQ18/?tag=&linkCode=df0&hvadid=366315306136&hvpos=&hvnetw=g&hvrand=13518499605173326940&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1025954&hvtargid=pla-784457979043&ref=&adgrpid=75347436639&th=1](https://www.amazon.com/AMD-Ryzen-3600-12-Thread-Processor/dp/B07STGGQ18/ref=asc_df_B07STGGQ18/?tag=&linkCode=df0&hvadid=366315306136&hvpos=&hvnetw=g&hvrand=13518499605173326940&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1025954&hvtargid=pla-784457979043&ref=&adgrpid=75347436639&th=1)

PNY GeForce GTX 1650 4GB GDDR6 Dual Fan Graphics Card: [https://www.amazon.com/PNY-GeForce-1650-GDDR6-Graphics/dp/B08C7VTFQ8/ref=psdc_284822_t3_B01M360WG6](https://www.amazon.com/PNY-GeForce-1650-GDDR6-Graphics/dp/B08C7VTFQ8/ref=psdc_284822_t3_B01M360WG6)

CORSAIR Vengeance LPX 16GB (2 x 8GB) 288-Pin DDR4 RAM: [https://www.newegg.com/corsair-16gb-288-pin-ddr4-sdram/p/N82E16820233867?Item=9SIB8PYJEA5377&Source=socialshare&cm_mmc=snc-social-_-sr-_-9SIB8PYJEA5377-_-01302023](https://www.newegg.com/corsair-16gb-288-pin-ddr4-sdram/p/N82E16820233867?Item=9SIB8PYJEA5377&Source=socialshare&cm_mmc=snc-social-_-sr-_-9SIB8PYJEA5377-_-01302023)

Team Group 128GB M.2 SSD: [https://www.newegg.com/team-group-mp33-128gb/p/N82E16820331414?Description=m.2%20ssd%20128%20gb&cm_re=m.2_ssd%20128%20gb-_-20-331-414-_-Product](https://www.newegg.com/team-group-mp33-128gb/p/N82E16820331414?Description=m.2%20ssd%20128%20gb&cm_re=m.2_ssd%20128%20gb-_-20-331-414-_-Product)

Seagate BarraCuda 2TB Internal Hard Drive: [https://www.amazon.com/Seagate-BarraCuda-Internal-Drive-3-5-Inch/dp/B07H2RR55Q/ref=asc_df_B07H2RR55Q/?tag=hyprod-20&linkCode=df0&hvadid=319972287270&hvpos=&hvnetw=g&hvrand=9119350792040813109&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1025954&hvtargid=pla-613251472056&th=1](https://www.amazon.com/Seagate-BarraCuda-Internal-Drive-3-5-Inch/dp/B07H2RR55Q/ref=asc_df_B07H2RR55Q/?tag=hyprod-20&linkCode=df0&hvadid=319972287270&hvpos=&hvnetw=g&hvrand=9119350792040813109&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1025954&hvtargid=pla-613251472056&th=1)

Thermaltake Toughpower GX2 80+ Gold 500W Power Supply: [https://www.amazon.com/Thermaltake-Toughpower-Crossfire-Continuous-PS-TPD-0600NNFAGU-2/dp/B087CDR14Z/ref=pd_lpo_1?pd_rd_w=M54vf&content-id=amzn1.sym.116f529c-aa4d-4763-b2b6-4d614ec7dc00&pf_rd_p=116f529c-aa4d-4763-b2b6-4d614ec7dc00&pf_rd_r=EXVZKP06FTX1XRRSZX5E&pd_rd_wg=DOqEq&pd_rd_r=5e5a4b24-9f86-43a4-bb65-7a2367f8704f&pd_rd_i=B087CDR14Z&th=1](https://www.amazon.com/Thermaltake-Toughpower-Crossfire-Continuous-PS-TPD-0600NNFAGU-2/dp/B087CDR14Z/ref=pd_lpo_1?pd_rd_w=M54vf&content-id=amzn1.sym.116f529c-aa4d-4763-b2b6-4d614ec7dc00&pf_rd_p=116f529c-aa4d-4763-b2b6-4d614ec7dc00&pf_rd_r=EXVZKP06FTX1XRRSZX5E&pd_rd_wg=DOqEq&pd_rd_r=5e5a4b24-9f86-43a4-bb65-7a2367f8704f&pd_rd_i=B087CDR14Z&th=1)

GIGABYTE B550 ATX AMD Motherboard: [https://www.newegg.com/gigabyte-b550-gaming-x-v2/p/N82E16813145255?Description=GIGABYTE%20B550%20GAMING%20X%20V2%20AM4%20AMD%20B550%20SATA%206Gb/s%20USB%203.0%20ATX%20AMD%20Motherboard&cm_re=GIGABYTE_B550%20GAMING%20X%20V2%20AM4%20AMD%20B550%20SATA%206Gb/s%20USB%203.0%20ATX%20AMD%20Motherboard-_-13-145-255-_-Product&quicklink=true](https://www.newegg.com/gigabyte-b550-gaming-x-v2/p/N82E16813145255?Description=GIGABYTE%20B550%20GAMING%20X%20V2%20AM4%20AMD%20B550%20SATA%206Gb/s%20USB%203.0%20ATX%20AMD%20Motherboard&cm_re=GIGABYTE_B550%20GAMING%20X%20V2%20AM4%20AMD%20B550%20SATA%206Gb/s%20USB%203.0%20ATX%20AMD%20Motherboard-_-13-145-255-_-Product&quicklink=true)

Corsair 4000D ATX Mid Tower Computer Case: [https://www.newegg.com/black-corsair-4000d-airflow-atx-mid-tower/p/N82E16811139156](https://www.newegg.com/black-corsair-4000d-airflow-atx-mid-tower/p/N82E16811139156)

Wavlink AX3000 Wifi Network Card: [https://www.newegg.com/wavlink-690a5d-usb-3-0/p/0XM-00B5-00053?Description=wifi%20adapter&cm_re=wifi_adapter-_-0XM-00B5-00053-_-Product&quicklink=true](https://www.newegg.com/wavlink-690a5d-usb-3-0/p/0XM-00B5-00053?Description=wifi%20adapter&cm_re=wifi_adapter-_-0XM-00B5-00053-_-Product&quicklink=true)


## Cited Sources

[1] Z. Rahman, A. Ami, M. A. Ullah, "A Real-Time Wrong-Way Vehicle Detection Based on YOLO and Centroid Tracking," 2020 IEEE Region 10 Symposium (TENSYMP), 5-7 June 2020, Dhaka, Bangladesh. [https://arxiv.org/pdf/2210.10226.pdf](https://arxiv.org/pdf/2210.10226.pdf).

[2] J. Lentin. "A Gentle Introduction to YOLO v4 for Object detection in Ubuntu 20.04," _Robocademy_. [https://robocademy.com/2020/05/01/a-gentle-introduction-to-yolo-v4-for-object-detection-in-ubuntu-20-04/](https://robocademy.com/2020/05/01/a-gentle-introduction-to-yolo-v4-for-object-detection-in-ubuntu-20-04/).

[3] A. James. "Faster YOLOv4 Performance with CUDA enabled OpenCV," _Toward Data Science_, 24 Feb. 2021. [https://towardsdatascience.com/yolov4-with-cuda-powered-opencv-dnn-2fef48ea3984](https://towardsdatascience.com/yolov4-with-cuda-powered-opencv-dnn-2fef48ea3984).

[4] S. Canu, "YOLO object detection using OpenCV with Python," _Pysource_. [https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/](https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/).

[5] P. Richards, “What Type of Computer Do I Need to Live Stream?,” _StreamGeeks_, 24 Mar. 2021. [https://streamgeeks.us/what-computer-do-i-need-to-live-stream/](https://streamgeeks.us/what-computer-do-i-need-to-live-stream/).

[6] N. Uke, R. Thool, "Moving Vehicle Detection for Measuring Traffic Count Using OpenCV," _Journal of Automation and Control Engineering_, Feb. 2012. [http://dx.doi.org/10.12720/joace.1.4.349-352](http://dx.doi.org/10.12720/joace.1.4.349-352).

[7] C. Tonde, "Hardware and Software Platforms for Computer Vision," CS: 534 Computer Vision, Rutgers University, Spring 2022. [https://people.cs.rutgers.edu/~elgammal/classes/cs534/lectures/GPUs.pdf](https://people.cs.rutgers.edu/~elgammal/classes/cs534/lectures/GPUs.pdf).

[8] A. Sharma, V. R. Shrimali, M. Beyeler, “Technical requirements,” _Machine Learning for OpenCV_, 2nd ed., _Packet Publishing Ltd._, Birmingham, UK, Sept. 2019. [https://www.oreilly.com/library/view/machine-learning-for/9781789536300/038d70bd-e186-483b-8ef0-23b344f46ecc.xhtml](https://www.oreilly.com/library/view/machine-learning-for/9781789536300/038d70bd-e186-483b-8ef0-23b344f46ecc.xhtml).

[9] NeuroTechnology, “SentiVeillance SDK,”  _NeuroTechnology_, 2022. [https://www.sentiveillance.com/sentiveillance-sdk/](https://www.sentiveillance.com/sentiveillance-sdk/).

[10] J. Fox, “80 PLUS Bronze vs Gold vs Platinum vs Titanium: Which PSU Rating do you Need?,” _TechGuided.com_, 13 Jun. 2022. [https://techguided.com/80-plus-bronze-vs-gold-vs-platinum-vs-titanium-which-psu-rating-do-you-need/](https://techguided.com/80-plus-bronze-vs-gold-vs-platinum-vs-titanium-which-psu-rating-do-you-need/).

[11] PCPartPicker, “Choose Your Parts,” _PCPartPicker_, 2022. [https://pcpartpicker.com/list/t7gKmr](https://pcpartpicker.com/list/t7gKmr).

[12] “Omni Calculator,” [https://www.omnicalculator.com/other/streaming-bitrate](https://www.omnicalculator.com/other/streaming-bitrate).

[13] Restream Team, “What is a good upload speed for streaming?,” _Restream, Inc._, 1 Jul. 2022, [https://restream.io/blog/what-is-a-good-upload-speed-for-streaming/](https://restream.io/blog/what-is-a-good-upload-speed-for-streaming/).

[14] UserBenchmark, "Compare: Intel Core i5-7300HQ vs. AMD Ryzen 5 3600". [https://cpu.userbenchmark.com/Compare/Intel-Core-i5-7300HQ-vs-AMD-Ryzen-5-3600/m223877vs4040](https://cpu.userbenchmark.com/Compare/Intel-Core-i5-7300HQ-vs-AMD-Ryzen-5-3600/m223877vs4040).

[15] UserBenchmark, "Compare: Nvidia GTX 1650 vs. Nvidia GTX 1050-Ti". [https://gpu.userbenchmark.com/Compare/Nvidia-GTX-1650-vs-Nvidia-GTX-1050-Ti/4039vs3649](https://gpu.userbenchmark.com/Compare/Nvidia-GTX-1650-vs-Nvidia-GTX-1050-Ti/4039vs3649).

## Revisions

12/4/2022 - Downscaled components to cut costs

1/24/2023 - Updated components to factor in YOLO algorithm with CUDA-enabled OpenCV

1/30/2023 - Included compatibility of selected parts
