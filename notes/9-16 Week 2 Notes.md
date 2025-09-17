
### Imagery Techniques

- **Nadir** imaging is straight downwards
- **Oblique** is at an angle, high/low describes the steepness of angle to the ground
- Gimbal cameras:
	- Switching from optical zoom to digital zoom
	- Optical zoom is actual zoom, better quality
	- Digital zoom lower quality, just uses cropping
- OpenCV
	- openCV is in python (!!! YAY NO MORE JAVACV PORT)
	- Optical flow: calculating velocity w/ image stream
	- deblurring and refining
	- editing
	- detection

### OpenCV Features
- Basic RGB manipulation
- Image properties
- Feature matching without AI using Sift
	- Sometimes inaccurate
- Can be slow

### OpenDroneMap
- Mostly premade, convenient functions all there
- Workflow
	- Give pictures with geotags, uses same workflow as cv but faster
	- Adjust parameters based on data from trial and error
	- Generates ground mesh with colored material (very cool)
		- gets discarded NOOOO
- The Good
	- Very simple to use
	- cool api
	- lots of cool data/models and stuff
- The Bad
	- Not optimized for RT, slow
	- needs good geotags
	- heavy library
- The Ugly
	- 
- Next Steps
	- make better RT opencv alg
	- get better at OpenDroneMap
	- Other Stuff (SLAM, optical flow)