
# Fire Detection IoT System 🔥🚨

## Overview

This project is an IoT-based fire detection system designed to enhance building safety. It uses sensors to detect fire and smoke, sending real-time alerts via IoT to notify authorities and occupants. The system can trigger alarms and provide remote monitoring through a web or mobile interface.

## Features

-   🔥 **Fire and Smoke Detection:** Uses dedicated sensors to detect fire and smoke in real-time.
-   📡 **IoT Connectivity:** Sends notifications via the SIM800L module.
-   🔔 **Alarm System:** Activates buzzers and relays for emergency alerts.
-   📟 **LCD Display:** Shows real-time system status and alerts.
-   🏠 **Remote Monitoring:** Can be integrated with a web or mobile app for remote access.

## Components Required

### Electronics:

-   Arduino Nano
-   LCD Screen 1602 (with I2C module)
-   SIM800L Module + Phone SIM
-   Fire Sensor
-   Smoke Sensor (MQ-2 or similar)
-   Buzzer
-   Relays (for activating fire suppression or alarms)

### Wiring & Power:

-   BEC Spray 0.3
-   3x5 Silicon Wire
-   Test Board
-   Jumper Wires 
-   Formex Plate
-   18650 Battery x 2
-   2P 18650 Battery Base
-   Switch & 5.5mm Female Jack
-   2S 8.4V Battery Charger

## Circuit Diagram
----

## Installation & Setup

1.  **Assemble the Hardware:**
    
    -   Connect the fire and smoke sensors to the Arduino Nano.
    -   Connect the LCD screen via I2C interface.
    -   Interface the SIM800L module for sending alerts.
    -   Wire up the buzzer and relays for alarms.
    -   Power the system using 18650 batteries with proper voltage regulation.
2.  **Upload the Code:**
    
    -   Install the Arduino IDE.
    -   Connect the Arduino Nano via USB.
    -   Upload the `he_thong_bao_chay.ino` sketch from this repository.
    -   Ensure all required libraries (Wire.h, SoftwareSerial.h, etc.) are installed.
3.  **Testing:**
    
    -   Power on the system and check the LCD display.
    -   Simulate smoke/fire detection and verify alarm activation.
    -   Check if SMS alerts are sent via SIM800L.

## Usage

-   Place the system in a strategic location within the building.
-   If smoke or fire is detected, the system will trigger an alarm and send SMS alerts.
-   Users can remotely monitor the status if integrated with a web or mobile app.

## Future Enhancements

-   Integration with cloud services for real-time monitoring.
-   Adding temperature sensors for better fire risk assessment.
-   Implementing a mobile app for remote control and alerts.


