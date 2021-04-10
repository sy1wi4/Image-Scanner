import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


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


def adaptive_mean_thresholding(image_name, block_size):
    img = cv.imread(image_name, 0)
    print("img\n", img)
    # blockSize determines the size of the neighbourhood area
    # C is a constant
    thresh = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, blockSize=block_size, C=5)
    plot_comparison(img, thresh, "Adaptive mean thresholding")


def adaptive_gaussian_thresholding(image_name, block_size):
    img = cv.imread(image_name, 0)
    print("img\n", img)
    # blockSize determines the size of the neighbourhood area
    # C is a constant
    thresh = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, blockSize=block_size, C=5)
    plot_comparison(img, thresh, "Adaptive gaussian thresholding")


if __name__ == '__main__':
    # cv.IMREAD_COLOR flag -  convert image to the 3 channel BGR color image
    # cv.imread() - returns numpy.ndarray

    global_thresholding('image1.jpg')
    adaptive_mean_thresholding('image1.jpg', 7)
    adaptive_gaussian_thresholding('image1.jpg', 7)
    adaptive_gaussian_thresholding('image1.jpg', 77)
    adaptive_gaussian_thresholding('image1.jpg', 777)
    adaptive_gaussian_thresholding('image1.jpg', 7777)

    # as blockSize grows, adaptive threshold is more like simple threshold



