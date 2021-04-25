import cv2 as cv
from matplotlib import pyplot as plt
import otsu_binarization


def plot_comparison(original, thresh, title):
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(original, 'gray')
    axes[0].set_title("Original")
    axes[0].axes.get_xaxis().set_visible(False)
    axes[0].axes.get_yaxis().set_visible(False)
    axes[1].imshow(thresh, 'gray')
    axes[1].set_title(title)
    axes[1].axes.get_xaxis().set_visible(False)
    axes[1].axes.get_yaxis().set_visible(False)
    plt.show()


def global_thresholding(image_name):
    img = cv.imread(image_name, 0)
    print("img\n", img)
    image, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    plot_comparison(img, thresh, "Global thresholding")
    return thresh


def adaptive_mean_thresholding(image_name, block_size):
    # The threshold value is the mean of the neighbourhood area minus the constant C

    img = cv.imread(image_name, 0)
    print("img\n", img)
    # blockSize determines the size of the neighbourhood area
    # C is a constant
    thresh = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, blockSize=block_size, C=5)
    plot_comparison(img, thresh, "Adaptive mean thresholding")


def adaptive_gaussian_thresholding(image_name, block_size):
    #  The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C

    img = cv.imread(image_name, 0)
    print("img\n", img)
    # blockSize determines the size of the neighbourhood area
    # C is a constant
    thresh = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, blockSize=block_size, C=5)
    plot_comparison(img, thresh, "Adaptive gaussian thresholding")


def otsu_thresholding(image_name):
    # Automatically calculates a threshold value from image histogram
    # (for bimodal images, otherwise binarization is not accurate)

    img = cv.imread(image_name, 0)
    print("img\n", img)
    image, thresh = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    plot_comparison(img, thresh, "Otsu's thresholding")


def otsu_thresholding_filtered(image_name):
    # Additionally image is filtered with a 5x5 gaussian kernel to remove the noise
    img = cv.imread(image_name, 0)
    print("img\n", img)
    blur = cv.GaussianBlur(img, (5, 5), 0)
    image, thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    plot_comparison(img, thresh, "Otsu's thresholding filtered")


if __name__ == '__main__':
    # cv.IMREAD_COLOR flag -  convert image to the 3 channel BGR color image
    # cv.imread() - returns numpy.ndarray

    # example of image with uneven lighting image
    global_thresholding('images/image1.jpg')
    # adaptive_mean_thresholding('images/image1.jpg', 7)
    # adaptive_gaussian_thresholding('images/image1.jpg', 7)
    # adaptive_gaussian_thresholding('image/image1.jpg', 77)
    # adaptive_gaussian_thresholding('image/image1.jpg', 777)
    # adaptive_gaussian_thresholding('image/image1.jpg', 7777)
    # as blockSize grows, adaptive threshold is more like simple threshold
    otsu_thresholding('images/image1.jpg')
    # otsu_thresholding_filtered('images/image1.jpg')
    # # OWN OTSU'S BINARIZATION
    # otsu_binarization.binarization('images/image1.jpg')

    # # example of image with even lighting
    # global_thresholding('image/image3.jpg')
    # otsu_thresholding_filtered('image/image3.jpg')

    # # histogram of bimodal image
    # im = cv.imread('images/image5.png', 0)
    # plt.hist(im.ravel(), 30)
    # plt.show()

    # # example of bimodal image
    # global_thresholding('images/image5.png')
    # otsu_thresholding('images/image5.png')
    # otsu_thresholding_filtered('images/image5.png')
    #
    # # OWN OTSU'S BINARIZATION
    # otsu_binarization.binarization('images/image5.png')
