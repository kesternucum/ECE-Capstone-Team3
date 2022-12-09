# Detail Design for Heat Module of Primary Data Acquisition System

## Big Picture

The primary data acquisition will use cameras designed for indoor use, but in an outdoor setting. Therefore, a few more additional constraints must be addressed in order to ensure the cameras can operate properly and don’t run into hardware issues. This document addresses temperature control of the cameras to ensure they don’t go below their specified operation temperature.

## Specifications

1. Camera Specs [1]
    * Operating Temperature
        * -10 °C to +50 °C (14 °F to 122 °F)
2. Functional Time
    * The heat module should only heat the camera when necessary
3. Size of Module
    * Should not interfere with camera vision
    * Should be easy to mount up with camera
4. Maintenance
    * Should be a reliable device that does not require frequent changing

## Analysis

1. Meeting Camera Derived Specifications
    * The average range of temperature within Cookeville for the year usually goes between 28 °F to 88 °F with it rarely going lower than 12 °F and higher than 94 °F [2]. The lowest and highest temperature ever recorded in Cookeville are -22 °F and 105 °F, respectively [3]. This means that while there is no concern for cooling the device in the high range temperatures of the summer, making sure the camera stays warm during potential lows in the winter is a must.
2. Temperature Detection
    * Given that the camera needs to be heated whenever the environment has reached a low enough temperature, the device should be able detect that temperature and begin to heat up accordingly.
    * Thermocouple
        * Description - To briefly summarize, a thermocouple is a device that outputs voltage based on the temperature of its environment. Its output is typically on the order of milliVolts (mV) [3]. 
        * Benefits
            * Size - These devices are small but come with lengthy cables if needed to be connected to another device farther away.
            * Longevity - If a thermocouple is properly installed and maintained, it should last around 10 years [7].
            * Power - Since thermocouples produce voltage as an output, they could also be used to power the heating device given a voltage amplifier is used to provide sufficient power.
        * Issues
            * Low Temperatures - While there are thermocouples that are designed to do readings below freezing (0 °C or 32 °F), they do not typically produce a lot of voltage around those temperatures (about 1 mV) [6]. These lower voltages will be harder to pick up from other connected devices.
            * Supplying Power - Even though there exists charts for thermocouples that state the voltage and temperature relationship, a simple device that can determine when to begin supplying power based on a specific voltage input is not readily available. Therefore, a microcontroller may have to be considered to get the voltage input, which could also be an issue given the small voltage produced by the thermocouple.
3. Heating Device
    * Heat Tape
        * Benefits
            * Size - The heat tape comes in a variety of sizes and is flexible enough to be placed on most surfaces.
            * Power - Heat tape requires very little energy to be powered.
        * Issues
            * Heat Output - Even though some have very low power requirements, these devices can produce an extraordinary amount of heat (a 1 Watt heat tape appliance can heat up to 176 °F [8]).
4. Final Design
    * No final design has been made at this time

## Bill of Materials

1. No items finalized at this time

## Cited Sources

[1] “2.0 Megapixel Day/Night H.264 HD Indoor Dome Camera,” _AVIGILON_, 2013.  [https://www.securityinformed.com/datasheets/avigilon-2-0-h3-d1-ip-dome-camera/co-3126-ga/2.0-H3-DdatasheetEN2.pdf](https://www.securityinformed.com/datasheets/avigilon-2-0-h3-d1-ip-dome-camera/co-3126-ga/2.0-H3-DdatasheetEN2.pdf)

[2] “Climate and Average Weather Year Round in Cookeville,” _Weather Spark_. [https://weatherspark.com/y/15151/Average-Weather-in-Cookeville-Tennessee-United-States-Year-Round#:~:text=Over%20the%20course%20of%20the,or%20above%2094%C2%B0F](https://weatherspark.com/y/15151/Average-Weather-in-Cookeville-Tennessee-United-States-Year-Round#:~:text=Over%20the%20course%20of%20the,or%20above%2094%C2%B0F)

[3] “Cookeville Weather Records,” _Extreme Weather Watch_, 2022. [https://www.extremeweatherwatch.com/cities/cookeville#:~:text=The%20highest%20temperature%20ever%20recorded,occurred%20on%20June%2030%2C%202012.&text=The%20lowest%20temperature%20ever%20recorded,occurred%20on%20January%2021%2C%201985](https://www.extremeweatherwatch.com/cities/cookeville#:~:text=The%20highest%20temperature%20ever%20recorded,occurred%20on%20June%2030%2C%202012.&text=The%20lowest%20temperature%20ever%20recorded,occurred%20on%20January%2021%2C%201985)

[4] “Thermocouples,” _Industrial Quick Search_. [https://www.iqsdirectory.com/articles/thermocouple.html](https://www.iqsdirectory.com/articles/thermocouple.html)

[5] Hunt, Scott, “AD8495 Interface to Type T Thermocouples,” 2022. [https://www.analog.com/en/technical-articles/ad8495-interface-to-type-t-thermocouples.html](https://www.analog.com/en/technical-articles/ad8495-interface-to-type-t-thermocouples.html)

[6] “Thermocouple Types,” _Mosaic Documentation Web_. [http://www.mosaic-industries.com/embedded-systems/microcontroller-projects/temperature-measurement/thermocouple/types-wire-element](http://www.mosaic-industries.com/embedded-systems/microcontroller-projects/temperature-measurement/thermocouple/types-wire-element)

[7] “How to Replace a Thermocouple,” _Home Depot_, 2022. [https://www.homedepot.com/c/ah/how-to-replace-a-thermocouple/9ba683603be9fa5395fab901ced3a679](https://www.homedepot.com/c/ah/how-to-replace-a-thermocouple/9ba683603be9fa5395fab901ced3a679)

[8] “Icstation 5V 1W Flexible Polyimide Heater Plate Adhesive PI Heating Film 30mmx40mm,” _amazon.com_, 2022. [https://www.amazon.com/dp/B06XR46HKM/ref=emc_b_5_t?th=1](https://www.amazon.com/dp/B06XR46HKM/ref=emc_b_5_t?th=1)