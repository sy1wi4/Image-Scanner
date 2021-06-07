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
You can change size of neighbourhood area using slider.

<img src="https://github.com/sy1wi4/Image-Scanner/blob/master/utils/scan_adaptive_7.png" width="350" hspace="30"/> <img src="https://github.com/sy1wi4/Image-Scanner/blob/master/utils/scan_adaptive_109.png" width="350"/>

As mentioned above, the Otsu's method is not doing well in this case.

<img src="https://github.com/sy1wi4/Image-Scanner/blob/master/utils/scan_otsu.png" width="450" hspace="30"/>

#### Scan bimodal image
To scan bimodal image Otsu method is more suitable.

<img src="https://github.com/sy1wi4/Image-Scanner/blob/master/utils/scan_bimodal_adaptive.png" width="350" hspace="30"/> <img src="https://github.com/sy1wi4/Image-Scanner/blob/master/utils/scan_bimodal_otsu.png" width="350"/>

#### Save result file
You can save scanned image on your computer (e.g. for printing).

<img src="https://github.com/sy1wi4/Image-Scanner/blob/master/utils/save.png" width="450" hspace="30"/>