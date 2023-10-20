---
title: "Autonomous Vehicle RDM53 - a THM Project"
date: 2023-02-26T21:53:30+01:00
categories:
  - blog
tags:
  - update
---

# RDM53

This project has already been finished for some time, but I never got around to actually write a blogpost about it. I will try to keep it short and simple, but if you have any questions feel free to contact me on twitter or via mail (you can find my mail address on my [about page](/about/) or add an issue to the respective repository on [github](www.github.com/jahknem)). 

The [RDM53](https://github.com/paspf/RDM53-1) was the first hardware project at the THM in which I was involved. It was part of the project management module, in which we were to create a scenario in which 2 autonomous wheeled vehicles were to try to compete to get to their respective goals first. They each had a candle on top, while an autonomous robot was to try to extinguish the candle. Each robot was build by one of 3 teams.

My team chose to create the autonomous Vehicle using as scaffold the [Joy-It Robot Car Kit 4WD](https://joy-it.net/de/products/Robot03). As the controlling computer we chose to use the WeMos LolinD32, a board that uses the ESP32 microcontroller. The ESP32 is a very powerful microcontroller, which has a dual core processor, 4MB of RAM and, as we thought at the time, enough GPIO pins to access all motors and sensors. Due to more sensors than initially planned being added, we also added a port expander of the type PCF85741 to the setup. It also has integrated WiFi and Bluetooth, which we used to communicate with the robot. The code running on the ESP32 was written in C++ using the Arduino Framework.

## Components

| Component  | Type | Function |
| ------------- | ------------- | ------------- |
| WeMos LolinD32  | microcontroller board | brain of the RDM53 |
| PCF85741  | port expansion | - |
| DRV8833  |  dual H-Bridge motor driver | power electronic |
| GRV IMU 10 DOF v2  | MPU9250 board | accelerometer, gyroscope, magnetometer |
| TCRT5000 | reflective optical sensor |coarse border detection (stripe detection) |
| VL53L0X | laser ranging sensor | obstacle detection |
| HC-SR04P | ultrasonic sensor | obstacle detection |
| TCS34725 | color sensor | adhesive stripe color detection |
| Joy-It Speed sensor | speed sensor | speed calculation |
| Joy-It Robot Car Kit 4WD | scaffold | base of the RDM53 |
| Li-ion 18650 | battery | power source |

## Software 

### Vehicle Control

#### Sensors

#### Motor Control

### Webinterface & Communication

To be able to control the RDM on the fly, paspf created a webinterface, and created a communication protocol to communicate with the RDM. The Communication was done using WebSockets over a TCP Connection.


### Magnetic Calibration

# Lessons Learned