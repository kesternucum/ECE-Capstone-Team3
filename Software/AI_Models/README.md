# AI Models and Car Count Total

## Functionality

The static tracking and dynamic tracking models can be found in their respective Static_Model/ and Dynamic_Model/ folders. The static tracking model counts the number of cars in a frame, and the dynamic tracking model counts the number of cars that enter or exit an area by tracking the direction of the cars as they move across a virtual line.

Car_Count_Read.py sums the number of cars from the dynamic_data.json file (count from dynamic model) and the static_data.json file (count from static model) and sends that number to the mobile application upon a change in the number.

## Dependencies

Operating System
  * Linux distribution (e.g. Ubuntu) or MacOS

Python Languages and Libraries
  * Python3 (Python 3.6.9 and up)
```
sudo apt-get upgrade python3
```

You also need to have the backend api for the mobile application and the private Google Firebase .json key to communciate with the Google Firebase remote server.

## How to Install

Clone the ECE-Capstone-Team3 repository from GitHub.
```
git clone https://github.com/kesternucum/ECE-Capstone-Team3
```

## How to Run/Use

Command to Run
```
python3 Car_Count_Read.py
```
