# Calibration
Calibration of the SP3 sunpanel by Parans.
The final degree project report is found [here](http://studentarbeten.chalmers.se/publication/218757-kalibrering-av-ljussensor-for-parans-solpanel).

Abstract
---
Parans Solar Lighting, a company based in Göteborg, have developed a solar panel used to bring sunlight indoors, by focusing light into optical fibres. A photosensor is used to adjust the panel's direction, in order to maximize its intake of light, and the necessary calibration of the photosensor was previously performed manually.
This degree project report describes the development of an automatic procedure for the calibration of the photosensor, and focuses on two main problems. The first problem was the development of an algorithm that performs the calibration, using values of measured luminosity, and the second problem was to find a communication solution to transfer these values from the illuminated room to the panel.
The project resulted in a calibration software application and two suggestions of solutions regarding the communication, where the solar panels fibre cables are used as communication medium.

# Application
To run the application:

1. Connect one of the lux-meters and a panel to a computer with ```python3 ``` installed. 

2. Use a terminal emulator to run ```src/python/main.py```

3a. The crosshair buttons sets the sensor settings ± 0.01 from the current value

3b. The "search" button starts the algorithm

3c. The "reset" button sets the sensor to the value of when the application started 
