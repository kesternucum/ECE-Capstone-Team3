# Detail Design for Power of Primary Data Acquisition System

## Big Picture

The primary data acquisition will use cameras designed for power over ethernet. Due to the monitoring system being outdoors and away from buildings, the cameras can’t be powered by traditional means of ethernet cables. Therefore, a “wireless” solution will have to be developed in order to ensure that the cameras can have a reliable and hands-off way to remain powered.

## Specifications



1. Camera Derived Specs [1]
    * Power Consumption
        * 6 W with external power (10 W for -IR option)
        * 6 W with IEEE 802.3af Class 3 PoE (10 W for -IR option)
    * Power Source
        * VDC: 12 V +/- 10%, 6 W min (10 W min with -IR option)
        * VAC: 24 V +/- 10%, 8 VA min (12 VA min with -IR option)
        * PoE: IEEE 802.3af Class 3 compliant
    * Power Connector
        * 2-pin terminal block
        * Ethernet port
2. Communication Device Derived Specs [2]
    * Power Consumption
        * Less than 2 W
    * Power Source 
        * VDC: 5-15 V
    * Power Connector
        * Ethernet cable
        * USB cable
3. Heating Strips
    * Adjust for potential very low temp
4. Maintainability
    * Should be as hands-off as possible once installed
5. Reliability
    * Should keep the camera and communication device powered, at a minimum,  during operational hours
    * Weather should not impact power to the camera or comm device

## Buildable Schematic

![Figure 1. Power Supply Connection](../3D&#32;Models/Camera_Power_Connection.PNG)

&lt;div align="center"> Figure 1. Power Supply Connection

&lt;br />

&lt;div align="left">

## Analysis



1. Meeting Camera Derived Specifications
    * In order to meet the required specifications to power the camera, PoE or direct power can be used with the given voltage and wattage constraints as seen in the above specifications. The cameras are scattered across the lot and not located close to the Bell Hall building, so direct cable connections will not be a feasible option. Additional infrastructure is also not allowed to be built.
    * PoE Injector
        * The injector is a good option since many are commercially available that meet the IEEE 802.3af standard of the camera. They are also relatively cheap given the cameras needed supplied power from the injector (most on amazon.com are between $10-$20).
    * Direct Power
        * Given that the cameras have a 2-pin terminal block connection and the camera specification allows for it, direct power would be a simpler implementation than putting power through a PoE device minimizing constraints. This will also help reduce costs for the project as now there is no need to purchase a PoE device for each camera.
2. Meeting Communication Derived Specifications
    * The comm device should utilize the same power source as the camera for simplicity and consistency. The cameras and comm device are different in nature though, not only in power supply needs, but how they connect to the power source which will make the use of adapters or voltage dividers important.
3. Meeting Maintainability Standards
    * If any work is to be done relating to cameras, facilities must be involved in order to make changes to the hardware. Therefore, considerations will be made to ensure that the cameras become as “hands off” as possible once they are mounted onto the posts including how the cameras will be powered.
    * Battery Power
        * Battery power is easy as an implementation, but will require frequent replacement for a device that should be having power supplied to it all day. Therefore, to spare the need for facilities to do regular battery inspections and replacements, traditional batteries will not be used.
    * Solar Power
        * Solar power has become a favorable choice to power cameras due to its lifespan. Panels require little maintenance as they tend to have a slow degradation rate with most lost low quality solar panels averaging about 82.47% of their original output after 25 years [5].
4. Meeting Reliability Standards
    * The cameras should be able to remain powered over operational hours without issue in order to maintain accuracy of and prevent the loss of data. To accomplish this, the power system must perform regardless of weather or temporary solar panel failure.
    * Rechargeable Batteries
        * Given the constraint to use solar energy, a rechargeable battery is the easiest option to be used in tandem with the solar panel. A battery that can hold a good duration of charge should ensure a power supply even if the solar panels aren’t operating well.
5. Device Selection
    * The Mighty Max Battery was selected due to it providing the needed 12 Volts while also being cost effective at about $20 per unit [8]. The battery is also rechargeable [8].
    * The 12 volt solar panel made by Dakota Lithium was selected as it is lightweight (2.11 pounds) and compatible with the selected 12 Volt 7 Ah Mighty Max Battery [7].

## Bill of Materials

| Name of Item | Description | Used in which subsystem(s) | Part Number | Manufacturer | Quantity |    Price   | Total |

| ------------ | ----------- | -------------------------- | ----------- | ------------ | -------- | ---------- | ----- |

|Mighty Max Battery|     "12-Volt 7 Ah Sealed Lead Acid (SLA) Rechargeable Battery"|     Sign|     ML7-12|     Mighty Max|     1|     $19.99|     $19.99|

|Solar Panel|     "12V FLEXIBLE SOLAR PANEL – 20 WATTS"|     Sign|     Number Not Found|     Dakota Lithium|     1|     $49.00|     $49.00|

## Cited Sources

[1] “2.0 Megapixel Day/Night H.264 HD Indoor Dome Camera,” _AVIGILON_, 2013.  https://www.securityinformed.com/datasheets/avigilon-2-0-h3-d1-ip-dome-camera/co-3126-ga/2.0-H3-DdatasheetEN2.pdf.

[2] “Vonets VAP11G-300,” _en.vonets.es_, 2022. http://en.vonets.es/products/VAP11G-300/.

[3] “What is PoE? Power over Ethernet Explained!” _NVT PHYBRIDGE_, 2 Mar 2020.  https://www.nvtphybridge.com/power-over-ethernet/#:~:text=Power%20over%20Ethernet%20(PoE)%20is,power%20over%20the%20network%20cabling.

[4] “What is a PoE Injector?” _Versa Technology_, 6 Apr 2021. https://www.versatek.com/what-is-a-poe-injector/.

[5] Walker, Daniel, “The Complete Guide to AA Batteries,” _Battery Specialists_, 21 Nov 2020.  https://batteryspecialists.com.au/blogs/news/the-complete-guide-to-aa-batteries#:~:text=On%20average%2C%20AA%20batteries%20last,of%20power%20before%205%20years.

[6] Sendy, Andrew, “How long do solar panels actually last?” _SolarReviews_, 14 Jan 2022.  https://www.solarreviews.com/blog/how-long-do-solar-panels-last#:~:text=Most%20solar%20panels%20last%2025,25%2B%20year%20solar%20panel%20lifespan.

[7] “12V FLEXIBLE SOLAR PANEL - 20 WATTS,” _Dakota Lithium_. https://dakotalithium.com/product/12v-solar-panel/.

[8] “12-Volt 7 Ah Sealed Lead Acid (SLA) Rechargeable Battery,” _Home Depot_, 2023. https://www.homedepot.com/p/MIGHTY-MAX-BATTERY-12-Volt-7-Ah-Sealed-Lead-Acid-SLA-Rechargeable-Battery-ML7-12/307979135.