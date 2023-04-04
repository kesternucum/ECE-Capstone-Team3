# Prototype

## Original Requirements

All of the below requirements demonstrate minimum functionality of every subsystem. These requirements compose the original agreement for the prototype design.

### Primary Data Acquisition System

One Static Tracking Camera
 - Connected to Linux server or other PC/laptop via Ethernet.
 - Must be able to obtain footage from the camera and upload images to the server.
 - Must be powered via solar power.

### Server

Server
 - Must be able to view a video via Ethernet from a camera.
 - Must be able to communicate with the remote database for the mobile application and the sign, i.e. send a number from the server which is shown on the mobile application and the sign.

### Sign

Sign
 - Must be able to display a number that is sent by the remote server.
 - Must be powered via solar power.
 - Must be able to communicate with server wirelessly using the wireless communication module, i.e. receive a number from the server and display it.

### Mobile Application

Mobile Application
 - Shows (arbitrary) data that is sent from the server.
 - Note: the mobile application is under the computer science team, so their work will be integrated with ours.

## Substitutions

Since we were not able to design a fully functional power system, and since the wireless communications devices have not arrived, we propose to substitute power and wireless communication for increased functionality in the cameras and AI processing.

### Primary Data Acquisition System

Rather than just one camera, we propose implementing two cameras (the number of cameras agreed upon for our final deliverable) for our prototype to make up for the lack of power and communications.

Two Cameras
 - One static tracking camera
    - Must be able to obtain video feed of stationary cars in a parking lot from camera via Ethernet.
    - The goal of this camera is to obtain frames of cars in stationary parking spots.
 - One dynamic tracking camera
    - Must be able to obtain video feed of moving cars in a parking lot from camera via Ethernet.
    - The goal of this camera is to obtain frames of cars moving across a parking lot.
 - Both camera will be demonstrated simultaneously when connected via Ethernet to the Linux server.
    - The Linux server has only one Ethernet port, which is already taken up by an Ethernet cable connected to the Tech network. It also has only one available USB port, in which a switch can be plugged in.
    - Cameras will NOT be powered by solar power. However, because a switch is required to connect both cameras to the server, the cameras will be powered via Ethernet (PoE) since the switch provides power directly to the cameras.
 - The cameras will be placed next to a window in the Capstone Lab to look down upon the Gold parking lot in the Engineering Quad. The Engineering Quad will serve as our prototype test lot to show basic functionality.

### Server

AI was not in the original prototype design, so we propose substituting power and wireless communications for two working vehicle detection models, one for static tracking and another for dynamic tracking.

Two Vehicle Detection Models
 - Static tracking model
   - Performs pre-processing of frames to black out part of the frame so that the algorithm only performs on a selected region.
   - Algorithm is performed to detect the number of vehicles in the selected portion of the lot. This number is then sent to the remote database that also interfaces with the mobile application.
 - Dynamic tracking model
   - Adds two lines to each frame that is chosen to be processed and determines the direction that a vehicle is going based on which line it runs in first.
   - The data on the remote database will be updated based on the traffic flow in and out of that area.
 - Both models must be able to perform frame skipping that will process every Nth frame and keeps up with the rate in which frames are received. In other words, frame-skipping does not affect the outputs being real-time.

### Mobile Application

We also propose substituting power and wireless communications for functionality in which the number of available parking spots can be determined from the two models and sent to the mobile application and sign.

Remote Database
 - The remote database will perform the calculations to determine the number of available spots from both the static tracking model and the dynamic tracking model.

### Sign

Sign
 - Will display data pulled directly from the remote database, i.e. the current number of available parking spots entered on the remote database for the mobile application.
 - Will be powered by a computer, which will also serve as the communication system to allow the sign to communicate to the remote server via Wi-Fi.
