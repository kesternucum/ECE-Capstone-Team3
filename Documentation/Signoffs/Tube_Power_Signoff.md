# Pneumatic Tube Power Detail Design

## Big Picture

The purpose of this subsystem is to provide sufficient and reliable power to the arduino used to operate the road tubes. Power will be supplied using solar energy.

## Constraints



1. Hardware Constraints
    * Arduino Uno Rev3 [1]
        * Input Voltage (recommended) - 7-12 Volts
2. Reliability Constraints
    * Always provide power during operational hours
    * Operate regardless of weather conditions

## Buildable Schematic

![Figure 1. Power Supply Connection](../3D&#32;Models/Tube_Power_Connection.PNG)

&lt;div align="center"> Figure 1. Power Supply Connection

&lt;br />

&lt;div align="left">

## Analysis



1. Meeting Reliability Requirements
    * In order to meet reliability needs, a combination of a solar panel and rechargeable battery will be used. The rechargeable battery should hold sufficient enough storage that it can power the sign for a few days given that there is a lack of sunlight for the solar panel to power it, and the solar panel should still be able to charge the battery within a day given there is sufficient sunshine. Solar panels are also designed for outdoor use, so weather resistance shouldn’t be an issue.
2. Meeting Hardware Requirements
    * The Arduino Uno can take in a 12 Volt power supply, so one battery should be sufficient to power the device. 
3. Hardware Selections
    * The Mighty Max Battery was selected due to it providing the needed 12 Volts while also being cost effective at about $20 per unit [3]. The battery is also rechargeable [3].
    * The 12 volt solar panel made by Dakota Lithium was selected as it is lightweight (2.11 pounds) and compatible with the selected 12 Volt 7 Ah Mighty Max Battery [2].

## Bill of Materials

| Name of Item | Description | Used in which subsystem(s) | Part Number | Manufacturer | Quantity |    Price   | Total |

| ------------ | ----------- | -------------------------- | ----------- | ------------ | -------- | ---------- | ----- |

|Mighty Max Battery|     "12-Volt 7 Ah Sealed Lead Acid (SLA) Rechargeable Battery"|     Sign|     ML7-12|     Mighty Max|     1|     $19.99|     $19.99|

|Solar Panel|     "12V FLEXIBLE SOLAR PANEL – 20 WATTS"|     Sign|     Number Not Found|     Dakota Lithium|     1|     $49.00|     $49.00|

## Revisions

No revisions at this time.

## Cited Sources

[1] “Arduino Uno Rev3.”_arduino.cc_, 2023. https://store-usa.arduino.cc/products/arduino-uno-rev3.

[2] “12V FLEXIBLE SOLAR PANEL - 20 WATTS,” _Dakota Lithium_. https://dakotalithium.com/product/12v-solar-panel/.

[3] “12-Volt 7 Ah Sealed Lead Acid (SLA) Rechargeable Battery,” _Home Depot_, 2023. https://www.homedepot.com/p/MIGHTY-MAX-BATTERY-12-Volt-7-Ah-Sealed-Lead-Acid-SLA-Rechargeable-Battery-ML7-12/307979135.
