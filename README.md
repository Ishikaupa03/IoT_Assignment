# IoT_Assignment
The code for an Internet of Things solution that a hotel chain created to guarantee ideal room temperatures for patron comfort is stored in this repository. The method is to read temperature sensor data, publish it to a MQTT broker, and sound an alert if the temperature rises above a predetermined threshold for a predetermined amount of time. An API is also included for accessing the sensor data.

Part One: Publisher Program
An MQTT broker receives data from a Python script that continuously reads from a simulated temperature sensor and publishes it on a particular topic.

Important characteristics:

simulates data from a temperature sensor.
data is published to the MQTT broker.
runs continually for the purpose of monitoring temperature.
Publisher.py is the file.

2. Subscription Scheme
To obtain sensor data, a Python script subscribes to the MQTT topic.
