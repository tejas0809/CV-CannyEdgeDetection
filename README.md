## Objective
The objective of the project was to implement canny edge detection for an image without the use of already available libraries like openCV. 

## Results 
![alt text](https://github.com/tejas0809/CV-CannyEdgeDetection/blob/master/canny_dataset/118035.jpg?raw=true)
![alt text](https://github.com/tejas0809/CV-CannyEdgeDetection/blob/master/output_canny_dataset/118035.png?raw=true)
![alt text](https://github.com/tejas0809/CV-CannyEdgeDetection/blob/master/canny_dataset/135069.jpg?raw=true)
![alt text](https://github.com/tejas0809/CV-CannyEdgeDetection/blob/master/output_canny_dataset/135069.png?raw=true)
![alt text](https://github.com/tejas0809/CV-CannyEdgeDetection/blob/master/canny_dataset/189080.jpg?raw=true)
![alt text](https://github.com/tejas0809/CV-CannyEdgeDetection/blob/master/output_canny_dataset/189080.png?raw=true)
![alt text](https://github.com/tejas0809/CV-CannyEdgeDetection/blob/master/canny_dataset/21077.jpg?raw=true)
![alt text](https://github.com/tejas0809/CV-CannyEdgeDetection/blob/master/output_canny_dataset/21077.png?raw=true)
![alt text](https://github.com/tejas0809/CV-CannyEdgeDetection/blob/master/lowLight_dataset/2015_00010.jpg?raw=true)
![alt text](https://github.com/tejas0809/CV-CannyEdgeDetection/blob/master/ExtraCredit/output_lowLight_dataset/2015_00010.png?raw=true)
![alt text](https://github.com/tejas0809/CV-CannyEdgeDetection/blob/master/lowLight_dataset/2015_03062.jpg?raw=true)
![alt text](https://github.com/tejas0809/CV-CannyEdgeDetection/blob/master/ExtraCredit/output_lowLight_dataset/2015_03062.png)



## Directory Structure:
- readme.txt
- canny_dataset: folder containing input images
- lowLight_dataset: folder containing images for lowLight
- output images: folder containing the output images. 
- ExtraCredit Folder: Folder containing code, dataset and output for low light images.                  
- python files: cannyEdge.py, edgeLink.py, findDerivatives.py, helpers.py, interp.py, nonMaxSup.py, Test_script.py, utils.py (this implementation uses interpolation for edge linking)
- Discretized_Edge_Linking(Extra) Folder containing the other implementation in which the edge linking is done by discretization of angles. 

*Note: The high and low thresholds have been set individually for each of the output images by taking multipliers of the mean and standard deviation of the gradient magnitudes. 



## Main Components
The algorithm can be broken down into the following main parts:
1. findDerivatives.py:
     Performs a convolution on the image with the derivative of a gaussian in order to perform smoothing on the image. 
     The gaussian distribution is taken from the GaussianPDF_2D function which was already provided in utils. However, the parameters of the gaussian have been tuned, (reducing the sigma for low light images). The function returns magnitude of gradient matrix, gradient matrix in x direction, gradient matrix in y direction and the matrix for angle along the maximum change in gradient.
1. nonMaxSup.py:
    Looks in the direction of maximum gradient and computes the magnitude of the neighboring points in the direction of the gradient change. The intensity values for neighbors are obtained by interpolating the values of the adjacent pixel values. Further, if the value of the current pixel is greater than both the neighbours, then keeps the pixel in the resultant. 
    The implementation is done in parallel using a meshgrid instead of iterating over the matrix. The interp2 function given in utils has been used for interpolation. 

1. edgeLink.py:    
    Two versions of edge linking have been implemented: 
    a) without discretisation (i.e. by finding the values in direction of edge by interpolation)
    b) By discretisation of angles in the edge direction.
    
    Both the versions take the supressed edge map, and decide upon a high threshold and low threshold to filter out the strong and the weak edges in the edgemap, and construct the weak edgemap and the strong edgemap. Further the direction of the edge is calculated, which is perpendicular to the Orientation matrix(which had the direction of maximum gradient). 
    
    In the non-discretized approach, the two side points are found at unit distance from the current pixel along the edge orientation,  and further these points are interpolated and their magnitudes are checked. If they are greater than the upper threshold, then they are updated in the edge map. The corresponding points are also removed from the weak edge map. strong edge map is also updated and again iterated over until convergence. 
    
    In the discretization method, these angles are further discretized into bins of 0, pi/4, pi/2, 3pi/4. Further, eight neighboring matrices have been constructed in each direction by shifting the strong edge Map. Also, indexes where the orientation becomes 0, pi/4, pi/2, and 3pi/4 have been stored in separate matrices respectively. The strong EdgeMap is updated, by checking the values of the angles at all eight neighbours and the presence of a pixel in the weak edge map at the corresponding locations. This is done until there are no new neighbors discovered which should be turned from weak to strong. The answer is returned which is the output of the Canny edge detector. 
    
 
   The high and low thresholds have been set individually for each of the output images by taking multipliers of the mean and standard deviation of the gradient magnitudes. The multipliers are obtained for each of the image by trial and error and intuition by lookking at each image. 
    
  In the final implementation, the mean of all the multipliers is taken. 
    
    
