# Static Tracking Model

This pretrained YOLOv3 model was taken from [https://github.com/guptavasu1213/Yolo-Vehicle-Counter](https://github.com/guptavasu1213/Yolo-Vehicle-Counter). The code was modified according for the needs for this project.

## Functionality

The static tracking model counts the number of cars in a frame and writes this number to the ../static_data.json file, which is used to determine the total number of cars in the parking lot to be sent to the remote server. The static model can only process images from a single video feed source.

yolo_video.py performs the processing of images received from a video or video feed.

input_retrieval.py parses the input arguments from the Python command to run the model.

run_detections.py can be used to run detections on multiple videos in a directory.

## Dependencies

Operating System
  * Linux distribution (e.g. Ubuntu) or MacOS

Pre-trained Weights
  * Pre-trained yolov3 weight file from Joseph Redmon
```
cd yolo-coco
wget https://pjreddie.com/media/files/yolov3.weights
```

Python Languages and Libraries
  * Python3 (Python 3.6.9 and up)
```
sudo apt-get upgrade python3
```
  * pip3
```
sudo apt-get install python3-pip
```
  * OpenCV 3.4 or above
```
pip3 install opencv-python
```
  * imutils
```
pip3 install imutils
```
  * scipy
```
pip3 install scipy
```

GPU Computations
  * Install GPU appropriate drivers as per Step 2 in [https://www.pyimagesearch.com/2019/12/09/how-to-install-tensorflow-2-0-on-ubuntu/](https://www.pyimagesearch.com/2019/12/09/how-to-install-tensorflow-2-0-on-ubuntu/)
  * Install OpenCV for GPU computations (since OpenCV installed via pip does not support GPU computations for 'dnn' module):
[https://www.pyimagesearch.com/2020/02/03/how-to-use-opencvs-dnn-module-with-nvidia-gpus-cuda-and-cudnn/](https://www.pyimagesearch.com/2020/02/03/how-to-use-opencvs-dnn-module-with-nvidia-gpus-cuda-and-cudnn/)

## How to Install

Clone the ECE-Capstone-Team3 repository from GitHub.
```
git clone https://github.com/kesternucum/ECE-Capstone-Team3
```

A static IP address is required to run this model. To set the IP address of the Avigilon cameras, install the Camera Configuration Tool: [https://www.avigilon.com/products/cameras-sensors/camera](https://www.avigilon.com/products/cameras-sensors/camera). Once the camera is powered and connected via Ethernet, a static IP address can be assigned, and this IP address can be used to view the device web browser interface in which the single frame addressed can be found. Please consult [https://help.avigilon.com/h5a-b/en-us/0Common/H4_AssignIP.htm](https://help.avigilon.com/h5a-b/en-us/0Common/H4_AssignIP.htm) for more information.

## How to Run/Use

The model can be run standalone for testing or training purposes. In order for data to actually be communicated with the remote server, the Car_Count_Read.py model must be run as well as the mobile application api.

To run with a prerecorded video, set videoStream = cv2.VideoCapture(inputVideoPath) in which inputVideoPath is the video argument in --input. To run with feed from a camera, set videoStream = cv2.VideoCapture(<http link of camera>).

Required Arguments
  * `--input` or `-i` argument the path to the input video (can be arbitrary if using IP address in yolo_video.py)
  * `--output` or `-o` argument requires the path to the output video (for live viewing purposes)
  * `--yolo` or `-y` argument requires the path to the folder where the configuration file, weights and the coco.names file is stored

Optional Arguments
  * `--confidence` or `-c` is an optional argument which requires a float number between 0 to 1 denoting the minimum confidence of detections. By default, the confidence is 0.5 (50%).
  * `--threshold` or `-t` is an optional argument which requires a float number between 0 to 1 denoting the threshold when applying non-maxima suppression. By default, the threshold is 0.3 (30%).
  * `--use-gpu` or `-u` is an optional argument which requires 0 or 1 denoting the use of GPU. By default, the CPU is used for computations

Command to Run
```
python3 yolo_video.py --input <input video path> --output <output video path> --yolo yolo-coco [--confidence <float number between 0 and 1>] [--threshold <float number between 0 and 1>] [--use-gpu 1]
```
Example Commands
* Running with defaults
```
python3 yolo_video.py --input inputVideos/highway.mp4 --output outputVideos/highwayOut.avi --yolo yolo-coco
```
* Specifying confidence
```
python3 yolo_video.py --input inputVideos/highway.mp4 --output outputVideos/highwayOut.avi --yolo yolo-coco --confidence 0.3
```
* Using GPU
```
python3 yolo_video.py --input inputVideos/highway.mp4 --output outputVideos/highwayOut.avi --yolo yolo-coco --use-gpu 1
```
