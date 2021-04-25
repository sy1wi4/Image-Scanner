import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def plot_c(original, thresh, title):
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(original, 'gray')
    axes[0].set_title("Original")
    axes[0].axes.get_xaxis().set_visible(False)
    axes[0].axes.get_yaxis().set_visible(False)
    axes[1].imshow(original > thresh, 'gray')
    axes[1].set_title(title)
    axes[1].axes.get_xaxis().set_visible(False)
    axes[1].axes.get_yaxis().set_visible(False)
    plt.show()


# with image filtering
def binarization(image_name, plot=False):
    img = cv.GaussianBlur(cv.imread(image_name, 0), (5, 5), 0)

    # compute histogram
    values = img.flatten()
    hist, bins = np.histogram(values, range(257))

    # normalize to get probabilities of each intensity level
    norm_hist = hist/np.sum(hist)

    # p1, p2 - probabilities of the two classes separated by a threshold t
    # m1, m2 - means of these two classes
    # v - inter-class variance

    thresh = -1
    max_v = -1
    for t in range(256):
        p1 = np.sum(norm_hist[:t])
        p2 = np.sum(norm_hist[t:])
        m1 = np.sum([i for i in range(t)] * hist[:t])/p1 if p1 != 0 else np.nan
        m2 = np.sum([i for i in range(t, 256)] * hist[t:])/p2 if p2 != 0 else np.nan

        v = p1 * p2 * (m1 - m2) ** 2
        if v > max_v:
            thresh = t
            max_v = v

    if plot:
        plot_c(img, thresh, "Own Otsu's thresholding")

    return thresh




