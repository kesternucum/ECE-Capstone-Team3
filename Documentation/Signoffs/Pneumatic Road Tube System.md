<h1>Detailed Design for Pneumatic Road Pressure Tube Subsystem within the Secondary Data Acquisition System</h1>


<h2>Big Picture</h2>

This subsystem will be responsible for counting how many vehicles are leaving or entering the Bell Hall parking lot. Counting will be done by pneumatic road tube sensors that will transmit their data to a counter. The counter will then transmit the data wirelessly to the server for processing.

<h3>Specifications</h3>

1. Selected Sensor Specifications
  *Pressure Range: 0 to 50kPa
  * 3 Vdc power needed
  * Microprocessor to process sensor data

2. Wireless Data Transfer Module

3. Outdoor Case & Hardware

<h4>Analysis</h4>

  *Selected Sensor Specification

 The MX53DP pressure sensor[1] needs to be able to detect variations in pressure inside the road tube. After researching different types of sensors, differential pressure sensing seems like the best solution. Using the differential pressure sensor, how much absolute pressure does not need to be known. Only the difference between two point, which will be the pressure in the tube and the internal vacuum pressure inside the sensor. The Arduino UNO R3[2] board will use Smakn 8194[3], which is a 12Vdc to 9Vdc step down converter to power it. The sensor however needs 3Vdc to power it so Digi-Key LD1085V[4], a 3 pin IC voltage regulator will be used to acquire the needed voltage. The sensor signal pin (2) will be connected to the IO pins on an Arduino Uno board to signify when the pressure in the road tube has exceeded the internal vacuum pressure of the sensor. 


  *Wireless Data Transfer Module

Data will be transmitted wirelessly back to the server using a ESP8288 Wi-Fi module[5]. This component works especially well with Arduino devices. 



  *Outdoor Case & Hardware	

The case for the hardware will require weather proofing to prohibit water from entering the case and damaging hardware. All tube connections will be done at the case and will also need to be leak proof. The rubber tubing selected as the road tube will be RT-SYB-3/16[6], this tubing is a synthetic blend that is specifically used in road tube applications for its resistance to UV rays and durability. The tube will be anchored down using a nail (RTA-SN-35)  and strap(RTA-CF R 9/16) combination. The anchor will be placed  on the opposing side of the case and will have an end plug(EP-312) to keep internal pressure and not allow contaminants to enter the tube and thus the case. 


Cited Sources
[1]   “MPX53DP: Digi-Key Electronics.” Digi, https://www.digikey.com/en/products/detail/nxp-usa-inc/MPX53DP/951812.
 
[2]   “Arduino Uno REV3.” Arduino Online Shop, https://store-usa.arduino.cc/products/arduino-uno-rev3/?gclid=Cj0KCQiA4OybBhCzARIsAIcfn9kV9UkTQrjUS3eyFXLQWgOKbkT_-2trZUZcNxKCzBDpr9lKgvfBuoMaAuWdEALw_wcB.
 
[3]   SMAKN DC/DC Converter 12V Step down to 3V/3A Power Supply Module. https://www.amazon.com/SMAKN%C2%AE-Converter-Power-Supply-Module/dp/B00ODL140M.
 
[4]   “LD1085V: Digi-Key Electronics.” Digi, https://www.digikey.com/en/products/detail/stmicroelectronics/LD1085V/586003?utm_adgroup=Integrated+Circuits&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Supplier_STMicroelectronics_0497_Co-op&utm_term=&utm_content=Integrated+Circuits&gclid=Cj0KCQiA4OybBhCzARIsAIcfn9ktcOJ0ebDnzHkmoL8cyy0OwVvOTisjXmD-CNdj8xpTFwz65r4_u98aAj7GEALw_wcB.
 
[5]   #1758620, Member. “WIFI Module - ESP8266 (4MB Flash).” WRL-17146 - SparkFun Electronics, https://www.sparkfun.com/products/17146.
 
[6]   “EPDM Synthetic Road Tube.” EPDM Synthetic Road Tube | Diamond Traffic ProductsRT-SYN, http://diamondtraffic.com/product/EPDM-Road-Tube.
