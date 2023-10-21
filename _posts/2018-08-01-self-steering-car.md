---
title: "Autonomous Vehicle RDM53 - a THM Project"
date: 2023-10-21T18:03:30+01:00
categories:
  - blog
tags:
  - vehicle
  - automation
  - project
  - THM
---

# RDM53

This project has already been finished for some time, but I never got around to actually write a blogpost about it. I will try to keep it short and simple, but if you have any questions feel free to contact me on twitter or via mail (you can find my mail address on my [about page](/about/) or add an issue to the respective repository on [github](www.github.com/jahknem)). 

The [RDM53](https://github.com/paspf/RDM53-1) was the first hardware project at the THM in which I was involved. It was part of the project management module, in which we were to create a scenario in which 2 autonomous wheeled vehicles were to try to compete to get to their respective goals first. They each had a candle on top, while an autonomous robot was to try to extinguish the candle. Each robot was build by one of 3 teams. More information about this project can be found on the [project page](https://www.thm.de/iem/fachbereich/service/aktuelles/abschlussrennen-autonome-fahrzeuge-im-modul-projektmanagement.html) of the THM.

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

### Sensors

For sensor we considered multiple different sets of snesor, but given the budget and the computing constraints of our chosen CPU platform we settled on the following sensors:
* a reflective optical sensor for stripe detection
* a color sensor for adhesive stripe color detection
* a laser ranging sensor for obstacle detection and distance measurement
* an ultrasonic sensor for obstacle detection and distance measurement
* a 9DoF sensor for orientation and acceleration measurement
* a speed sensor for speed measurement

Using a combination of the reflectibe optical sensor and the color sensor we were able to detect the adhesive stripes and their color, by which we calculated the limit of track as well as the the win area. This approach led to problems when the stripe was wet. As soon as the stripes were covered with water, the color sensor got different readings, leading to our algorithm not triggering. We only discovered this issue during the trial run one hour before the final run, and were sadly not able to fix it in time.
Using the laser and ultra sonic sensors we also expected to be able to detect obstacles and avoid them, with the laser sensor allowing for more exact measurements for a better map and the ultra sonic sensor allowing for a wider spread of detection. Given our requirements, we could probably have done without the laser ranging sensor.
The 9DoF sensor was used to be able to calculate the orientation of the vehicle, and the speed sensor was used to be able to calculate the speed of the vehicle. Using a combination of these we could calculate the 2D position of the vehicle by orientation and distance travelled. 
This combination of information allowed us to create a 2D map of the track, which we could then use to navigate it. Due to time constrains, we did not use the map to navigate the track, instead opting for 2 simpler solutions.


### Motor Control

The motor control would have been 2 diffent layers. [paspf](https://github.com/paspf) created an EngineInterface in which each Engine could be controlled on its own, which used the ledc library. Additionally I created a steering Interface which allowed to set specific parameters for how the vehicle should move, e.g. if it should move in a circle, forward, describe a curve etc. 
The parameters which could be set were:
* Speed in 0-255, where 0 was max backwards and 255 max forwards
* Degrees in 0-180, where 0 was hard left, 90 straight and 180 hard right

### Autonomous Schemes

We created 4 different autonomous schemes, 3 of which were applicable to the task, while the fourth was a sole obstacle avoidance algorithm.

#### Line Following

The line-following algorithm is one of the key autonomous schemes we implemented in the RDM53. The primary purpose of this algorithm is to keep the vehicle on the track by following a line or a set of lines.

We utilized the reflective optical sensor (TCRT5000) and the color sensor (TCS34725) to detect the lines on the track. The optical sensor was responsible for coarse border detection, while the color sensor identified the specific color of the adhesive stripes on the track. The initial

The main challenges were in tuning the sensor readings and motor control to work in harmony. Too fast, and the vehicle would miss the line; too slow, and it would be inefficient.

Performance

The line-following algorithm proved to be quite reliable. It could handle sharp turns as well as moderate changes in line width and color. 2 issues were that with many sharp turn, it took a while to get to the win area, and that the algorithm was not able to handle wet lines, which was due to a lower level problem.

#### Random Direction

The "Random Direction" algorithm was our plan B, employed as a simpler yet effective approach to navigate the RDM53 through the track. This algorithm was designed to, hopefully, reach the win area sooner compared to the line-following algorithm.

The algorithm essentially makes the vehicle move in random directions while avoiding obstacles. We utilized the laser ranging sensor (VL53L0X) and the ultrasonic sensor (HC-SR04P) for obstacle detection.

1. Initialization: Upon startup, the vehicle initializes its sensors and motors.
2. Obstacle Check: The vehicle continuously scans for obstacles using the laser and ultrasonic sensors.
3. Obstacle and Line Avoidance: If an obstacle or an Edg Stripe is detected, the vehicle reverses a bit, turns a random angle, and continues.
4. Loop: Until the Win Area is reached, the algorithm repeats this approach

The biggest challenge was to make sure the vehicle didn't end up in an infinite loop, especially in corners or dead-ends. To mitigate this, the vehicle turns in the opposite direction if it detects an obstacle or an edge stripe while turning. This however did not solve the problem for sharp egdes.

The Random Direction algorithm was less efficient than the line-following one, whcih was especially due to it often zigzagging along a straight edge of the parcours.

#### Map Creation & Navigation (not fully implemented)

The Map Creation and Navigation algorithm was our plan C, which we did not get to implement fully. The idea was to create a map of the track, and then use this map to navigate the track. The map was created using the 9DoF sensor (GRV IMU 10 DOF v2) and the speed sensor (Joy-It Speed sensor) additionally to the previous sensors. The 9DoF sensor was used to calculate the orientation of the vehicle, while the speed sensor was used to calculate the distance travelled. Using these two values, we could calculate the 2D position of the vehicle. This way we could create a map of the track, which we could then use to navigate the track. For saving the map we had 2 different schemes. 
a.) Create a 2D matrix in memory in which we would mark all the positions the vehicle had been to and all recogniced obstacles and edges, and save this matrix to the flash memory of the ESP32. Given this map, the algorithm could have been able to discover positions in which it was not yet in the search for the win area.
b.) As this would have been very memory intensive, a different approach was saving only the locations of the obstacles and lines, in a sort of recursive dependency list, with the initial position of the vehicle being (0,0), and the coordinates of the obstacles being calculated from there. Te be able to save memory, we would have saved an obstacle always as a circle. Obstacles very near to each other would have been recogniced as a single obstacle.
Regardless of which approach would have been used, a dijsktra algorithm would habe been used to find the shortest path to expected win areas.

## Webinterface & Communication

To be able to control the RDM on the fly, paspf created a webinterface, and created a communication protocol to communicate with the RDM. The Communication was done using WebSockets over a TCP Connection.

I have uploaded the Webinterface to my site, you can find it [here](/rdm53/). The source code can be found [here](https://github.com/paspf/RDM53-1/tree/master/Webinterface). While the webinterface is neither very pretty, nor currently functional, due to not having a RDM to test it on, it should give you a good idea of how it worked.  

We initially tried to use the ESP32 as a Webserver, but due to our own code being too demanding on the ESP32, we did not want to have the additional load of a webserver. Therefore, we did not deploy the Website on a Webserver at all, instead opting of opening the Site locally.

### Protocol

As none of us had any previous experience with this kind of project, we decided to create our own protocol, in the hopes of it being more efficient. Suffice to say that in retrospect we should just have used mqtt, which already had a wide basis of open source libraries we could have used at the time. Nonetheless, our protocol worked remarkibly well for our use case.
As we also communicated via serial connection, we created an interface which could be accessed from either the Websocket or the Serial Connection. Depending on wether we wanted to use either one we would set a flag in the connectivity.h file, recompile the firmware and upload it onto the ESP32.

The protocol we developed had a length of 10 Bytes. The first and the last bytes had a fixed value of 0xB respective 0xC, so that we would be able to recognize the message when it was sent. The middle 8 Bytes of the message were used for select / control Bytes (first 4 Bytes) and Payload (last 4 Bytes). Using this scheme we had the ability to choose up to 16 different commands, and send up to 4 Bytes of data with each command, allowing us to also sent float values.



#### Select / Control Scheme

The first byte was used to select the reason the message was sent: Switch the Device mode (0x2) or to transmit data (0x3). The second byte was used to select the mode of operation. The third and fourth byte were used to select the subsystem and the sensor or actuator respectively. As can be seen in this first description alone, most bytes were very much underused, which was due to us expecting to create a much more sophisticated system. In this project, I learned that the complexity of a project may increase more than linearly with each added feature.

 * PROTOCOL     PAYLOAD (last payload byte)
 * 3rd Byte     START     END
 * ----------------------------------------------------
 * 0x00 00 00 + 0x00      0xFF : Autonomous
 * 0x01 00 00 + 0x00      0x0F : Remote Control (static)
 * 0x01 00 00 + 0x10      0x1F : Remote Control (dynamic)
 * 0x02 00 00 + 0x00      0x00 : Chill
 * 0x03 00 00 + 0x00      0x00 : Reset (Reboot device)

This way we could switch between the different modes of operation: one fully autonomous mode, two different remote control modes (static as in slow and dynamic as in fast) and a chill mode, which essentially was a disarm mode with which we would make sure we could retrieve the device safely. The reset command was used to reboot the ESP32.

The 3rd byte of the select control scheme was used to target a subsystem of the RDM, while the 4th byte was used to target a specific sensor or actuator. The subsystems were as follows:
 * 0x00 : Remote Control
 * 0x01 : Calibration Data
 * 0x02 : Testing
 * 0x03 : Query

Why it was absolutely required that we could sent the calibration data via this protocol is explained in the section Magnetic Calibration below.

## External 9DoF Calibration

The calibration of the 9DoF Sensor was my task. I initially expected to just be able to use some existing script from github or stackoverflow, but boy was I out of my depth. 

# Lessons Learned

* Project Management is more important than the code
* People Management and expectation management is difficult
* Know your skills, know your limits, know your team
* If a feature does not seem to be implementable with your current ressources, don't be afraid to ax it and think about alternatives.