### Blob Detection

- Can detect objects without ML on uniform background
- LoG (Laplacian of Gaussian)
	- Apply gaussian blur
		- Convolution with Gaussian kernel
		- Reduces noise
	- Laplacian Operator
		- Second Order Derivatives
		- Edge detection
- Convolution: apply some function to each kernel as a matrix operation
$$\frac{1}{16}\begin{bmatrix}
1 & 2 & 1 \\
2 & 4 & 2 \\
1 & 2 & 1
\end{bmatrix}$$
- Example gaussian blur convolution matrix
	- Use dot product
	- Gaussian matrix = 2d normal distribution
- Laplacian takes 2nd order derivative in x and y
	- 0 crossing = edge
	- Gaussian makes edges more defined
	- derivative approximated using kernel
- builtin methods
	- OpenCV builtin SimpleBlobDetector
		- apply binary threshold masks
		- produces noise
	- take centers of blobs and merge if close
	- filter based on eccentricity, confidence, etc
### Yolo
- linear classifier + perceptron
- outputs probabilities for each category
- ML
	- Update weights each epoch
	- define loss function to penalize/reward
		- move towards minimal loss by computing gradient and simulated annealing
	- Pooling reduces overfitting dimensions and noise
	- learned kernels
- YOLO is one-shot
	- two-shot more accurate, first pass proposes object locations
- Data sets
	- Training
		- used to train
	- Validation
		- tunes hyperparameters
	- Test
		- evaluates models
- Overfitting
	- memorizes pattern/loses generality
### Future
- Yolo is slow
- OpenCV may be enough?
- Custom CNN?