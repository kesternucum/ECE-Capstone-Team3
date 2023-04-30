# Sign Software

## Functionality

The folder has two different scripts:

Sign_Code_Final.py connects to the Firebase database with the give JSON file containing credentials. It then pulls parking availability for the "Bell Hall" lot in the database, and serially sends it over a specified port.

Arduino_Code_Final.ino (inside Arduino_Code_Final folder) is meant to be ran on an Arduino connected to the computer running the Sign_Code_Final code. It gets a number from the connected comptuer, and displays that number by enabling and disabling digital pins connected to LED strips.

## Dependencies

The python code requires the JSON file to be in the same directory. The computer running the script must also be connected to internet.

The Arduino code requires the Arduino IDE to be installed to the code can be uploaded to the connected arduino board. The Arduino board needs to be an Arduino Mega 2560 Rev3.

## Installation

The python code only requires that python be installed on the computer being used.

The Arduino code requires the Arduino IDE to be installed.

## Running the program

The Arduino code must be ran first. This can be done by opening the Arduino_Code_Final file in the Arduino IDE, then pushing the code to the board. Once that is complete, the python code can be ran.

For the python code, open up a terminal in the directory where the python code and JSON file is located. Use the command "py Sign_Code_Final.py" to begin running the program. Once done, the code should begin sending over values from the database to the Arduino.

Once both scripts are running, ensure the computer is not turned off to prevent the python code from erroring.
