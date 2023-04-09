# Import Libraries
import serial
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize serial communication of Arduino
arduino = serial.Serial(port='COM4', baudrate=9600)

# This function returns available parking lot count from firebase database
def getData():
    try:
        app = firebase_admin.get_app()
        firebase_admin.delete_app(app)
    except:
        pass

    # Load credentials and access firebase database
    cred = credentials.Certificate('intelligentparkingfb-59ed35520e29.json')
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    # Access table containing parking lot counts
    doc = db.collection(u'parkingLots').document(u'92opt')

    firebase_data = doc.get().to_dict()['openSpots']
    print("Open Spots:",firebase_data)
    return firebase_data

# This function sends data to Arduino
def writeData(input_data):
    arduino.write(bytes(str(input_data), 'utf-8'))
    time.sleep(0.05)
    
# Main loop
while True:
    data = getData()
    writeData(data)
    time.sleep(15)