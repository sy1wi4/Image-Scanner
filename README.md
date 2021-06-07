# Image-Scanner
#### Simple scanner using different thresholding methods with adaptive window selection for uneven lighting image.

One global thresh is not enough if we are dealing with an uneven lighting image. To print them, for example, we need 
a more precise method - that considers a small set of neighboring pixels at a time and determine the appropriate threshold. 

Scanner takes an image (with different lighting conditions in different parts) and applies Gaussian adaptive thresholding to it. 
You can also pick different method - Otsu's binarization, but it works fine only for bimodal images (its histogram has 
bimodal distribution).

### Usage example
![](https://github.com/sy1wi4/Image-Scanner/blob/master/utils/usage.gif)

#### Scan uneven ligting image
You can change size of neighbourhood area using slider
<img src="https://github.com/sy1wi4/Image-Scanner/blob/master/utils/scan_adaptive_7.png" width="300" hspace="30"/> <img src="https://github.com/sy1wi4/Image-Scanner/blob/master/utils/scan_adaptive_109.png" width="300"/>

