### Hardware

- Flight Controllers
	- Maintains drone stability
	- Follows commands
	- processes control loops
	- radio input
	- not autonomous
	- forwards sensor data
- Jetson (Onboard CPU/GPU)
	- high-level tasks
	- obj detection, SLAM, etc
	- receives sensor data from flight controller, sends commands
	- serial, ethernet or usb

### Sensors

- Flight Controller
	- IMU
		- accelerometer
			- detects gravity, stable down heading
		- gyro
	- Barometer
		- pressure used to estimate altitude
	- Magnetometer
		- built into IMU sometimes (9-axis)
		- Heading corrects yaw drift
	- GPS module
		- global positioning (you could almost say its a... global positioning system) 
		- Real Time Kinematics
		- waypoint nav, return to home
- Cameras (yay)
	- 4k30hz pog
	- gimbal for stability
	- digital zoom good enough for this year, lighter

### RC 

- transmitter (tx)
	- handheld by pilot
- receiver (rx)
	- commands to flight controller
- uses serial not pwm

### Communication Protocols

- Serial (UART)
	- FC-computer, gps, telemetry
		- tx & rx line, shared ground
		- binary signal against clock
- CAN
	- ITS CAN
		- OMG ITS CAN
			- IS THAT A CANBUS REFERENCE
				- LIKE CAN
	- multidevice
	- smart ESCs, gimbals, sensor networks
	- error checking
- I2C
	- data line and clock line SDA & SCL
		- slower (barometer, magnetometer, imu)
	- network multiple devices, only one can send
- SPI
	- multiple devices listening to one master device
	- MISO - master in slave out
	- MOSI - master out slave in
	- SCLK - clock
	- CS - chip select, switch between non-master devices
- MAVLink
	- encoding format
	- send/receive info between FC, computer, ground
	- takes up to seconds
- DDS
	- rt publish-subscribing
	- better for rt stuff like control loops
	- used in ROS 2 (goal: ROS integration)
	- FC-computer, used over UART

### FC Firmware

- ran out of time rip
- we dont make this ourselves (thankfully)
- PID YAYYY
- Ardupilot
	- auto, mapping
- Betaflight
	- racing
- PX4
	- modular, industry standard